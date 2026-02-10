'''
String encoding can be a problem, especially with non-ASCII characters embedded in data 
being analyzed by Python. This module contains helpful encoding related functions.
'''

def replace_non_ascii_with_replacement_char(text):
    """
    Replaces non-ASCII characters in a string with the Unicode Replacement Character (U+FFFD).
    
    Args:
    text: The input string.
    
    Returns:
    A new string with non-ASCII characters replaced by U+FFFD.

    # Example usage:
        input_string = "This is a string with non-ASCII characters: é, ñ, ü, ©"
        output_string = replace_non_ascii_with_replacement_char(input_string)
        print(output_string)
    """
    # Encode to 'ascii' with 'replace' error handling to insert U+FFFD
    encoded_bytes = text.encode('ascii', 'replace')
    # Decode back to a string
    decoded_string = encoded_bytes.decode('ascii')
    return decoded_string