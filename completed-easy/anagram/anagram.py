def find_anagrams(word, candidates):
    successful = []
    for candidate in candidates:
        anagram = True
        word_lower = word.lower()
        candidate_lower = candidate.lower()
        
        if len(candidate_lower) != len(word_lower): continue
        if candidate_lower == word_lower: continue
        for letter in candidate_lower:
            if letter not in word_lower:
                anagram = False
                break
            if letter in word_lower:
                word_lower = word_lower.replace(letter,"",1)
        if anagram: successful.append(candidate)
    return successful
