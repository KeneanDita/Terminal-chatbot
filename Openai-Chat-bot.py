import openai

#insert your api key here
api_key = ""

def chat_with_ai():
    print("AI Assistant (type 'exit' to quit)")
    while True:
        try:
            user_input = input("\nPrompt: ")
            if user_input.lower() == "exit":
                print("Goodbye!")
                break
            client = openai.OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": "Hello"}]
            )

            print(response.choices[0].message.content)
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")

chat_with_ai()
