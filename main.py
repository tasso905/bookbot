def main():
    count = 0
    returned_dict={}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        count += word_count(file_contents)
        returned_dict = letter_count(file_contents)
    print_report(count, returned_dict)

def word_count(words):
    count_words = len(words.split())
    return(count_words)

def letter_count(letters):
    count_dict={}
    for letter in letters:
        letter = letter.lower()
        if letter not in count_dict:
            count_dict[letter] = 1
        else:
            count_dict[letter] += 1
    return(count_dict)

def print_report(count, returned_dict):
    print("\n --- Begin report of books/frankenstein.txt --- \n")
    print(f"{count} words found in the document. \n")
    for key,value in returned_dict.items():
        print(f"The {key} character was found {value} times")

main()
