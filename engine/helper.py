import os  # OS module for interacting with the operating system
import re  # Regular expressions for pattern matching
import time  # Time module for handling delays
def extract_yt_term(command):
    """
    Extracts the YouTube search term from a voice command.
    
    Args:
        command (str): The voice command containing the play request.
    
    Returns:
        str or None: Extracted search term if found, else None.
    """
    # Define a regular expression pattern to capture the song name
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    
    # Use re.search to find the match in the command
    match = re.search(pattern, command, re.IGNORECASE)
    
    # If a match is found, return the extracted song name; otherwise, return None
    return match.group(1) if match else None
def remove_words(input_string, words_to_remove):
    """
    Removes specified words from a given input string.
    
    Args:
        input_string (str): The original text.
        words_to_remove (list): List of words to be removed from the input string.
    
    Returns:
        str: The cleaned string with unwanted words removed.
    """
    # Split the input string into words
    words = input_string.split()

    # Remove unwanted words
    filtered_words = [word for word in words if word.lower() not in words_to_remove]

    # Join the remaining words back into a string
    result_string = ' '.join(filtered_words)
    
    return result_string
