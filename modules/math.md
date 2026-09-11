# 📐 AiraLang `math` Module
> **Mathematical Functions & Constants**

## Import
```aira
import "math";
```

## Methods & Constants
- `math.sqrt(x)`: Square root.
- `math.floor(x)`, `math.ceil(x)`: Rounding down and up.
- `math.abs(x)`: Absolute value.
- `math.round(x, [decimals])`: Rounding.
- `math.pow(base, exp)`: Exponentiation.
- `math.random(low, high)`: Generate random integer or float.
- `math.pi`: $\pi$ constant (~3.14159265).
- `math.e`: Euler constant (~2.7182818).

## Example
```aira
import "math";

say "Hypotenuse: " + math.sqrt(math.pow(3, 2) + math.pow(4, 2)); # 5.0
```
