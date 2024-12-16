def last_char_of_string(s):
    if s:
        return s[-1]
    else:
        return ""  # Return an empty string for empty input

if _name__ == "__main__":
    a_string = input("Enter a string: ")  # Change to input() to read as string
    last_char = last_char_of_string(a_string)  # Corrected variable name
    if last_char:
        print("The last character of the string is:", last_char)  # Add comma
    else:
        print("The string is empty.")
