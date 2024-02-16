def main():
    return 0

def get_document_letters_dict(document):
    text_content = {}
    for word in document.split():
        aux_dictionary = get_word_letters_dict(word)
        for key in aux_dictionary:
            if key not in text_content:
                text_content[key] = aux_dictionary[key]
            else:
                text_content[key] += aux_dictionary[key]
    return text_content


def get_word_letters_dict(word):
    word_content = {}
    lowered_word = word.lower()
    for char in lowered_word:
        if char in word_content:
            word_content[char] += 1
        else:
            word_content[char] = 1
    return word_content


def count_words(book):
    words = book.split()
    return len(words)


def get_document_content(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


main()
