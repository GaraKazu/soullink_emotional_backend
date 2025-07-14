import requests

API_URL = "http://127.0.0.1:8000/chat"

def main():
    print("🌸 Welcome to SoulLink — Talk to Noel")
    print("Type 'exit' to leave.\n")

    chat_history = []  # Keep track of conversation

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bye!")
            break

        payload = {
            "message": user_input,
            "chat_history": chat_history
        }

        try:
            response = requests.post(API_URL, json=payload)
            response.raise_for_status()
            data = response.json()

            noel_reply = data.get("response", "...")
            print(f"Noel: {noel_reply}")

            # Save conversation history for context (user and Noel)
            chat_history.append((user_input, noel_reply))

        except Exception as e:
            print(f"Noel: Oops, something went wrong: {e}")

if __name__ == "__main__":
    main()
