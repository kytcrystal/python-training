def reverse(text):
    original = list(text)
    reverse = ""
    while len(original) > 0:
        reverse += original.pop()
    return reverse