def main():
    return 0

def count_words(book):
    words = book.split()
    return len(words)


def get_document_content(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


main()
