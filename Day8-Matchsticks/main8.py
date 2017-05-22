def code_string(string_to_count):
    return len(string_to_count)

def encode_string(string_to_encode):
    modified_string = "\"";
    for char in string_to_encode:
        if char == "\\":
            modified_string += "\\\\"
        elif char == "\"":
            modified_string += "\\\""
        else:
            modified_string += char
    modified_string += "\""
    return modified_string


def decode_string(string_to_count):
    escape_mode = False
    ascii_escape = 0
    modified_string = ""

    number_of_escaped_slashes = 0
    number_of_escaped_quotes = 0
    number_of_escaped_ascii = 0

    for char in string_to_count[1:-1]:
        if not escape_mode:
            if char == "\\":
                escape_mode = True
            else:
                modified_string += char
        elif escape_mode and ascii_escape > 0:
            ascii_escape -= 1
            if ascii_escape == 0:
                escape_mode = False
                modified_string += "A"
        else:
            if char == "\\":
                modified_string += "\\"
                number_of_escaped_slashes += 1
                escape_mode = False
            elif char == "\"":
                modified_string += "\""
                number_of_escaped_quotes += 1
                escape_mode = False
            elif char == "x":
                ascii_escape = 2
                number_of_escaped_ascii += 1
            else:
                escape_mode = False

    return modified_string

    number_of_escaped_slashes = modified_string.count("\\\\")
    modified_string = modified_string.replace("\\\\", "\\")
    number_of_escaped_quotes = modified_string.count("\\\"")
    modified_string = modified_string.replace("\\\"", "\"")
    number_of_escaped_ascii = modified_string.count("\\x")
    ''''print("{0} - quotes={1} - slashes={2} - ascii's={3}".format(modified_string, number_of_escaped_quotes, number_of_escaped_slashes, number_of_escaped_ascii))
    return len(string_to_count[1:-1]) - \
           number_of_escaped_slashes - \
           number_of_escaped_quotes - \
           number_of_escaped_ascii * 3'''


def new_string(string_to_convert):
    string_without_quotes = string_to_convert[1:-1]
    string_with_escaped_quotes = string_without_quotes.replace("\\\"", "\"")
    string_with_escaped_slashes = string_with_escaped_quotes.replace("\\\\", "\\")
    return string_with_escaped_slashes

f = open("realInput.txt")
code_chars = 0
value_chars = 0
encoded_chars = 0
for line in f:
    code_chars += code_string(line.strip())
    value_chars += len(decode_string(line.strip()))
    encoded_chars += len(encode_string(line.strip()))
    print("{0}\n{1}\n - code={2} - value={3}".format(line.strip(), decode_string(line.strip()), code_string(line.strip()), len(decode_string(line.strip()))))

print("code_chars = {0}".format(code_chars))
print("value_chars = {0}".format(value_chars))
print("answer = {0}".format(code_chars - value_chars))
print("answer2 = {0}".format(encoded_chars - code_chars))
