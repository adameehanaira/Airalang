import os
import sys
import math
import time
import json
import random
import hashlib
import base64
import socket
import sqlite3
import urllib.request
import urllib.parse
import threading
from concurrent.futures import ThreadPoolExecutor

class AiraModule:
    def __init__(self, name, methods=None):
        self.name = name
        self.methods = methods or {}

    def get(self, prop_name):
        if prop_name in self.methods:
            return self.methods[prop_name]
        raise AttributeError(f"AiraLang Module '{self.name}' has no method or property '{prop_name}'")

class AiraSQLiteDB:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

    def execute(self, sql, params=None):
        cursor = self.conn.cursor()
        if params:
            cursor.execute(sql, tuple(params) if isinstance(params, list) else (params,))
        else:
            cursor.execute(sql)
        self.conn.commit()
        return cursor.rowcount

    def query(self, sql, params=None):
        cursor = self.conn.cursor()
        if params:
            cursor.execute(sql, tuple(params) if isinstance(params, list) else (params,))
        else:
            cursor.execute(sql)
        rows = cursor.fetchall()
        result = []
        for r in rows:
            result.append({k: r[k] for k in r.keys()})
        return result

    def insert(self, table, data_dict):
        if not isinstance(data_dict, dict):
            raise TypeError("sqlite.insert requires a dictionary of column: value")
        columns = ", ".join(data_dict.keys())
        placeholders = ", ".join(["?"] * len(data_dict))
        sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        return self.execute(sql, list(data_dict.values()))

    def close(self):
        self.conn.close()
        return True

    def get(self, prop_name):
        if hasattr(self, prop_name):
            return getattr(self, prop_name)
        raise AttributeError(f"SQLite DB object has no property '{prop_name}'")

def create_sqlite_module():
    def open_db(path):
        db = AiraSQLiteDB(path)
        return AiraModule("sqlite_conn", {
            "execute": db.execute,
            "query": db.query,
            "insert": db.insert,
            "close": db.close
        })

    return AiraModule("sqlite", {
        "open": open_db,
        "connect": open_db
    })

def create_net_module():
    def scan_port(host, port, timeout=2.0):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(float(timeout))
            result = s.connect_ex((str(host), int(port)))
            s.close()
            return result == 0
        except Exception:
            return False

    def scan_ports(host, start_port, end_port, timeout=1.0):
        open_ports = []
        for p in range(int(start_port), int(end_port) + 1):
            if scan_port(host, p, timeout):
                open_ports.append(p)
        return open_ports

    def resolve(domain):
        try:
            return socket.gethostbyname(str(domain))
        except Exception as e:
            return f"Error: {e}"

    def local_ip():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except Exception:
            return "127.0.0.1"

    def tcp_send(host, port, message, timeout=5.0):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(float(timeout))
            s.connect((str(host), int(port)))
            s.sendall(str(message).encode('utf-8'))
            data = s.recv(4096)
            s.close()
            return data.decode('utf-8', errors='ignore')
        except Exception as e:
            return f"Socket Error: {e}"

    return AiraModule("net", {
        "scan_port": scan_port,
        "scan_ports": scan_ports,
        "resolve": resolve,
        "local_ip": local_ip,
        "tcp_send": tcp_send
    })

