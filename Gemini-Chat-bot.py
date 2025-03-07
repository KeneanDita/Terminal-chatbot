import os
import requests
import json

#insert your Gemini API key between the parenthesis
api_key = ""

if not api_key:
    raise ValueError("API key not found. Set the GEMINI_API_KEY environment variable.")

GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

def chat_with_gemini():
    print("Gemini AI Assistant (type 'exit' to quit)")

    while True:
        try:
            user_input = input("\nPrompt: ")
            if user_input.lower() == "exit":
                print("Goodbye")
                break

            payload = {
                "contents": [{
                    "parts": [{"text": user_input}]
                }]
            }

            headers = {"Content-Type": "application/json"}
            response = requests.post(GEMINI_API_URL, headers=headers, data=json.dumps(payload))

            if response.status_code != 200:
                print(f"\nError: {response.status_code} - {response.text}")
                continue

            ai_response = response.json()
            reply = ai_response.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")

            print("\nAI:", reply if reply else "No response from AI.")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}\nCheck your API key and internet connection.")

chat_with_gemini()
