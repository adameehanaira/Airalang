# 📱 `android` Module (AiraLang Native Android Security)

Native Android security inspection, APK static analysis, and device hardening module engineered specifically for mobile application penetration testing and security auditing directly inside Termux and Linux environments.

Can be imported as either:
```aira
import "android";
# or
import "droidsec";
```

---

## 🛠️ Functions & Capabilities

### 1. `android.device_info()`
Returns comprehensive hardware and operating system profile details:
- `brand`: Device brand (e.g. Redmi, Samsung, Google)
- `model`: Device hardware model code
- `manufacturer`: Hardware manufacturer
- `android_version`: Android OS release version (e.g. "16")
- `sdk_version`: Android API level integer (e.g. 36)
- `arch`: CPU architecture (e.g. arm64-v8a)
- `build_type`: OS build variant (e.g. "user", "userdebug")

```aira
import "android";
let dev = android.device_info();
say "Device: " + dev.brand + " " + dev.model;
say "Android Version: " + dev.android_version + " (API " + dev.sdk_version + ")";
```

---

### 2. `android.audit_device()`
Performs complete security posture and integrity audit on the host device:
- `is_rooted`: Boolean checking SU binaries (`/system/bin/su`, `/data/local/su`, Magisk paths).
- `bootloader_locked`: Boolean evaluating `ro.boot.flash.locked`.
- `verified_boot`: Android Verified Boot (AVB) state (e.g. "green", "yellow", "orange").
- `is_debuggable_os`: Boolean checking if OS runs with `ro.debuggable=1`.
- `security_score`: Calculated integer security health score (0 - 100).
- `posture`: Overall rating: `"SECURE"`, `"MODERATE_RISK"`, or `"HIGH_RISK"`.
- `findings`: List of security risks discovered.
- `recommendations`: Hardening recommendations.

```aira
import "android";
let audit = android.audit_device();
say "Device Posture: " + audit.posture;
say "Security Score: " + audit.security_score + "/100";
say "Root Detected: " + audit.is_rooted;
say "Findings: " + audit.findings;
```

---

### 3. `android.audit_apk(apk_path)`
High-speed zero-dependency static APK security auditor:
- **Binary AXML String Extractor:** Decodes permissions and configuration flags from compiled `AndroidManifest.xml`.
- **Dangerous Permissions Identifier:** Flags high-risk permissions (SMS, Camera, Location, Audio, Contacts).
- **Security Misconfigurations:** Checks `debuggable`, `allowBackup`, and `usesCleartextTraffic`.
- **DEX Bytecode Key Scanner:** Scans compiled `.dex` files for exposed cloud keys (Google API `AIza...`, AWS `AKIA...`, plaintext HTTP URLs).
- **Signature Audit:** Checks for META-INF signatures and flags insecure Android Debug Keystores.

```aira
import "android";
let report = android.audit_apk("/sdcard/Download/target.apk");
say "Package Name: " + report.package_name;
say "Risk Level: " + report.risk_level;
say "Dangerous Permissions: " + report.dangerous_permissions;
say "Exposed Keys: " + report.hardcoded_secrets;
say "Findings: " + report.findings;
```

---

### 4. `android.audit_package(package_name)`
Attempts to locate and audit an installed package by name.

```aira
import "android";
let report = android.audit_package("com.whatsapp");
say report;
```

---

### 5. `android.check_root()` / `android.is_rooted()`
Quick boolean helper returning `true` if root / su binary is detected.

---

### 6. `android.get_prop(prop_name)`
Queries any Android system property via `/system/bin/getprop`:
```aira
import "android";
say "CPU ABI: " + android.get_prop("ro.product.cpu.abi");
```