def create_file_module():
    def read_file(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    def write_file(path, content):
        with open(path, "w", encoding="utf-8") as f:
            f.write(str(content))
        return True

    def append_file(path, content):
        with open(path, "a", encoding="utf-8") as f:
            f.write(str(content))
        return True

    def exists(path):
        return os.path.exists(path)

    def delete(path):
        if os.path.exists(path):
            os.remove(path)
            return True
        return False

    def size(path):
        if os.path.exists(path):
            return os.path.getsize(path)
        return -1

    return AiraModule("file", {
        "read": read_file,
        "write": write_file,
        "append": append_file,
        "exists": exists,
        "delete": delete,
        "size": size
    })

def create_os_module():
    def cmd(command):
        return os.popen(command).read().strip()

    def env(var_name, default=""):
        return os.environ.get(var_name, default)

    def platform():
        return sys.platform

    def cwd():
        return os.getcwd()

    def listdir(path="."):
        return os.listdir(path)

    def mkdir(path):
        os.makedirs(path, exist_ok=True)
        return True

    return AiraModule("os", {
        "cmd": cmd,
        "system": cmd,
        "env": env,
        "getenv": env,
        "platform": platform,
        "cwd": cwd,
        "getcwd": cwd,
        "listdir": listdir,
        "mkdir": mkdir
    })

def create_math_module():
    return AiraModule("math", {
        "sqrt": lambda x: math.sqrt(x),
        "floor": lambda x: math.floor(x),
        "ceil": lambda x: math.ceil(x),
        "abs": lambda x: abs(x),
        "round": lambda x, d=0: round(x, d) if d else round(x),
        "pow": lambda b, e: math.pow(b, e),
        "random": lambda low=0, high=1: random.randint(int(low), int(high)) if isinstance(low, int) and isinstance(high, int) else random.uniform(low, high),
        "pi": math.pi,
        "e": math.e
    })

def create_time_module():
    return AiraModule("time", {
        "now": lambda: time.strftime("%Y-%m-%d %H:%M:%S"),
        "time": lambda: time.time(),
        "sleep": lambda s: time.sleep(s)
    })

def create_json_module():
    return AiraModule("json", {
        "parse": lambda s: json.loads(s),
        "mkstring": lambda obj, indent=2: json.dumps(obj, indent=indent),
        "stringify": lambda obj, indent=2: json.dumps(obj, indent=indent)
    })

def create_http_module():
    def get(url, headers=None):
        req_headers = {"User-Agent": "AiraLang/1.3 (Termux; Android)"}
        if isinstance(headers, dict):
            req_headers.update(headers)
        req = urllib.request.Request(url, headers=req_headers)
        try:
            with urllib.request.urlopen(req, timeout=15) as response:
                return response.read().decode("utf-8")
        except Exception as e:
            raise RuntimeError(f"HTTP GET Error: {e}")

    def post(url, data_payload=None, headers=None):
        req_headers = {"User-Agent": "AiraLang/1.3 (Termux; Android)"}
        if isinstance(headers, dict):
            req_headers.update(headers)
        encoded_data = None
        if isinstance(data_payload, dict):
            req_headers["Content-Type"] = "application/x-www-form-urlencoded"
            encoded_data = urllib.parse.urlencode(data_payload).encode("utf-8")
        elif isinstance(data_payload, str):
            encoded_data = data_payload.encode("utf-8")
        req = urllib.request.Request(url, data=encoded_data, headers=req_headers)
        try:
            with urllib.request.urlopen(req, timeout=15) as response:
                return response.read().decode("utf-8")
        except Exception as e:
            raise RuntimeError(f"HTTP POST Error: {e}")

    def download(url, dest_path):
        req = urllib.request.Request(url, headers={"User-Agent": "AiraLang/1.3"})
        try:
            with urllib.request.urlopen(req, timeout=30) as response, open(dest_path, "wb") as out_file:
                out_file.write(response.read())
            return True
        except Exception as e:
            raise RuntimeError(f"HTTP Download Error: {e}")

    def status(url):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "AiraLang/1.3"})
            with urllib.request.urlopen(req, timeout=10) as response:
                return response.getcode()
        except urllib.error.HTTPError as e:
            return e.code
        except Exception:
            return 0

    return AiraModule("http", {
        "get": get,
        "post": post,
        "download": download,
        "status": status
    })

def create_crypto_module():
    def md5(s):
        return hashlib.md5(str(s).encode('utf-8')).hexdigest()

    def sha256(s):
        return hashlib.sha256(str(s).encode('utf-8')).hexdigest()

    def sha1(s):
        return hashlib.sha1(str(s).encode('utf-8')).hexdigest()

    def b64encode(s):
        return base64.b64encode(str(s).encode('utf-8')).decode('utf-8')

    def b64decode(s):
        return base64.b64decode(str(s).encode('utf-8')).decode('utf-8')

    return AiraModule("crypto", {
        "md5": md5,
        "sha256": sha256,
        "sha1": sha1,
        "base64_encode": b64encode,
        "base64_decode": b64decode,
        "b64encode": b64encode,
        "b64decode": b64decode
    })

def create_string_module():
    return AiraModule("string", {
        "upper": lambda s: str(s).upper(),
        "lower": lambda s: str(s).lower(),
        "split": lambda s, sep=" ": str(s).split(sep),
        "replace": lambda s, old, new: str(s).replace(str(old), str(new)),
        "trim": lambda s: str(s).strip(),
        "contains": lambda s, sub: str(sub) in str(s),
        "length": lambda s: len(str(s)),
        "join": lambda lst, sep=" ": sep.join(str(x) for x in lst)
    })

