# 💖 AiraLang `proposal` Module
> **Cyber-Romance & Proposal Prank Engine**  
> Features an automated HTTP 500 Server Love Timeout loop and an intelligent Lover Accept Checker AI with celebratory wishes.

## Import
```aira
import "proposal";
import "ai"; # Optional, for shared API key configuration
```

## Methods
- `proposal.ask(prompt="Do You Love Me : ", [api_key], [wish_enabled=True])`: Runs proposal prompt. Automatically enters an inescapable simulated HTTP 500 error loop until target answers affirmatively.
- `proposal.set_key(api_key)`: Sets Groq or Gemini API key for Lover Accept Checker AI sentiment analysis.
- `proposal.set_system(system_prompt)`: Customizes Lover Accept Checker AI persona.
- `proposal.set_wish(custom_wish)`: Sets a custom congratulatory message.
- `proposal.wish([custom_message])`: Triggers Aira celebratory wish immediately.

## Example
```aira
import "proposal";
import "ai";

ai.set_key("gsk_YOUR_GROQ_KEY");

proposal.ask("Do You Love Me : ");
say "mee too 🩷";
```
