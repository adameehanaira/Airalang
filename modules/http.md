# 🌐 AiraLang `http` Module
> **HTTP Networking & Web Request Client**

## Import
```aira
import "http";
```

## Methods
- `http.get(url, [headers])`: Perform HTTP GET request.
- `http.post(url, data_payload, [headers])`: Perform HTTP POST request.
- `http.download(url, destination_path)`: Download remote file to local disk.
- `http.status(url)`: Get HTTP response status code.

## Example
```aira
import "http";

let html = http.get("https://httpbin.org/get");
say html;
```
