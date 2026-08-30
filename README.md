# 🌟 AiraLang (v1.3.0 Pro Edition)
> **The High-Performance, Expressive & Modular Scripting Language for Creators & Developers**  
> **Author & Creator:** Adam Eehan (Founder & CEO, Aira Group of Technology) 👑

---

## ⚡ Introduction
`AiraLang` is an open-source, dynamic, and expressive scripting language engineered from scratch with a focus on simplicity, developer freedom, high speed, and native systems/cybersecurity capabilities.

---

## 🚀 Quick Start in Termux / Linux

### 1. Interactive REPL Shell
Launch the live interactive REPL anytime by typing:
```bash
airalang
```

### 2. Run an AiraLang Script
```bash
airalang script.aira
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

---

## 📦 Standard Library Modules

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
