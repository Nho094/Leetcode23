def process_strings(s):
    vowels = "aeiouAEIOUYy"
    result = ""

    for char in s:
        if char not in vowels:
            result += "." + char.lower()

    return result


print(process_strings(input()))