#!/data/data/com.termux/files/usr/bin/python3
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lexer import Lexer
from parser import Parser
from evaluator import Evaluator

VERSION = "1.4.0 (Aira Cyber & AI Edition)"
AUTHOR = "Adam Eehan (Aira Group of Technology)"

ASCII_BANNER = f"""\033[1;36m
    ___    _           __                    
   /   |  (_)________ _/ /   ____ _____  ____ _
  / /| | / / ___/ __ `/ /   / __ `/ __ \\/ __ `/
 / ___ |/ / /  / /_/ / /___/ /_/ / / / / /_/ / 
/_/  |_/_/_/   \\__,_/_____/\\__,_/_/ /_/\\__, /  
                                      /____/   
\033[0m\033[1;30m---------------------------------------------------\033[0m
 \033[1;32m[+]\033[0m \033[1;37mEngine:\033[0m AiraLang v{VERSION}
 \033[1;34m[*]\033[0m \033[1;37mCreator:\033[0m {AUTHOR}
 \033[1;35m[⚡]\033[0m \033[1;37mModules:\033[0m ai, sec, thread, sqlite, net, crypto
 \033[1;33m[!]\033[0m Multiline support: open \033[1;32m{{\033[0m will continue on next line.
 \033[1;33m[!]\033[0m Type \033[1;31m'exit'\033[0m or \033[1;31m'quit'\033[0m to close REPL.
\033[1;30m---------------------------------------------------\033[0m
"""

def is_balanced(code):
    in_single_quote = False
    in_double_quote = False
    in_comment = False
    
    braces = 0
    parens = 0
    brackets = 0
    
    i = 0
    while i < len(code):
        c = code[i]
        
        if in_comment:
            if c == '\n':
                in_comment = False
            i += 1
            continue
            
        if c == '#' and not in_single_quote and not in_double_quote:
            in_comment = True
            i += 1
            continue
            
        if c == '"' and not in_single_quote:
            if i > 0 and code[i-1] == '\\':
                pass
            else:
                in_double_quote = not in_double_quote
            i += 1
            continue
            
        if c == "'" and not in_double_quote:
            if i > 0 and code[i-1] == '\\':
                pass
            else:
                in_single_quote = not in_single_quote
            i += 1
            continue
            
        if not in_single_quote and not in_double_quote:
            if c == '{': braces += 1
            elif c == '}': braces -= 1
            elif c == '(': parens += 1
            elif c == ')': parens -= 1
            elif c == '[': brackets += 1
            elif c == ']': brackets -= 1
            
        i += 1
        
    return (braces <= 0 and parens <= 0 and brackets <= 0 and not in_single_quote and not in_double_quote)

def run_code(source_code, evaluator=None):
    if evaluator is None:
        evaluator = Evaluator()
    try:
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        return evaluator.eval(ast)
    except SyntaxError as e:
        print(f"\033[1;31m[!] SyntaxError:\033[0m {e}")
    except NameError as e:
        print(f"\033[1;31m[!] NameError:\033[0m {e}")
    except TypeError as e:
        print(f"\033[1;31m[!] TypeError:\033[0m {e}")
    except Exception as e:
        print(f"\033[1;31m[!] Error:\033[0m {e}")

def run_file(filepath):
    if not os.path.exists(filepath):
        print(f"\033[1;31m[!] Error: File '{filepath}' not found.\033[0m")
        sys.exit(1)
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()
    run_code(code)

def start_repl():
    print(ASCII_BANNER)
    evaluator = Evaluator()
    buffer = []
    
    while True:
        try:
            if not buffer:
                prompt = "\033[1;35m[aira]\033[0m \033[1;32m❯❯\033[0m "
            else:
                prompt = "\033[1;33m[....]\033[0m \033[1;32m··\033[0m "
                
            line = input(prompt)
            
            if not buffer and line.strip() in ("exit", "quit"):
                print("\033[1;33m[*] Exiting AiraLang. Goodbye, Boss!\033[0m")
                break
                
            if not buffer and line.strip() == "clear":
                os.system("clear")
                continue
                
            if not line.strip() and not buffer:
                continue

            buffer.append(line)
            full_code = "\n".join(buffer)
            
            if is_balanced(full_code) or (len(buffer) > 1 and not line.strip()):
                run_code(full_code, evaluator)
                buffer = []
                
        except (KeyboardInterrupt, EOFError):
            if buffer:
                print("\n\033[1;33m[*] Discarded incomplete block.\033[0m")
                buffer = []
            else:
                print("\n\033[1;33m[*] Interrupted. Exiting AiraLang...\033[0m")
                break

