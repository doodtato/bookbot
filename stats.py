def get_num_words(book):
    word_count = 0
    words = book.split()
    for word in words:
        word_count += 1
    return word_count

def count_characters(book):
    char_count = {}
    book = book.lower()
    for char in book:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def sort_on(char_list):
    return char_list["count"]

def sort_dict(char_list):
    char_list = [{"character": char, "count": count} for char, count in char_list.items()]
    char_list.sort(key=sort_on, reverse=True)
    return char_list