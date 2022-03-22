from app import capital_dic

def check_answers(responses):
    message = ""
    for response in responses:
        if response in capital_dic:
            message.append(response + "----> Correct \n" )
        else:
            message.append(response + "----> Incorrect \n")
    return message