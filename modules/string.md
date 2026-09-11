# 🔤 AiraLang `string` Module
> **Advanced Text & String Utilities**

## Import
```aira
import "string";
```

## Methods
- `string.split(text, [delimiter])`: Split text into array.
- `string.replace(text, old, new)`: Replace occurrences.
- `string.upper(text)`: Convert to uppercase.
- `string.lower(text)`: Convert to lowercase.
- `string.trim(text)`: Strip whitespace.
- `string.length(text)`: Get length.
- `string.contains(text, sub)`: Check substring presence.
- `string.starts_with(text, prefix)`: Check prefix.
- `string.ends_with(text, suffix)`: Check suffix.
- `string.join(list, [sep])`: Join list into string.

## Example
```aira
import "string";

say string.upper("hello world");
```
