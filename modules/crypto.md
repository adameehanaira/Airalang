# 🔐 AiraLang `crypto` Module
> **Cryptographic Hashing & Encoding**

## Import
```aira
import "crypto";
```

## Methods
- `crypto.md5(text)`: Generate MD5 hex digest.
- `crypto.sha256(text)`: Generate SHA-256 hex digest.
- `crypto.sha1(text)`: Generate SHA-1 hex digest.
- `crypto.base64_encode(text)`: Base64 encoding.
- `crypto.base64_decode(encoded)`: Base64 decoding.

## Example
```aira
import "crypto";

say "Hash: " + crypto.sha256("admin123");
```
