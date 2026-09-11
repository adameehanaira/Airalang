# 💻 AiraLang `os` Module
> **Operating System Interaction & Shell Commands**

## Import
```aira
import "os";
```

## Methods
- `os.cmd(command)` / `os.system(command)`: Execute shell command and return stdout.
- `os.env(name, [default])`: Read environment variable.
- `os.platform()`: Return host OS platform (linux, darwin, win32).
- `os.cwd()`: Current working directory.
- `os.listdir([path])`: List files and directories.
- `os.mkdir(path)`: Create directory recursively.

## Example
```aira
import "os";

say "OS: " + os.platform();
say "Files: ", os.listdir(".");
```
