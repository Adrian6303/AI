import nltk
from unidecode import unidecode

#nltk.download('punkt')

def read_text(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def count_sentences(text):
    sentences = nltk.sent_tokenize(text)
    return len(sentences)

def count_words(text):
    words = nltk.word_tokenize(text)
    return len(words)

def count_unique_words(text):
    words = nltk.word_tokenize(text)
    unique_words = set(words)
    return len(unique_words)

def find_shortest_longest_words(text):
    words = nltk.word_tokenize(text)
    shortest_word = min(words, key=len)
    longest_word = max(words, key=len)
    return shortest_word, longest_word

def remove_diacritics(text):
    return unidecode(text)


file_path = 'data\\texts.txt'

text = read_text(file_path)

num_sentences = count_sentences(text)
print("Numărul de propoziții din text:", num_sentences)

num_words = count_words(text)
print("Numărul de cuvinte din text:", num_words)

num_unique_words = count_unique_words(text)
print("Numărul de cuvinte diferite din text:", num_unique_words)

shortest_word, longest_word = find_shortest_longest_words(text)
print("Cel mai scurt cuvânt:", shortest_word)
print("Cel mai lung cuvânt:", longest_word)

text_without_diacritics = remove_diacritics(text)
print("Textul fără diacritice:")
print(text_without_diacritics)