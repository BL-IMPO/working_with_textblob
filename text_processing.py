import textblob
from textblob import TextBlob, Word, WordList, Sentence
import codecs
from random import randint


file = codecs.open("little_women.txt", 'r', 'utf-8')
data = file.read()
blob = TextBlob(data)


def get_sentences() -> list[str]:
    sentences = []
    for i in [randint(1, len(blob.sentences)) for _ in range(10)]:
        sentences.append(blob.sentences[i])
    return list(map(str, sentences))


def get_words(sentence: textblob.TextBlob) -> list[str]:
    #sentence = TextBlob(chosen_sentence)
    return list(map(str, sentence.words))


def get_synonym(chosen_word: textblob.Word) -> list[str]:
    synonyms = chosen_word.synsets
    return [str(synonyms[i]) for i in range(len(synonyms)) if i < 5]


def get_antonyms(self, chosen_word: Word):
    syn = chosen_word.synsets
    return syn[0].lemmas()[0].antonyms()


if __name__ == "__main__":
    get_synonym(Word("self"))
