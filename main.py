def main(book_path):
    text = get_text(book_path)
    word_count = get_word_count(text)
    occurence = get_character_counts(text)
    print(f"The file '{book_path}' contains {word_count} words.")
    for key, value in occurence.items():
        if key == '\n':
            print(f"Character '\\n' appears '{value}' times.")            
        else:
            print(f"Character '{key}' appears '{value}' times.")

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



main("books/frankenstein.txt")