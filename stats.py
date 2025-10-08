def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    letter_counts = {}
    for char in text.lower():
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1
    return letter_counts

def sort_list(letter_counts):
         return sorted(letter_counts.items(), key=lambda x: (-x[1], x[0]))

def gen_report(file_path, word_count, letter_counts):
    sorted_letters = sort_list(letter_counts)
    print("============ BOOKBOT ============")
    print(f"Processing book found at:{file_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, count in sorted_letters:
        print(f"{char}: {count}")
    print("============= END ===============")