def create_ai_module():
    state = {
        "gemini_key": os.environ.get("GEMINI_API_KEY", ""),
        "groq_key": os.environ.get("GROQ_API_KEY", "")
    }

    def set_key(key, provider="gemini"):
        if str(provider).lower() == "groq":
            state["groq_key"] = str(key)
        else:
            state["gemini_key"] = str(key)
        return True

    def get_key(provider="gemini"):
        return state["groq_key"] if str(provider).lower() == "groq" else state["gemini_key"]

    def ask(prompt, model="gemini-2.5-flash", key=None):
        api_key = key or state["gemini_key"]
        if not api_key:
            if state["groq_key"]:
                return groq(prompt, key=state["groq_key"])
            return f"[Aira AI Engine] Notice: No API Key configured. Call `ai.set_key('YOUR_API_KEY')` or set `GEMINI_API_KEY` in environment. Received prompt: '{prompt}'"

        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
        payload = json.dumps({"contents": [{"parts": [{"text": str(prompt)}]}]}).encode("utf-8")
        req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            return f"[Aira AI Error]: {e}"

    def groq(prompt, model="llama-3.3-70b-versatile", key=None):
        api_key = key or state["groq_key"]
        if not api_key:
            return f"[Aira Groq Error]: No GROQ API key provided. Set GROQ_API_KEY or call ai.set_key('key', 'groq')."
        url = "https://api.groq.com/openai/v1/chat/completions"
        payload = json.dumps({
            "model": model,
            "messages": [{"role": "user", "content": str(prompt)}]
        }).encode("utf-8")
        req = urllib.request.Request(url, data=payload, headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        })
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data["choices"][0]["message"]["content"]
        except Exception as e:
            return f"[Aira Groq Error]: {e}"

    def chat(messages, model="gemini-2.5-flash", key=None):
        api_key = key or state["gemini_key"]
        if not api_key and state["groq_key"]:
            url = "https://api.groq.com/openai/v1/chat/completions"
            payload = json.dumps({"model": "llama-3.3-70b-versatile", "messages": messages}).encode("utf-8")
            req = urllib.request.Request(url, data=payload, headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {state['groq_key']}"
            })
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))["choices"][0]["message"]["content"]
        last_msg = messages[-1]["content"] if isinstance(messages, list) and messages else str(messages)
        return ask(last_msg, model=model, key=api_key)

    def summarize(text, max_words=100):
        prompt = f"Summarize the following text concisely in under {max_words} words:\n\n{text}"
        return ask(prompt)

    return AiraModule("ai", {
        "ask": ask,
        "chat": chat,
        "groq": groq,
        "summarize": summarize,
        "set_key": set_key,
        "get_key": get_key,
    })

