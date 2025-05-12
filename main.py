import sys
from stats import word_count


def main():
    count = 0
    returned_dict={}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        count += word_count(file_contents)
        returned_dict = letter_count(file_contents)
    print_report(count, returned_dict)

def letter_count(letters):
    count_dict={}
    for letter in letters:
        letter = letter.lower()
        if letter not in count_dict:
            count_dict[letter] = 1
        else:
            count_dict[letter] += 1
    return(count_dict)

def print_report(count, returned_dict, bookpath):
    print(f"\n --- Begin report of {bookpath} --- \n")
    print(f"{count} words found in the document. \n")
    #for key,value in returned_dict.items():
    #    print(f"The {key} character was found {value} times")
    if 'e' in returned_dict:
        print(f"e: {returned_dict['e']}")
    if 't' in returned_dict:
        print(f"t: {returned_dict['t']}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    count = 0
    returned_dict = {}

    with open(file_path, 'r') as f:
        file_contents = f.read()

    count += word_count(file_contents)
    returned_dict = letter_count(file_contents)

    print_report(count, returned_dict, file_path)

if __name__ == "__main__":
    main()
