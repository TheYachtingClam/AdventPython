def code_string(string_to_count):
    return len(string_to_count)


def value_string(string_to_count):
    string_without_quotes = string_to_count[1:-1]
    number_of_escaped_slashes = string_without_quotes.count("\\\\")
    number_of_escaped_quotes = string_without_quotes.count("\\\"")
    number_of_escaped_ascii = string_without_quotes.count("\\x")
    print("{0} - quotes={1} - slashes={2} - ascii's={3}".format(line.strip(), number_of_escaped_quotes, number_of_escaped_slashes, number_of_escaped_ascii))
    return len(string_without_quotes) - \
           number_of_escaped_slashes - \
           number_of_escaped_quotes - \
           number_of_escaped_ascii * 3


f = open("realInput.txt")
code_chars = 0
value_chars = 0
for line in f:
    code_chars += code_string(line.strip())
    value_chars += value_string(line.strip())
    print("{0} - code={1} - value={2}".format(line.strip(), code_string(line.strip()), value_string(line.strip())))

print("code_chars = {0}".format(code_chars))
print("value_chars = {0}".format(value_chars))
print("answer = {0}".format(code_chars - value_chars))
