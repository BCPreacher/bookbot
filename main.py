import sys
from stats import get_book_text, count_words, count_characters, sort_list, gen_report

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    word_count = count_words(text)
    letter_counts = count_characters(text)
    sorted_letters = sort_list(letter_counts)
    gen_report(file_path, word_count, letter_counts)
    
main()


## for char, count in counted_numbers.items():
        ## print(f"{repr(char)}: {count}")