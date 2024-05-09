def answer(question):
    
    if not question.startswith("What is"):
        raise ValueError("unknown operation")
    question = question.removeprefix("What is").removesuffix("?")
    if not question: 
        raise ValueError("syntax error")
    question_in_list = question.split()
    
    lhs_num = retrieve_next(question_in_list)
    lhs_num = convert_string_to_int(lhs_num)
    
    operations = ["plus", "minus", "multiplied", "divided"]
    
    while len(question_in_list) > 0:
    
        operation = retrieve_next(question_in_list)
        if not operation.isalpha():
            raise ValueError("syntax error")
        if not operation in operations:
            raise ValueError("unknown operation")
        if operation == "multiplied" or operation == "divided":
            by_word = retrieve_next(question_in_list)
            if by_word != "by":
                raise ValueError("syntax error")
        
        rhs_num = retrieve_next(question_in_list)
        rhs_num = convert_string_to_int(rhs_num)
            
        result = evaluate(lhs_num, operation, rhs_num)
        lhs_num = result

    return lhs_num

def retrieve_next(question_in_list):
    try:
        item = question_in_list.pop(0)
    except:
        raise ValueError("syntax error")
    return item

def convert_string_to_int(num):
    if not num.isnumeric():        
        try:
            num = int(num)
        except:
            raise ValueError("syntax error")
    return int(num)

def evaluate(lhs_num, operation, rhs_num):
    match operation:
        case "plus":
            return lhs_num + rhs_num
        case "minus":
            return lhs_num - rhs_num
        case "multiplied":
            return lhs_num * rhs_num
        case "divided":
            return lhs_num / rhs_num