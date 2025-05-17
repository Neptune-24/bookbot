def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def word_count(path_to_file):
    text = get_book_text(path_to_file)
    words = text.split()
    return len(words)


def char_count(path_to_file):
    text = get_book_text(path_to_file)
    character_counts = {}
    for char in text:
        char = char.lower()
        character_counts[char] = character_counts.get(char, 0) + 1
    return character_counts


def sort_on(item):
    return item["num"]


def char_count_sort(character_counts):
    sorted_list = []
    for key, value in character_counts.items():
        sorted_dict = {"char": key, "num": value}
        sorted_list.append(sorted_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
