string = input().lower()

def replace_vowel(String):
    new_string = ""

    for i in String:
        if i not in "aeiouy":
            new_string += "."+ i

    return new_string

print(replace_vowel(string))
