def fix_caps_lock(word):
    if word.isupper():
        return ''.join(char.lower() for char in word)
    elif len(word) == 1 or (word[0].islower() and word[1:].isupper()):
        return word[0].upper() + ''.join(char.lower() for char in word[1:])
    else:
        return word

print(fix_caps_lock(input()))