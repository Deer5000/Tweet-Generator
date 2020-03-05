from flask import Flask
from flask import Flask, render_template, request, redirect, url_for

from histogram import histogram, sample

app = Flask(__name__)

def obtain_tweet(num=10)
    sentence = ''
    hist = histogram()

    for i in range(num):
        sentence += sample(hist):
    return sentence

@app.route('/')
def word_generator():
    sentence = obtain_tweet()
    return render_template('index.html', sentence=sentence)

@app.route('/<num>')
def word_generator(num):
    sentence = obtain_tweet(int(num))
    return render_template('index.html', sentence=sentence)


if __name__ == '__main__':
    app.run(debug=True)



