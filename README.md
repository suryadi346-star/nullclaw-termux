# 🐾 NullClaw AI for Termux
Terminal AI assistant yang berjalan **native di Termux** tanpa `proot-distro` atau root.

## ✨ Fitur
- Ringan & cepat (Python + Requests + Rich)
- Chat history persistent (`chat_history.json`)
- Support semua OpenAI-compatible API (OpenRouter, Ollama lokal, Groq, dll)
- UI terminal bersih dengan markdown rendering

## 🚀 Instalasi
```bash
# 1. Extract ZIP
https://github.com/suryadi346-star/nullclaw-termux.git
cd nullclaw-termux

# 2. Setup
bash setup_termux.sh

# 3. Masukkan API Key
nano config.json  # Ganti YOUR_API_KEY_HERE
```
## Penggunaan

```bash
python main.py
```

## Konfigurasi API
| Field | Keterangan |
|-------|------------|
| `api_base_url` | Endpoint API (default: OpenAI) |
| `api_key` | API Key Anda |
| `model` | Nama model (contoh: `gpt-3.5-turbo`, `llama3-8b`, `mistral`) |
| `system_prompt` | Peran & gaya respons AI |

> 💡 **Opsi Offline**: Install [Ollama Android](https://github.com/ollama/ollama) atau jalankan Ollama di PC/Laptop, lalu ubah `api_base_url` ke `http://localhost:11434/v1` (jika di device yang sama).

# nullclaw-termux
