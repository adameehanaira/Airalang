# 🤖 AiraLang `ai` Module
> **Generative AI & LLM Integration Engine**  
> Native dual-provider AI supporting both Google Gemini and Groq LLMs with automatic key-prefix routing and custom system prompts.

## Import
```aira
import "ai";
```

## Methods
- `ai.set_key(api_key, [provider])`: Configure API key. Keys starting with `gsk_` automatically select Groq; others select Gemini.
- `ai.get_key([provider])`: Retrieve configured API key.
- `ai.set_system(prompt)`: Customize the AI engine system prompt/persona (default: official Aira persona).
- `ai.ask(prompt, [model], [key], [system])`: Send a prompt and get the AI model response.
- `ai.groq(prompt, [model], [key], [system])`: Direct execution on Groq cloud inference.
- `ai.summarize(text, [max_words])`: Summarize text within specified word count.
- `ai.chat(messages, [model], [key])`: Multi-turn conversational chat.

## Example
```aira
import "ai";

ai.set_key("gsk_YOUR_GROQ_KEY");
let ans = ai.ask("What is AiraLang?");
say ans;
```
