from stats import get_num_words
from stats import count_characters
from stats import sort_dict

def get_book_text():
    with open("books/frankenstein.txt") as book:
        book_contents = book.read()
    return book_contents


def main():
    book = get_book_text()
    word_count = get_num_words(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    char_count = count_characters(book)
    char_count_sorted = sort_dict(char_count)
    print("--------- Character Count -------")
    for char_dict in char_count_sorted:
        char = char_dict["character"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")

main()