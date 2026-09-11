# 📡 AiraLang `net` Module
> **Low-Level Network Diagnostics & Sockets**

## Import
```aira
import "net";
```

## Methods
- `net.ping(host, [timeout=2])`: Check ICMP reachability.
- `net.port_open(host, port, [timeout=2])`: Test TCP socket connectivity.
- `net.local_ip()`: Retrieve current local network IP address.
- `net.fetch(url)`: Quick HTTP GET shortcut.

## Example
```aira
import "net";

say "Local IP: " + net.local_ip();
say "Gateway reachable: " + net.ping("1.1.1.1");
```
