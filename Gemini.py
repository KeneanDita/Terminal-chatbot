import requests
import json
from colorama import Fore, Style, init

init(autoreset=True)

#insert your Gemni API key here
api_key = ""

if not api_key:
    raise ValueError("API key not found. Set the GEMINI_API_KEY environment variable.")

GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

def format_response(text):
    """Formats AI response with proper spacing and colors."""
    return f"\n{Fore.YELLOW}AI:{Style.RESET_ALL}\n{'-'*50}\n{text}\n{'-'*50}\n"

def chat_with_gemini():
    print(f"{Fore.CYAN} AI Assistant (type 'exit' to quit){Style.RESET_ALL}")

    while True:
        try:
            user_input = input(f"\n{Fore.GREEN}You:{Style.RESET_ALL} ")

            if user_input.lower() == "exit":
                print(f"{Fore.RED}Goodbye!{Style.RESET_ALL}")
                break

            payload = {
                "contents": [{
                    "parts": [{"text": user_input}]
                }]
            }

            headers = {"Content-Type": "application/json"}
            response = requests.post(GEMINI_API_URL, headers=headers, data=json.dumps(payload))

            if response.status_code != 200:
                print(f"\n{Fore.RED}Error: {response.status_code} - {response.text}{Style.RESET_ALL}")
                continue

            ai_response = response.json()
            reply = ai_response.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")

            print(format_response(reply if reply else "No response from AI."))

        except KeyboardInterrupt:
            print(f"\n{Fore.RED}Goodbye!{Style.RESET_ALL}")
            break
        except Exception as e:
            print(f"\n{Fore.RED}Error: {e}\nCheck your API key and internet connection.{Style.RESET_ALL}")

chat_with_gemini()
