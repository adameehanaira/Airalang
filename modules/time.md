# ⏱️ AiraLang `time` Module
> **Time, Clock & Sleep Utilities**

## Import
```aira
import "time";
```

## Methods
- `time.now()`: Formatted current timestamp (`YYYY-MM-DD HH:MM:SS`).
- `time.time()`: Unix epoch timestamp in seconds.
- `time.sleep(seconds)`: Pause thread execution.

## Example
```aira
import "time";

say "Start: " + time.now();
time.sleep(1);
say "End: " + time.now();
```
