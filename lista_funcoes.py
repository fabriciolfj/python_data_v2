import re


def remove_punctuation(text):
    return re.sub("[!#?]", "", text)


def clear_strings(strings, ops):
    result = []
    for string in strings:
        for op in ops:
            string = op(string)
        result.append(string)

    return result


clean_ops = [str.strip, remove_punctuation, str.title]
states = [" Alabama", "Georgia!", "geogia", "fLoriDa", "south carolina##"]

result = clear_strings(states, clean_ops)
print(result)
