import openai

openai.api_key = "Enter your API key here"  # Insert your actual API key here

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]  # Fix: corrected dictionary syntax for "role"
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":  # Fix: use double underscores __name__ and __main__
    while True:
        user_input = input("You: ")  # Fix: added indentation
        if user_input.lower() in ["quit", "exit", "bye"]:  # Fix: call lower() as a method
            break

        response = chat_with_gpt(user_input)
        print("Chatbot:", response)

    