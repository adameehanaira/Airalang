# 🌟 AiraLang (v1.4.0 Aira Cyber & AI Edition)
> **The High-Performance, Expressive & Modular Scripting Language for Creators, AI & Cybersecurity Engineers**  
> **Author & Creator:** Adam Eehan (Founder & CEO, Aira Group of Technology) 👑

---

## ⚡ Introduction
`AiraLang` is an open-source, dynamic, and expressive scripting language engineered from scratch with a focus on simplicity, developer freedom, high speed, native AI integrations, and advanced systems/cybersecurity capabilities.

---

## 🚀 Quick Start in Termux / Linux

### 1. Interactive REPL Shell
```bash
airalang
```

### 2. Run an AiraLang Script
```bash
airalang script.aira
# or: airalang run script.aira
```

### 3. Compile Script to Standalone Executable Binary
```bash
airalang build script.aira -o my_tool
./my_tool
```

### 4. Create New Project Scaffold
```bash
airalang new my_cyber_project
cd my_cyber_project && airalang main.aira
```

---

## 💻 Syntax & Features Guide

### 1. Variables & Output
```aira
say "Hello, World!";
let name = "Adam Boss";
let power = 100;
say "Creator: " + name;
```

### 2. Shorthand Operators (`+=`, `-=`, `*=`, `/=`)
```aira
let count = 10;
count += 5; # count is now 15
count *= 2; # count is now 30
count -= 10; # count is now 20
```

### 3. Conditionals (`if`, `else if`, `else`)
```aira
let marks = 85;

if (marks >= 90) {
    say "Grade: S (Master)";
} else if (marks >= 80) {
    say "Grade: A (Pro)";
} else if (marks >= 50) {
    say "Grade: B";
} else {
    say "Grade: Pass";
}
```

### 4. For..In Loops & Range
```aira
let tools = ["Termux", "AiraLang", "CyberGuard"];
for tool in tools {
    say "Tool: " + tool;
}

# Looping through numbers using range(start, end)
for i in range(1, 6) {
    if (i == 3) {
        continue; # skip 3
    }
    say "Count: " + i;
}
```

### 5. Functions & Return Values (`fn`)
```aira
fn calculate_power(base, multiplier) {
    return base * multiplier;
}

let result = calculate_power(50, 2);
say "Total Power: " + result;
```

### 6. Object-Oriented Programming (OOP)
```aira
class Agent {
    fn init(name, role) {
        this.name = name;
        this.role = role;
    }

    fn introduce() {
        return "Agent: " + this.name + " (" + this.role + ")";
    }
}

let adam = new Agent("Adam Eehan", "CEO");
say adam.introduce();
```

### 7. Exception Handling (Try / Catch / Throw)
```aira
try {
    throw "Security Access Denied";
} catch (err) {
    say "Caught Exception: " + err;
}
```

### 8. Native String & List Methods
```aira
let text = "  aira technology  ";
say text.trim().upper(); # "AIRA TECHNOLOGY"

let langs = ["C++", "Python"];
langs.push("AiraLang");
say langs.join(" -> "); # "C++ -> Python -> AiraLang"
```

### 9. Built-in Utilities
```aira
let numbers = [10, 50, 5, 90, 25];
say "Max: " + max(numbers);
say "Min: " + min(numbers);
say "Sum: " + sum(numbers);
say "Abs: " + abs(-42);
```

### 10. Functional Programming & Anonymous Functions
First-class functions can be created anonymously (`fn(...) { ... }`) and passed into higher-order methods:
```aira
let nums = [1, 2, 3, 4, 5, 6];

# Filter even numbers
let evens = nums.filter(fn(x) { return x % 2 == 0; }); # [2, 4, 6]

# Map over items
let doubled = evens.map(fn(x) { return x * 2; }); # [4, 8, 12]

# Find specific item
let target = nums.find(fn(x) { return x > 4; }); # 5

# Reduce list to a single value
let sum = nums.reduce(fn(acc, val) { return acc + val; }, 0); # 21
```

---

## 📦 Standard Library Modules
> 📚 **Detailed Documentation:** For complete syntax, parameters, and examples for all 14 built-in modules, visit the [**Modules Catalog (`modules/`)**](./modules/README.md).

