def main(book_path):
    text = get_text(book_path)
    word_count = get_word_count(text)
    occurence = get_character_counts(text)
    print(f"--- Begin report of '{book_path}' --- ")
    print(f"{word_count} words found in document.\n")
    alphabet = isalpha(occurence)
    for key, value in alphabet.items():
        print(f"Character '{key}' appears '{value}' times.")
    sorted_alpha = sort_alpha(alphabet)
    print(sorted_alpha)
#    for key, value in occurence.items():
#        if key.isalpha():
#            print(f"Character '{key}' appears '{value}' times.")
    print(f"--- End report ---")

def get_text(book_path):
    with open(book_path) as f:
        return f.read()
        
def get_word_count(text):
    word_count = text.split()
    return len(word_count)

def get_character_counts(text):
    lowered_text = text.lower()
    occurence = {}
    for i in lowered_text:
        if i in occurence:
            occurence[i] += 1
        else:
            occurence[i] = 1
    return occurence

def isalpha(occurence):
    alphabet = {}
    for key, value in occurence.items():
        if key.isalpha():
            alphabet[key] = value
    return alphabet

def sort_on(alphabet):
    return alphabet["value"]

def sort_alpha(alphabet):
    alphabet_list = []
    for key, value in alphabet.items():
        alphabet_list.append({"key": key, "value": value})
    sorted_by_num = alphabet_list.sort(reverse=True, key=sort_on)
    return sorted_by_num


main("books/frankenstein.txt")