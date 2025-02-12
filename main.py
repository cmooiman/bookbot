def main(book_path):
    text = get_text(book_path)
    word_count = get_word_count(text)
    print(f"The file '{book_path}' has {word_count} words.")

def get_text(book_path):
    with open(book_path) as f:
        return f.read()
        
def get_word_count(text):
    word_count = text.split()
    return len(word_count)

main("books/frankenstein.txt")