### 🤖 Universal AI Integration Engine (`ai`)
Directly integrate Generative AI from ANY provider in the world natively in AiraLang (OpenAI, DeepSeek, Anthropic Claude, Google Gemini, Groq, OpenRouter, Mistral, Ollama, Perplexity, Cerebras, or custom servers):
```aira
import "ai";

# 1. Automatic Key Prefix Detection (Groq, OpenRouter, Claude, Cerebras, Gemini, etc.)
ai.set_key("gsk_YOUR_GROQ_KEY");
say ai.ask("Explain cyber security defensive postures");

# 2. Explicit Provider Selection (DeepSeek, OpenAI, Mistral, etc.)
ai.set_provider("deepseek", "sk-YOUR_DEEPSEEK_KEY");
say ai.ask("Optimize this sorting algorithm");

# 3. 100% Offline Local AI with Ollama (Termux / PC)
ai.set_provider("ollama", model="llama3.2");
say ai.ask("Local offline AI query");

# 4. Custom Enterprise Server (vLLM, LM Studio, Localhost)
ai.set_endpoint("http://localhost:8000/v1/chat/completions", "token", "my-model");
```

### 💖 Cyber-Romance & Proposal Engine (`proposal`)
Interactive proposal prank module with automated HTTP 500 server love timeout loop and Lover Accept Checker AI:
```aira
import "proposal";
import "ai";

ai.set_key("gsk_YOUR_GROQ_KEY");

# Loops automatically until the target accepts, celebrating with couple wishes!
proposal.ask("Do You Love Me : ");
say "mee too 🩷";
```

### 🛡️ Cyber Security & Reconnaissance Engine (`sec`)
Engineered natively for ethical hackers, security researchers, and cyber defense:
```aira
import "sec";

# Multi-Threaded Port Scanner
let open_ports = sec.scan_ports("google.com", [80, 443, 8080], 10);
say "Open Ports: ", open_ports;

# HTTP Security Header Audit (checks CSP, HSTS, X-Frame-Options)
let audit = sec.audit_headers("https://example.com");
say "Security Grade: " + audit["grade"];
say "Missing Headers: ", audit["missing"];

# Subdomain Enumeration via Certificate Transparency
let subdomains = sec.subdomains("example.com");
say "Discovered Subdomains: ", subdomains;

# Hash Identification & Cracking
say "Hash Type: " + sec.hash_identify("098f6bcd4621d373cade4e832627b4f6");
let plain = sec.crack_md5("098f6bcd4621d373cade4e832627b4f6", ["admin", "test", "root"]);
say "Cracked Plaintext: " + plain;
```

### 🧵 Multi-Threading & Concurrency (`thread`)
Run parallel workloads, concurrent network sweeps, or background jobs:
```aira
import "thread";

# Background thread execution
thread.spawn(fn() {
    say "Worker running concurrently in background!";
});

# High-speed parallel pool map
let results = thread.pool(fn(x) {
    return x * 10;
}, [1, 2, 3, 4, 5], 4);
say "Parallel results: ", results; # [10, 20, 30, 40, 50]
```

### 🗄️ SQLite Database Module (`sqlite`)
```aira
import "sqlite";

let db = sqlite.open("data.db");
db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, role TEXT);");
db.insert("users", {"name": "Adam Eehan", "role": "Founder & CEO"});

let rows = db.query("SELECT * FROM users;");
for row in rows {
    say "User: " + row["name"] + " | Role: " + row["role"];
}
db.close();
```

### 🔌 Networking & Sockets Module (`net`)
```aira
import "net";

say "Local Machine IP: " + net.local_ip();
say "Resolved IP: " + net.resolve("google.com");

# Port Scanner
let is_open = net.scan_port("google.com", 443);
say "Port 443 is open: " + is_open;
```

### 🔐 Cryptography & Hashing (`crypto`)
```aira
import "crypto";

let hash = crypto.sha256("admin123");
let b64 = crypto.b64encode("secret_token");
say "SHA-256: " + hash;
say "Base64: " + b64;
say "Decoded: " + crypto.b64decode(b64);
```

### 🌐 HTTP Client (`http`)
```aira
import "http";

let res = http.get("https://httpbin.org/get");
say res;
```

### 📂 OS, File, Math, Time & JSON
```aira
import "os";
import "file";
import "math";
import "time";
import "json";

say "OS Kernel: " + os.cmd("uname -o");
say "Sqrt: " + math.sqrt(144);
say "Current Time: " + time.now();
```

### 🧩 Custom `.aira` File Imports
```aira
# Import functions from another file (e.g., utils.aira)
import "utils.aira";
let output = utils.my_custom_function();
```

---

## 📜 License
MIT Open Source License © 2026 Adam Eehan (Aira Group of Technology).
