# 🛡️ AiraLang `sec` Module
> **Cybersecurity & Ethical Reconnaissance Engine**  
> Built natively for security researchers, penetration testers, and cyber defenders.

## Import
```aira
import "sec";
```

## Methods
- `sec.scan_ports(host, ports, [timeout])`: Multi-threaded TCP port scanner.
- `sec.scan_port(host, port, [timeout])`: Single port check.
- `sec.banner(host, port, [timeout])`: Grab service banner.
- `sec.audit_headers(url)`: Security header audit (CSP, HSTS, X-Frame-Options) with grading.
- `sec.subdomains(domain)`: Discover subdomains via Certificate Transparency.
- `sec.hash_identify(hash_string)`: Identify hash algorithms (MD5, SHA1, SHA256, Bcrypt, etc.).
- `sec.crack_md5(hash, wordlist)`: Dictionary-based MD5 cracker.
- `sec.resolve(hostname)`: DNS host-to-IP resolution.
- `sec.reverse_dns(ip)`: Reverse DNS lookup.

## Example
```aira
import "sec";

let open_ports = sec.scan_ports("google.com", [80, 443, 8080]);
say "Open Ports: ", open_ports;
```
