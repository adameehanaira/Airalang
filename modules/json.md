# 📋 AiraLang `json` Module
> **JSON Parsing & Serialization**

## Import
```aira
import "json";
```

## Methods
- `json.parse(json_string)`: Parse JSON string into AiraLang dictionary or list.
- `json.stringify(obj, [indent=2])` / `json.mkstring()`: Serialize data structure to JSON.

## Example
```aira
import "json";

let obj = json.parse("{"status": "ok", "code": 200}");
say obj["status"];
```
