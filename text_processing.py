import textblob
from textblob import TextBlob, Word, WordList, Sentence
import codecs
from random import randint


file = codecs.open("little_women.txt", 'r', 'utf-8')
data = file.read()
blob = TextBlob(data)


def word_normalize(word: str) -> str:
    return ''.join(char for char in word if char.isalnum())


def get_sentences() -> list[str]:
    sentences = []
    current_sentences = ["Select sentence."]
    for i in [randint(1, len(blob.sentences)) for _ in range(10)]:
        sentences.append(blob.sentences[i])

    for i in sentences:
        current_sentences.append(str(i))

    return current_sentences


def get_words(sentence: textblob.TextBlob) -> list[str]:
    return list(map(str, sentence.words))


def get_synonym(chosen_word: textblob.Word) -> str:
    word = Word(word_normalize(chosen_word))
    synonym = word.synsets[0]
    return str(synonym)


def get_antonyms(chosen_word: Word):
    syn = chosen_word.synsets
    return syn[0].lemmas()[0].antonyms()


def get_lemmatize(chosen_sentence: str):
    sentence = TextBlob(chosen_sentence)
    return ', '.join([str(Word(word_normalize(word)).lemmatize()) for word in get_words(sentence)])


if __name__ == "__main__":
    print(get_synonym("I"))
