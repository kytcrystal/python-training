def count_words(sentence):
    punc = '''!()-[]{};:"\,<>./?@#$%^&*_~'''
    for ele in sentence:
        if ele in punc:
            sentence = sentence.replace(ele, " ")
    sentence_list = sentence.lower().split()
        
    mapping = {}
    for word in sentence_list:
        word = word.strip("'")
        if word in mapping:
            mapping[word] += 1
        elif len(word) > 0:
            mapping[word] = 1
    return mapping
