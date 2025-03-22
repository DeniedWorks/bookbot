import sys
from stats import get_num_words, get_book_text, get_chars_dict, get_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_list = get_list(chars_dict)

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {book_path}...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for char_dict in chars_list:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f'{char}: {count}')
    print('============= END ===============')

main()