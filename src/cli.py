#!/data/data/com.termux/files/usr/bin/python3
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lexer import Lexer
from parser import Parser
from evaluator import Evaluator

VERSION = "1.3.0 (Pro Edition)"
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

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] in ("-v", "--version"):
            print(f"AiraLang v{VERSION} | Creator: {AUTHOR}")
        elif sys.argv[1] in ("-h", "--help"):
            print("Usage: airalang [script.aira]")
            print("       airalang (starts interactive REPL)")
        else:
            run_file(sys.argv[1])
    else:
        start_repl()

if __name__ == "__main__":
    main()