def create_sec_module():
    COMMON_SERVICES = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
        80: "HTTP", 110: "POP3", 111: "RPCBind", 135: "RPC", 139: "NetBIOS",
        143: "IMAP", 443: "HTTPS", 445: "SMB", 993: "IMAPS", 995: "POP3S",
        1433: "MSSQL", 1521: "Oracle", 3306: "MySQL", 3389: "RDP",
        5432: "PostgreSQL", 5900: "VNC", 6379: "Redis", 8000: "HTTP-Alt",
        8080: "HTTP-Proxy", 8443: "HTTPS-Alt", 8888: "HTTP-Alt", 9000: "SonarQube",
        27017: "MongoDB"
    }

    def scan_port(host, port, timeout=1.0):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(float(timeout))
            res = s.connect_ex((str(host), int(port)))
            s.close()
            return res == 0
        except Exception:
            return False

    def scan_ports(host, ports=None, threads=15, timeout=1.0):
        if ports is None:
            ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 1433, 1521, 3306, 3389, 5432, 6379, 8000, 8080, 8443, 8888]
        elif isinstance(ports, range):
            ports = list(ports)
        elif not isinstance(ports, list):
            ports = [int(ports)]

        open_ports = []
        def _check(p):
            if scan_port(host, p, timeout=timeout):
                svc = COMMON_SERVICES.get(p, "Unknown")
                return {"port": p, "service": svc, "state": "open"}
            return None

        with ThreadPoolExecutor(max_workers=int(threads)) as executor:
            results = executor.map(_check, ports)
            for r in results:
                if r is not None:
                    open_ports.append(r)
        return open_ports

    def banner(host, port, timeout=2.0):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(float(timeout))
            s.connect((str(host), int(port)))
            if int(port) in (80, 8080, 8000, 8888):
                s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
            else:
                s.sendall(b"\r\n")
            data = s.recv(1024).decode('utf-8', errors='ignore').strip()
            s.close()
            return data
        except Exception as e:
            return f"Error: {e}"

    def audit_headers(url):
        if not str(url).startswith("http://") and not str(url).startswith("https://"):
            url = "https://" + str(url)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "AiraLang-SecEngine/1.4.0"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                headers = dict(resp.headers)

            important_headers = [
                "Strict-Transport-Security",
                "Content-Security-Policy",
                "X-Frame-Options",
                "X-Content-Type-Options",
                "Referrer-Policy",
                "Permissions-Policy"
            ]

            present = []
            missing = []
            header_keys_lower = {k.lower(): k for k in headers.keys()}

            for h in important_headers:
                if h.lower() in header_keys_lower:
                    present.append(h)
                else:
                    missing.append(h)

            score_ratio = len(present) / len(important_headers)
            if score_ratio >= 0.8: grade = "A"
            elif score_ratio >= 0.6: grade = "B"
            elif score_ratio >= 0.4: grade = "C"
            elif score_ratio >= 0.2: grade = "D"
            else: grade = "F"

            return {
                "url": url,
                "grade": grade,
                "present": present,
                "missing": missing,
                "server": headers.get("Server", headers.get("server", "Hidden/Unknown")),
                "headers": headers
            }
        except Exception as e:
            return {"url": url, "error": str(e)}

    def subdomains(domain, timeout=8.0):
        try:
            clean_dom = str(domain).replace("https://", "").replace("http://", "").split("/")[0]
            url = f"https://crt.sh/?q=%.{urllib.parse.quote(clean_dom)}&output=json"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=float(timeout)) as resp:
                data = json.loads(resp.read().decode('utf-8'))
            subs = set()
            for entry in data:
                name_val = entry.get("name_value", "")
                for sub in name_val.split("\n"):
                    sub = sub.strip().lower()
                    if sub and "*" not in sub:
                        subs.add(sub)
            return sorted(list(subs))
        except Exception as e:
            return [f"Error fetching subdomains: {e}"]

    def hash_identify(hash_str):
        h = str(hash_str).strip()
        l = len(h)
        is_hex = all(c in "0123456789abcdefABCDEF" for c in h)

        if h.startswith("$2a$") or h.startswith("$2b$") or h.startswith("$2y$"):
            return "Bcrypt"
        if h.startswith("$6$"):
            return "SHA-512 Crypt"
        if h.startswith("$1$"):
            return "MD5 Crypt"

        if is_hex:
            if l == 32: return "MD5 / NTLM"
            elif l == 40: return "SHA-1"
            elif l == 56: return "SHA-224"
            elif l == 64: return "SHA-256"
            elif l == 96: return "SHA-384"
            elif l == 128: return "SHA-512"

        return "Unknown Hash Format"

    def crack_md5(target_hash, wordlist):
        target = str(target_hash).lower().strip()
        words = []
        if isinstance(wordlist, list):
            words = wordlist
        elif isinstance(wordlist, str):
            if os.path.exists(wordlist):
                with open(wordlist, "r", encoding="utf-8", errors="ignore") as f:
                    words = [line.strip() for line in f]
            else:
                words = [wordlist]

        for w in words:
            if hashlib.md5(w.encode('utf-8')).hexdigest() == target:
                return w
        return None

    def resolve(host):
        try:
            return socket.gethostbyname(str(host))
        except Exception as e:
            return str(e)

    def reverse_dns(ip):
        try:
            return socket.gethostbyaddr(str(ip))[0]
        except Exception as e:
            return str(e)

    return AiraModule("sec", {
        "scan_port": scan_port,
        "scan_ports": scan_ports,
        "scan": scan_ports,
        "banner": banner,
        "audit_headers": audit_headers,
        "subdomains": subdomains,
        "hash_identify": hash_identify,
        "crack_md5": crack_md5,
        "resolve": resolve,
        "reverse_dns": reverse_dns
    })

def create_thread_module():
    def spawn(fn, args=None):
        if args is None:
            args = []
        elif not isinstance(args, (list, tuple)):
            args = [args]

        def _runner():
            if callable(fn):
                fn(*args)

        t = threading.Thread(target=_runner, daemon=True)
        t.start()
        return t

    def join(t, timeout=None):
        if hasattr(t, "join"):
            t.join(timeout=float(timeout) if timeout is not None else None)
            return True
        return False

    def sleep(seconds):
        time.sleep(float(seconds))
        return True

    def pool(fn, items, max_workers=5):
        if not isinstance(items, (list, tuple)):
            items = list(items)

        def _worker(item):
            if callable(fn):
                return fn(item)
            return None

        with ThreadPoolExecutor(max_workers=int(max_workers)) as executor:
            return list(executor.map(_worker, items))

    return AiraModule("thread", {
        "spawn": spawn,
        "start": spawn,
        "join": join,
        "sleep": sleep,
        "pool": pool
    })

BUILTIN_MODULES = {
    "file": create_file_module,
    "os": create_os_module,
    "math": create_math_module,
    "time": create_time_module,
    "json": create_json_module,
    "http": create_http_module,
    "crypto": create_crypto_module,
    "string": create_string_module,
    "sqlite": create_sqlite_module,
    "net": create_net_module,
    "ai": create_ai_module,
    "sec": create_sec_module,
    "thread": create_thread_module
}

