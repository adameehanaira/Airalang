# 📁 AiraLang `file` Module
> **Local File System I/O Operations**

## Import
```aira
import "file";
```

## Methods
- `file.read(path)`: Read entire text file.
- `file.write(path, content)`: Overwrite file with content.
- `file.append(path, content)`: Append content to file.
- `file.exists(path)`: Check if file exists.
- `file.delete(path)`: Remove file.
- `file.size(path)`: Get file size in bytes.

## Example
```aira
import "file";

file.write("test.txt", "AiraLang v1.4.1");
let text = file.read("test.txt");
say text;
```
