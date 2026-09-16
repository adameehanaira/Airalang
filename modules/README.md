# 📦 AiraLang Standard Library Modules Directory
> **Official Module Catalog for AiraLang (v1.4.1 Aira Cyber & AI Edition)**  
> **Author & Creator:** Adam Eehan (Founder & CEO, Aira Group of Technology) 👑

---

## 🌟 Overview
AiraLang features 15 built-in standard library modules engineered natively for speed, AI capabilities, cyber security recon, system operations, and developer joy.

All modules are loaded natively via the `import` statement:
```aira
import "<module_name>";
```

---

## 📋 Complete Modules Catalog

| # | Module | Category | Primary Purpose | Key Methods |
|---|---|---|---|---|
| 1 | [`ai`](./ai.md) | Artificial Intelligence | Universal LLM engine (OpenAI, DeepSeek, Claude, Gemini, Groq, Ollama, OpenRouter, etc.) | `ask()`, `set_provider()`, `set_endpoint()`, `set_key()`, `providers()` |
| 2 | [`android`](./android.md) / `droidsec` | Mobile Security & Recon | Android device integrity audit, root detection, and static APK security analyzer | `device_info()`, `audit_device()`, `audit_apk()`, `audit_package()`, `check_root()` |
| 3 | [`sec`](./sec.md) | Cybersecurity | Port scanning, header auditing, subdomain discovery | `scan_ports()`, `audit_headers()`, `subdomains()`, `crack_md5()` |
| 4 | [`proposal`](./proposal.md) | Fun & Cyber-Prank | Automated HTTP 500 love timeout & AI sentiment checker | `ask()`, `set_key()`, `set_system()`, `wish()`, `set_wish()` |
| 5 | [`http`](./http.md) | Networking | Web requests, REST APIs, and file downloads | `get()`, `post()`, `download()`, `status()` |
| 6 | [`file`](./file.md) | System I/O | Read, write, append, and inspect local files | `read()`, `write()`, `append()`, `exists()`, `delete()` |
| 7 | [`os`](./os.md) | System | Shell commands, environment variables, directories | `cmd()`, `env()`, `cwd()`, `listdir()`, `mkdir()`, `platform()` |
| 8 | [`math`](./math.md) | Mathematics | Math functions, trigonometry, and constants | `sqrt()`, `pow()`, `abs()`, `random()`, `round()`, `pi`, `e` |
| 9 | [`time`](./time.md) | System | Epoch time, timestamps, and execution delays | `now()`, `time()`, `sleep()` |
| 10 | [`json`](./json.md) | Data | Parsing and serialization of JSON payloads | `parse()`, `stringify()`, `mkstring()` |
| 11 | [`crypto`](./crypto.md) | Security | Cryptographic hashes and encoding utilities | `md5()`, `sha256()`, `sha1()`, `base64_encode()`, `base64_decode()` |
| 12 | [`string`](./string.md) | Utilities | Advanced text manipulation and transformation | `split()`, `replace()`, `upper()`, `lower()`, `trim()`, `join()` |
| 13 | [`sqlite`](./sqlite.md) | Database | Lightweight embedded SQL relational database | `open()`, `query()`, `execute()`, `close()` |
| 14 | [`net`](./net.md) | Networking | Host pings, TCP port checks, and IP discovery | `ping()`, `port_open()`, `local_ip()`, `fetch()` |
| 15 | [`thread`](./thread.md) | Concurrency | Thread spawning, worker pools, and parallel execution | `spawn()`, `join()`, `pool()`, `sleep()` |

---
*Maintained by the AiraLang Core Engineering Team. Created by Adam Eehan.*