def build_file(source_path, output_path=None):
    if not os.path.exists(source_path):
        print(f"\033[1;31m[!] Error: File '{source_path}' not found.\033[0m")
        sys.exit(1)
    if output_path is None:
        output_path = os.path.splitext(source_path)[0]
    with open(source_path, "r", encoding="utf-8") as f:
        aira_code = f.read()

    runner_script = f"""#!/data/data/com.termux/files/usr/bin/python3
# ==========================================
# Standalone Binary Executable
# Generated by AiraLang v{VERSION}
# Author: {AUTHOR}
# ==========================================
import sys, os
AIRA_SRC = "/data/data/com.termux/files/home/airalang/src"
if AIRA_SRC not in sys.path:
    sys.path.insert(0, AIRA_SRC)
from cli import run_code
CODE = {repr(aira_code)}
if __name__ == '__main__':
    run_code(CODE)
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(runner_script)
    os.chmod(output_path, 0o755)
    print(f"\033[1;32m[+] Successfully built executable binary:\033[0m {output_path}")
    print(f"\033[1;34m[*] Run it directly:\033[0m ./{output_path}")

def new_project(proj_name):
    if os.path.exists(proj_name):
        print(f"\033[1;31m[!] Error: Directory '{proj_name}' already exists.\033[0m")
        return
    os.makedirs(proj_name, exist_ok=True)
    main_code = f"""# 🚀 Welcome to {proj_name}!
# Powered by AiraLang v{VERSION}
# Creator: {AUTHOR}

import "ai";
import "sec";

say "🔥 Welcome to {proj_name} powered by AiraLang!";
let creator = "{AUTHOR}";
say "⚡ Built by: " + creator;
"""
    with open(os.path.join(proj_name, "main.aira"), "w", encoding="utf-8") as f:
        f.write(main_code)
    with open(os.path.join(proj_name, "README.md"), "w", encoding="utf-8") as f:
        f.write(f"# {proj_name}\\n\\nProject created with AiraLang v{VERSION}.\\n\\nRun:\\n```bash\\nairalang main.aira\\n```\\n")
    print(f"\033[1;32m[+] Created new AiraLang project:\033[0m {proj_name}/")
    print(f"\033[1;34m[*] cd {proj_name} && airalang main.aira\033[0m")

def print_help():
    print(f"""\033[1;36mAiraLang v{VERSION}\033[0m
Creator: {AUTHOR}

\033[1;33mUsage:\033[0m
  airalang                             Start interactive REPL
  airalang <script.aira>               Execute an AiraLang script
  airalang run <script.aira>           Execute an AiraLang script
  airalang build <file.aira> [-o out]  Compile script to standalone executable
  airalang new <project_name>          Create a new AiraLang project scaffold
  airalang -v, --version               Display version information
  airalang -h, --help                  Show this help message
""")

def main():
    if len(sys.argv) > 1:
        arg1 = sys.argv[1]
        if arg1 in ("-v", "--version"):
            print(f"AiraLang v{VERSION} | Creator: {AUTHOR}")
        elif arg1 in ("-h", "--help"):
            print_help()
        elif arg1 == "run":
            if len(sys.argv) > 2:
                run_file(sys.argv[2])
            else:
                print("\033[1;31m[!] Error: Specify file to run: airalang run <file.aira>\033[0m")
        elif arg1 == "build":
            if len(sys.argv) > 2:
                src_file = sys.argv[2]
                out_file = None
                if "-o" in sys.argv:
                    idx = sys.argv.index("-o")
                    if idx + 1 < len(sys.argv):
                        out_file = sys.argv[idx + 1]
                build_file(src_file, out_file)
            else:
                print("\033[1;31m[!] Error: Specify file to build: airalang build <file.aira> [-o <out>]\033[0m")
        elif arg1 == "new":
            if len(sys.argv) > 2:
                new_project(sys.argv[2])
            else:
                print("\033[1;31m[!] Error: Specify project name: airalang new <project_name>\033[0m")
        else:
            run_file(arg1)
    else:
        start_repl()

if __name__ == "__main__":
    main()
