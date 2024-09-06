import re

text = "foo   bar\t baz \tqux"

result = re.split(r"\s+", text)

print(result)


text = """
    Dave dave@google.com
    Steve steve@gmail.com
    Rob rob@gmail.com
    Ryan ryan@yahoo.com
"""

patter = r"([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})"
regex = re.compile(patter, re.IGNORECASE)

print(regex.findall(text))

print(regex.sub(r"Username: \1, Domain: \2, Suffix: \3", text))