def answer(question):
    
    if not question.startswith("What is"):
        raise ValueError("unknown operation")
    if not question.startswith("What is "):
        raise ValueError("syntax error")
    
    question_in_list = question[:-1].split()[2:]
    
    num_a = question_in_list.pop(0)
    
    if not num_a.isnumeric():        
        try:
            num_a = int(num_a)
        except:
            raise ValueError("syntax error")
    
    operations = ["plus", "minus", "multiplied", "divided"]
    
    while len(question_in_list) > 0:
    
        operation = question_in_list.pop(0)
        if operation.isnumeric():
            raise ValueError("syntax error")
        if not operation in operations:
            raise ValueError("unknown operation")
        if operation == "multiplied" or operation == "divided":
            try:
                by = question_in_list.pop(0)
                if by != "by":
                    raise ValueError("syntax error")
            except:
                raise ValueError("syntax error")
        
        try:
            num_b = question_in_list.pop(0)
        except:
            raise ValueError("syntax error")
            
        if not num_b.isnumeric():
            try:
                num_b = int(num_b)
            except:
                raise ValueError("syntax error")
            
        num_c = 0
        if operation == "plus":
            num_c = int(num_a) + int(num_b)
        if operation == "minus":
            num_c = int(num_a) - int(num_b)
        if operation == "multiplied":
            num_c = int(num_a) * int(num_b)
        if operation == "divided":
            num_c = int(num_a) / int(num_b)
        
        num_a = num_c

    return int(num_a)
