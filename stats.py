def count_words(book_text):
    words = book_text.split()
    return len(words)
def char_count(book_text):
    chars = {}
    for char in book_text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_char_counts(char_dict):
    """
    Takes a dict of character counts and returns a sorted list of dicts with 'char' and 'num',
    sorted descending by count, skipping non-alphabetical chars.
    """
    char_list = [
        {"char": c, "num": n}
        for c, n in char_dict.items()
        if c.isalpha()
    ]
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list

