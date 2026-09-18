# 💻 `system` Module (AiraLang Cross-Platform Hardware & OS)

Native cross-platform system diagnostic, hardware telemetry, and host environment inspection module. Companion module to `android`, designed for PC, Laptop, and Server environments (Windows, Linux, and Termux).

Can be imported as either:
```aira
import "system";
# or
import "hardware";
```

---

## 🛠️ Functions & Capabilities

### 1. `system.info()`
Returns comprehensive hardware and operating system telemetry in a unified dictionary:
- `platform`: Host OS platform identifier (`win32`, `linux`, etc.)
- `cpu`: CPU details (name, core count, architecture)
- `ram`: System memory metrics (total GB, available GB, used GB, percent used)
- `gpu`: GPU profile (NVIDIA model, VRAM total, free VRAM, driver version, status)
- `battery`: Power source and battery percentage

```aira
import "system";
let info = system.info();
say "Platform: " + info.platform;
say "CPU: " + info.cpu.name;
say "RAM: " + info.ram.total_gb + " GB";
```

---

### 2. `system.gpu()`
Detects dedicated and integrated graphics processing units, querying NVIDIA SMI on modern GPUs (e.g. RTX 3050, 4060, etc.):
- `name`: Full GPU brand and model
- `total_vram_mb`: Total video memory in Megabytes
- `free_vram_mb`: Available free VRAM
- `driver_version`: Installed NVIDIA driver version
- `temperature_c`: Current GPU die temperature in Celsius
- `status`: `"active"` or `"integrated_or_unavailable"`

```aira
import "system";
let gpu = system.gpu();
say "GPU Model: " + gpu.name;
if (gpu.total_vram_mb > 0) {
    say "VRAM: " + gpu.total_vram_mb + " MB";
}
```

---

### 3. `system.battery()`
Inspects battery and charging status via native Windows Kernel32 / Linux power supply APIs:
- `percentage`: Battery state of charge (0 - 100%)
- `is_charging`: Boolean whether power is connected
- `power_source`: Detailed power source status

```aira
import "system";
let bat = system.battery();
say "Battery: " + bat.percentage + "% | Charging: " + bat.is_charging;
```

---

### 4. `system.ram()`
Queries live RAM memory allocation:
- `total_gb`: Total physical RAM
- `available_gb`: Available free memory
- `used_gb`: Currently utilized memory
- `percent_used`: Memory load percentage (0 - 100)

```aira
import "system";
let mem = system.ram();
say "RAM: " + mem.used_gb + " / " + mem.total_gb + " GB (" + mem.percent_used + "% used)";
```

---

### 5. `system.cpu()`
Queries CPU architecture, core topology, and model identifier:
- `cores`: Logical core count
- `name`: Processor identifier string
- `architecture`: Machine architecture

```aira
import "system";
let cpu = system.cpu();
say "CPU: " + cpu.name + " (" + cpu.cores + " Cores)";
```
