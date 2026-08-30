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
    "net": create_net_module
}
