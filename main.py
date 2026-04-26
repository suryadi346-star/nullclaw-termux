#!/usr/bin/env python3
import sys
from nullclaw_cli.core import load_config, load_history, save_history, chat_with_ai
from nullclaw_cli.ui import display_welcome, display_response

def main():
    config = load_config()
    if config["api_key"] == "YOUR_API_KEY_HERE":
        print("🔑 Edit config.json dulu dan masukkan API key!")
        sys.exit(1)

    display_welcome()
    messages = load_history()
    if not messages:
        messages = [{"role": "system", "content": config["system_prompt"]}]

    try:
        while True:
            try:
                user_input = input("\n\033[1;34mYou\033[0m: ").strip()
            except EOFError:
                break

            cmd = user_input.lower()
            if cmd in ["exit", "quit"]:
                print("\033[2mSaving history & exiting...\033[0m")
                save_history(messages)
                break
            if cmd == "clear":
                messages = [{"role": "system", "content": config["system_prompt"]}]
                save_history(messages)
                print("\033[33m🧹 History cleared.\033[0m")
                continue
            if not user_input:
                continue

            messages.append({"role": "user", "content": user_input})
            print("\n\033[1;33m🐾 NullClaw\033[0m thinking...")
            
            response = chat_with_ai(messages, config)
            messages.append({"role": "assistant", "content": response})
            display_response(response)
            save_history(messages)

    except KeyboardInterrupt:
        print("\n\033[2m⚡ Interrupted. History saved.\033[0m")
        save_history(messages)
        sys.exit(0)

if __name__ == "__main__":
    main()
