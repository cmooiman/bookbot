#A script that for every text file in a directory returns the word and character count in descending order.

#Path is used in the process_directory() function. Enables the use of path objects instead of 'path to file' strings.
from pathlib import Path

def main(directory_path):
    """
    Converts directory path to a path object and calls main() over every .txt file in the directory.
    
    Args:
        directory_path (str): Path to the directory to be processed.
    
    """
    directory = Path(directory_path)
    for file_path in directory.glob("*.txt"):
        process_file(file_path)

def process_file(file_path):
    """
    Prints a report on the amount of words and the count of alphabet characters in descending order of a file.

    Args:
        file_path (str): Path to the file to read.

    Return:
        No returns.
    """
    text = get_text(file_path)
    word_count = get_word_count(text)
    occurence = get_character_counts(text)
    alphabet = isalpha(occurence)
    sorted_alpha = sort_alpha(alphabet)
    
    #Print statements for a readable report on the book's content.
    print(f"--- Begin report of {file_path} --- ")
    print(f"{word_count} words found in document.\n")
    for character in sorted_alpha:
        print(f"The '{character['character']}' character was found '{character['count']}' times.")
    
    print(f"--- End report ---")

def get_text(file_path):
    """
    Reads the content of a file and returns it as a string.
    
    Args:
        file_path (str): Path to the file to read.
    
    Returns:
        str: Full text content of the file.
    """
    with open(file_path) as book_file:
        return book_file.read()

def get_word_count(text):
    """
    Counts the number of words in the given text.

    This function splits the input text into words using spaces and other whitespace characters as delimiters, then return the total word count.
    
    Args:
        text (str): The text content to be analyzed.
    
    Returns:
        int: The number of words in the text.
    """
    word_count = text.split()
    return len(word_count)

def get_character_counts(text):
    """
    Counts the times a character appears in a text.
    
    This function converts all characters to lower case to prevent duplicates, then loops over every character in the text and adds them to a dictionary where:
        - Keys are unique characters in the text.
        - Values are the counts of each character's occurence.
    
    Args:
        text (str): The text content to analyze.
        
    Returns:
        occurence (dict): Dictionary with characters as keys and counts as values.
    """
    lowered_text = text.lower()
    occurence = {}
    for character in lowered_text:
        if character in occurence:
            occurence[character] += 1
        else:
            occurence[character] = 1
    return occurence

def isalpha(occurence):
    """
    Filters the dictionary 'occurence' to retain only alphabetical characters.

    This function creates a new dictionary where:
        - Keys are alphabetical characters from 'occurence'.
        - Values are the counts of those characters.

    Args:
        occurence (dict): Dictionary with characters as keys and counts as values.

    Returns:
        alphabet (dict): Dictionary with characters as keys and counts as values.
    """
    alphabet = {}
    for character, count in occurence.items():
        if character.isalpha():
            alphabet[character] = count
    return alphabet

def sort_alpha(alphabet):
    """
    Sorts the alphabetical characters in descending order based on their count
    
    Args:
        alphabet (dict): Dictionary with characters as keys and counts as values.
        
    Returns:
        alphabet_list (lst): A list of dictionaries in following format: {"character": char, "count": number}.
    
    """
    alphabet_list = []
    for character, count in alphabet.items():
        alphabet_list.append({"character": character, "count": count})
    alphabet_list.sort(reverse=True, key=sort_on)
    return alphabet_list

def sort_on(alphabet_list):
    """
    Determines how a dictionary should be sorted.

    Args:
        alphabet (dict): Dictionary with characters as keys and counts as values.
    
    Returns:
        (int): The value that needs sorted.
    """
    return alphabet_list["count"]

main("books")