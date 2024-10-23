from flask import Flask, render_template, request
from textblob import TextBlob, Word
import random
import text_processing

app = Flask(__name__)

# Примерные предложения для демонстрации (замените на любые нужные вам)
sentences = text_processing.get_sentences()
random_sentences = random.sample(sentences, 10)
characters = ["Jo March", "Beth March", "Amy March", "Meg March", "Laurie"]


@app.route('/')
def index():
    # Генерация 10 случайных предложений
    return render_template('index.html', sentences=random_sentences)


@app.route('/process', methods=['POST'])
def process():
    selected_sentence = request.form.get('sentence')
    command = request.form.get('command')

    output = ""
    if selected_sentence:
        blob = TextBlob(selected_sentence)

        if command == 'words':
            output = ', '.join(text_processing.get_words(blob))
        elif command == 'synonym':
            #synonyms = [','.join(text_processing.get_synonym(Word(word))) for word in text_processing.get_words(blob)]
            output = "Synonyms: " + ','.join([str(text_processing.get_synonym(Word(word))[1]) for word in text_processing.get_words(blob)])
            print(output)
        elif command == 'antonym':
            output = "Антонимы: (в TextBlob не реализованы)"
        elif command == 'lemmas':
            output = ', '.join([word.lemmatize() for word in blob.words])

    rns = random_sentences[0]
    random_sentences[0] = selected_sentence

    return render_template('index.html', sentences=random_sentences, output=output, characters=characters)

#random.sample(sentences, 10)
@app.route('/characters', methods=['POST'])
def characters_list():
    return render_template('index.html', sentences=random.sample(sentences, 10), characters=characters)


if __name__ == '__main__':
    app.run(debug=True)