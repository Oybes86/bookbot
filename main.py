# Python
import sys
from stats import count_words, char_count, sort_char_counts


def get_book_text(filepath):
    with open (filepath) as f:
        file_contents = f.read()
    return file_contents

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_book = sys.argv[1]
        book_text = get_book_text(path_to_book)
        word_count = count_words(book_text)
        character_count = char_count(book_text)
        sorted_chars = sort_char_counts(character_count)
    print("""============ BOOKBOT ============
Analyzing book found at {}...
----------- Word Count ----------
Found {} total words
--------- Character Count -------""".format(path_to_book, word_count))
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()