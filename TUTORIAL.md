# 📘 AiraLang: Complete Zero-to-Hero Mastery Handbook
> **The Official Learning Guide for Adam Eehan & Aira Developers** 👑  
> **Language:** AiraLang (v1.4.0 Aira Cyber & AI Edition)  
> **Author & Architect:** Adam Eehan (Founder & CEO, Aira Group of Technology)  
> **Co-Pilot:** Aira (Engine v3.6)

---

## 📑 Table of Contents
1. [Introduction & Terminal Setup](#1-introduction--terminal-setup)
2. [Level 1: The Basics (Syntax, Variables, Operators)](#2-level-1-the-basics)
3. [Level 2: Control Flow (Conditions & Loops)](#3-level-2-control-flow)
4. [Level 3: Data Structures (Lists, Dictionaries, Strings)](#4-level-3-data-structures)
5. [Level 4: Modular Code (Functions & OOP)](#5-level-4-modular-code)
6. [Level 5: Functional Programming (v1.4.0)](#6-level-5-functional-programming)
7. [Level 6: Concurrency & Multi-Threading (`thread`)](#7-level-6-concurrency--multi-threading)
8. [Level 7: Cyber Security & Recon Engine (`sec`)](#8-level-7-cyber-security--recon-engine)
9. [Level 8: Native AI Engine (`ai`)](#9-level-8-native-ai-engine)
10. [Level 9: Built-in Systems Modules (File, OS, SQLite, Crypto, Net)](#10-level-9-built-in-systems-modules)
11. [Level 10: CLI Mastery & Binary Compiler (`build`, `new`)](#11-level-10-cli-mastery--binary-compiler)

---

## 1. Introduction & Terminal Setup

AiraLang runs directly inside Termux or any Linux terminal.

### Quick Commands:
* **Start Live REPL Shell:**
  ```bash
  airalang
  ```
* **Run any script:**
  ```bash
  airalang script.aira
  ```
* **Create a new project scaffold:**
  ```bash
  airalang new my_project
  ```
* **Compile script to direct executable binary:**
  ```bash
  airalang build script.aira -o my_tool
  ./my_tool
  ```

---

## 2. Level 1: The Basics

### A. Output (`say` / `print`)
```aira
say "Hello Boss, Welcome to AiraLang!";
print("Print also works identically!");
say "Item 1", "Item 2", 100;
```

### B. Variables (`let`)
Variables are dynamically typed:
```aira
let name = "Adam Eehan";      # String
let age = 20;                 # Number (Integer)
let score = 98.5;             # Number (Float)
let is_active = true;         # Boolean (true / false)
let empty_data = null;        # Null

say "Founder: " + name;
```

### C. Operators & Shorthands
```aira
let a = 10;
let b = 3;

say a + b;   # 13 (Addition)
say a - b;   # 7  (Subtraction)
say a * b;   # 30 (Multiplication)
say a / b;   # 3.333 (Division)
say a % b;   # 1  (Modulo / Remainder)

# Shorthand Operators (v1.3.0+)
let counter = 10;
counter += 5; # 15
counter -= 2; # 13
counter *= 2; # 26
counter /= 2; # 13
```

### D. User Input (`input`)
```aira
let user_name = input("Enter your name: ");
say "Welcome, " + user_name + "!";
```

---

## 3. Level 2: Control Flow

### A. Conditions (`if`, `else if`, `else`)
```aira
let marks = 85;

if (marks >= 90) {
    say "Grade: S Rank (Master)";
} else if (marks >= 80) {
    say "Grade: A Rank (Pro)";
} else if (marks >= 50) {
    say "Grade: B Rank";
} else {
    say "Grade: Needs Improvement";
}
```

### B. Logical Operators (`and`, `or`, `not`)
```aira
let is_admin = true;
let has_token = true;

if (is_admin and has_token) {
    say "Full System Access Granted!";
}

if (not is_admin) {
    say "Standard User";
}
```

### C. Loops

#### 1. `while` Loop
```aira
let i = 1;
while (i <= 5) {
    say "Step: " + i;
    i += 1;
}
```

#### 2. `for..in` Loop with Lists
```aira
let tools = ["Termux", "AiraLang", "CyberGuard"];
for t in tools {
    say "Active Tool: " + t;
}
```

#### 3. `for..in` with `range(start, stop, step)`
```aira
for n in range(1, 6) {
    if (n == 3) {
        continue; # Skip number 3
    }
    if (n == 5) {
        break;    # Stop loop at 5
    }
    say "Number: " + n;
}
```

---

## 4. Level 3: Data Structures

### A. Lists (Arrays)
```aira
let fruits = ["Apple", "Mango", "Banana"];

# Built-in Methods
fruits.push("Orange");       # Add to end
say fruits.length;           # 4
say fruits.contains("Mango");# true
say fruits.join(" -> ");     # "Apple -> Mango -> Banana -> Orange"

let popped = fruits.pop();   # Removes last item
fruits.reverse();            # Reverses list in-place
let sub = fruits.slice(0, 2);# Slices index 0 to 2
```

### B. Dictionaries (Maps / Objects)
```aira
let user = {
    "name": "Adam",
    "role": "CEO",
    "power": 9999
};

# Accessing
say user["name"];            # "Adam"
say user.role;               # "CEO"

# Dictionary Methods
say user.get("role");        # "CEO"
say user.get("location", "Kerala"); # Default fallback
say user.keys();             # ["name", "role", "power"]
say user.values();           # ["Adam", "CEO", 9999]
say user.items();            # [["name", "Adam"], ...]
say user.has("power");       # true
```

### C. String Enhancements
```aira
let text = "aira cyber security";

say text.upper();            # "AIRA CYBER SECURITY"
say text.lower();            # "aira cyber security"
say text.title();            # "Aira Cyber Security"
say text.reverse();          # "ytiruces rebyc aria"
say text.replace("cyber", "guard"); # "aira guard security"
say text.split(" ");         # ["aira", "cyber", "security"]
```

---

## 5. Level 4: Modular Code (Functions & OOP)

### A. Functions (`fn`)
```aira
fn calculate_tax(amount, rate) {
    let tax = amount * (rate / 100);
    return amount + tax;
}

let total = calculate_tax(1000, 18);
say "Total with 18% Tax: " + total;
```

### B. Object-Oriented Programming (`class`, `new`, `this`)
```aira
class Developer {
    fn init(name, language) {
        this.name = name;
        this.language = language;
    }

    fn introduce() {
        return "Dev: " + this.name + " | Primary Lang: " + this.language;
    }
}

let dev1 = new Developer("Adam", "AiraLang");
say dev1.introduce();
```

### C. Exception Handling (`try`, `catch`, `throw`)
```aira
try {
    let x = 10;
    throw "Unauthorized Action!";
} catch (err) {
    say "Caught Exception Safely: " + err;
}
```

---

## 6. Level 5: Functional Programming (v1.4.0)

AiraLang supports First-Class Anonymous Functions:
```aira
let numbers = [1, 2, 3, 4, 5, 6, 7, 8];

# 1. .filter(fn) - Filter items matching condition
let evens = numbers.filter(fn(x) { 
    return x % 2 == 0; 
});
say evens; # [2, 4, 6, 8]

# 2. .map(fn) - Transform each element
let doubled = evens.map(fn(x) { 
    return x * 10; 
});
say doubled; # [20, 40, 60, 80]

# 3. .find(fn) - Find first element matching predicate
let match = numbers.find(fn(x) { 
    return x > 5; 
});
say match; # 6

# 4. .reduce(fn, initial) - Combine list into a single value
let sum = numbers.reduce(fn(accum, val) { 
    return accum + val; 
}, 0);
say sum; # 36

# 5. .sort(reverse=false)
let unsorted = [5, 1, 9, 3];
say unsorted.sort();        # [1, 3, 5, 9]
say unsorted.sort(true);    # [9, 5, 3, 1]
```

---

## 7. Level 6: Concurrency & Multi-Threading (`thread`)

### A. Spawn Background Thread
```aira
import "thread";

thread.spawn(fn() {
    say "Worker starting background task...";
    thread.sleep(1.0);
    say "Worker finished!";
});

say "Main thread continues running without blocking!";
```

### B. High-Speed Parallel Thread Pool
Run functions across items simultaneously using multi-core threads:
```aira
import "thread";

let urls = ["api1", "api2", "api3", "api4"];
let results = thread.pool(fn(endpoint) {
    return "Fetched " + endpoint;
}, urls, 4);

say results;
```

---

## 8. Level 7: Cyber Security & Recon Engine (`sec`)

Built natively for ethical hacking and defensive security:
```aira
import "sec";

# 1. Multi-Threaded Port Scanner
let ports = sec.scan_ports("google.com", [21, 22, 80, 443, 8080], 10);
say "Scan Results: ", ports;

# 2. HTTP Security Header Audit (Checks CSP, HSTS, X-Frame-Options)
let report = sec.audit_headers("https://example.com");
say "Security Grade: " + report["grade"];
say "Missing Headers: ", report["missing"];

# 3. Live Subdomain Enumeration (via Certificate Logs)
let subdomains = sec.subdomains("example.com");
say "Found Subdomains: ", subdomains;

# 4. Hash Identification & Dictionary Cracker
say "Hash Type: " + sec.hash_identify("098f6bcd4621d373cade4e832627b4f6");
let cleartext = sec.crack_md5("098f6bcd4621d373cade4e832627b4f6", ["admin", "test", "root"]);
say "Cracked Password: " + cleartext;

# 5. IP & DNS Resolution
say "IP of google.com: " + sec.resolve("google.com");
```

---

## 9. Level 8: Native AI Engine (`ai`)

AiraLang is an **AI-Native Language** supporting Gemini & Groq:

### Setting Up API Key (BYOK Model):
In Termux terminal:
```bash
export GEMINI_API_KEY="your_api_key_here"
```

### In AiraLang Code:
```aira
import "ai";

# Simple 1-Line AI Query
let reply = ai.ask("Explain Zero Trust Architecture");
say reply;

# Setting key in code (if not in environment)
ai.set_key("YOUR_API_KEY", "gemini");
# or for Groq:
ai.set_key("YOUR_GROQ_KEY", "groq");

# Summarizing long content
let text = "Very long vulnerability report...";
say ai.summarize(text, 50); # summary under 50 words
```

---

## 10. Level 9: Built-in Systems Modules

### A. SQLite Database (`sqlite`)
```aira
import "sqlite";

let db = sqlite.open("app.db");
db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT);");
db.insert("users", {"name": "Adam Boss"});

let rows = db.query("SELECT * FROM users;");
say rows;
db.close();
```

### B. Cryptography (`crypto`)
```aira
import "crypto";

say "SHA-256: " + crypto.sha256("admin123");
say "MD5:     " + crypto.md5("admin123");
say "Base64:  " + crypto.b64encode("secret");
```

### C. File System & OS (`file`, `os`)
```aira
import "file";
import "os";

file.write("notes.txt", "AiraLang Rocks!");
say file.read("notes.txt");
say "Current Dir: " + os.cwd();
say "Uname: " + os.cmd("uname -a");
```

---

## 11. Level 10: CLI Mastery & Binary Compiler

### A. Creating a Standalone Executable Binary
No need for users to have `airalang` CLI in their mind. You can compile your scripts into standalone tools:
```bash
airalang build my_scanner.aira -o my_scanner
chmod +x my_scanner
./my_scanner
```

### B. Starting a New Project
```bash
airalang new cyber_recon_tool
cd cyber_recon_tool
airalang main.aira
```

---
👑 **AiraLang © 2026 Adam Eehan — Aira Group of Technology**  
*Built for the next generation of cybersecurity researchers and AI engineers.*
