
from flask import Flask, request, jsonify, render_template
import config as c
import bot_request as br
import random

app = Flask(__name__)


# Initialize your chatbot here (as per your setup)
bot = br.Chatbot(c.initial_message, c.API_KEY)


@app.route('/')
def home():
    return render_template('chat.html')


@app.route('/greet', methods=['GET'])
def greet():
    # Generate or retrieve a greeting message
    greetings = [
        "Hey there! I'm Eran's sidekick in the digital realm. What's cooking, good looking?",
        "Knock knock! Eran's bot here. Who's there? You needing help?",
        "Guess who?! Eran's friendly neighborhood bot. Ready to crack some codes or jokes?",
        "Bing bong! Eran's AI at your service. Spill the beans, what's the mission?",
        "Yo! Eran's digital genie here. Rub the keyboard and make your wish!",
        "Psst! Eran's secret bot agent reporting for duty. Got any mysteries for me?",
        "Whazzup?! Eran's bot, the master of bytes and bits. How can I add a byte of fun today?",
        "Ahoy matey! Captain Botbeard at your service. Where shall we set sail in the sea of information?",
        "Hello from the other side! Eran's bot tuning in. Ready to cross the digital divide?",
        "Howdy, partner! Eran's wild west bot here. Ready to lasso some answers for ya?"
    ]
    # select a radnom greeting from list
    greeting = greetings[random.randint(0, len(greetings) - 1)]
    return jsonify({'greeting': greeting})


@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data['user_input']
    bot.chatbot_response(user_input)
    response = bot.chat_response  # Modify this line according to how your chatbot processes input
    return jsonify({'response': response})


if __name__ == '__main__':
    app.run()