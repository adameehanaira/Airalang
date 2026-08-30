# 🌟 AiraLang (v1.2.0 Next-Gen Engine)
> **The High-Performance, Lightweight & Expressive Programming Language for Creators & Developers**  
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

### 2. For..In Loops & Range
```aira
let tools = ["Termux", "AiraLang", "CyberGuard"];
for tool in tools {
    say "Tool: " + tool;
}

# Looping using range(start, end)
for i in range(1, 6) {
    if (i == 3) {
        continue; # skip 3
    }
    say "Count: " + i;
}
```

### 3. Object-Oriented Programming (OOP)
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

### 4. Exception Handling (Try / Catch / Throw)
```aira
try {
    throw "Security Access Denied";
} catch (err) {
    say "Caught Exception: " + err;
}
```

### 5. Native String & List Methods
```aira
let text = "  aira technology  ";
say text.trim().upper(); # "AIRA TECHNOLOGY"

let langs = ["C++", "Python"];
langs.push("AiraLang");
say langs.join(" -> "); # "C++ -> Python -> AiraLang"
```

### 6. Standard Library Modules
```aira
# Network / HTTP
import "http";
let res = http.get("https://httpbin.org/get");

# Cryptography & Hashing
import "crypto";
let hash = crypto.sha256("admin123");
let b64 = crypto.b64encode("secret");

# System & OS
import "os";
let out = os.cmd("uname -a");

# Math & Time & JSON
import "math";
import "time";
import "json";
```

---

## 📜 License
MIT Open Source License © 2026 Adam Eehan (Aira Group of Technology).
