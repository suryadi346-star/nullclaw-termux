import json
from pathlib import Path
import requests

CONFIG_PATH = Path(__file__).parent.parent / "config.json"
HISTORY_PATH = Path(__file__).parent.parent / "chat_history.json"

def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def save_history(messages):
    with open(HISTORY_PATH, "w") as f:
        json.dump(messages, f, indent=2, ensure_ascii=False)

def load_history():
    if HISTORY_PATH.exists():
        with open(HISTORY_PATH, "r") as f:
            return json.load(f)
    return []

def chat_with_ai(messages, config):
    headers = {
        "Authorization": f"Bearer {config['api_key']}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": config["model"],
        "messages": messages,
        "max_tokens": config.get("max_tokens", 1024),
        "temperature": config.get("temperature", 0.7)
    }
    try:
        response = requests.post(
            f"{config['api_base_url']}/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"⚠️ Network/API Error: {str(e)}"
    except Exception as e:
        return f"❌ Unexpected Error: {str(e)}"
