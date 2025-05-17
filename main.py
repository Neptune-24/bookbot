import sys
from stats import word_count
from stats import char_count
from stats import char_count_sort

try:
    sys.argv[1]
except IndexError:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book = sys.argv[1]


def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")

    num_words = word_count(book)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    total_characters = char_count(book)

    sorted_characters = char_count_sort(total_characters)
    for char in sorted_characters:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")

    print("============= END ===============")


main()
