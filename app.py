from flask import Flask, render_template, Response
import random
import itertools
import time
import os

texts = [
    "Logic will get you from A to B. Imagination will take you everywhere",
    "There are 10 kinds of people. Those who know binary and those who don't",
    "There are two ways of constructing a software design. One way is to make it so simple that there are obviously no deficiencies and the other is to make it so complicated that there are no obvious deficiencies.",
    "It's not that I'm so smart, it's just that I stay with problems longer."
    "It is pitch dark. You are likely to be eaten by a grue."
]

# Create Flask Application

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def stream_messages():
    while True:
        # Get random messages from the listed text above
        text = random.choice(texts)
        # Send the message as an event
        yield f"data: {text}\n\n"
        # Wait 2 seconds before next message
        time.sleep(2)

@app.route('/stream')
def stream():
    return Response(stream_messages(), mimetype='text/event-stream')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))