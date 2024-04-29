def response(hey_bob):
    hey_bob = hey_bob.strip()
    if hey_bob.isupper():
        if hey_bob.endswith("?"):
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    elif hey_bob.endswith("?"):
        return "Sure."
    elif len(hey_bob) == 0:
        return "Fine. Be that way!"
    return "Whatever."
