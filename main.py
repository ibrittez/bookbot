def main():
    return 0

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
