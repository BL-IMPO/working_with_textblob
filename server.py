from flask import Flask, render_template, request
from textblob import TextBlob, Word
import random
import text_processing

app = Flask(__name__)

sentences = text_processing.get_sentences()
characters = [""]


@app.route('/')
def index():
    return render_template('index.html', sentences=sentences)


@app.route('/process', methods=['POST'])
def process():
    selected_sentence = request.form.get('sentence')
    command = request.form.get('command')

    output = ""
    if selected_sentence:
        blob = TextBlob(selected_sentence)

        if command == 'words':
            output = ', '.join(text_processing.get_words(blob))
        elif command == 'select':
            # pass selected sentence to top
            sentences[0] = selected_sentence
        elif command == 'synonym':
            pass
        elif command == 'antonym':
            pass
        elif command == 'lemmas':
            output = text_processing.get_lemmatize(selected_sentence)

    return render_template('index.html', sentences=sentences, output=output, characters=characters)


@app.route('/characters', methods=['POST'])
def characters_list():
    return render_template('index.html', sentences=random.sample(sentences, 10), characters=characters)


if __name__ == '__main__':
    app.run(debug=True)
