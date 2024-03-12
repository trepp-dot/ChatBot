from openai import OpenAI


# A class that represents a chatbot
class Chatbot:
    def __init__(self, initial_message, api_key):
        self.client = OpenAI(api_key=api_key)
        self.current_massage = initial_message
        self.chat_response = ''

    # a function that receives a message and returns a response
    def chatbot_response(self, message_text=None):
        message = self.current_massage
        if message_text is not None:
            message = message + [{"role": "user", "content": message_text}]

        # Send the message to the chatbot
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=message,
            temperature=0.5,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        message = message + [{"role": "assistant", "content": response.choices[0].message.content}]
        self.current_massage = message
        self.chat_response = response.choices[0].message.content
