def count_words(text):
    """
    Counts the number of words in a given text.

    Args:
        text: The input text string.

    Returns:
        The number of words in the text.
    """

    # Split the text into a list of words using whitespace as the delimiter
    words = text.split()

    # Count the number of words in the list
    word_count = len(words)

    return word_count

# Get user input
text = input("Enter a sentence or paragraph: ")

# Count the words
word_count = count_words(text)

# Display the output
print("Number of words:", word_count)m