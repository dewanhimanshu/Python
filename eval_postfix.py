import stack

# Assumtion the postfix expression is correct otherwise error will occur

def eval_post(exp):
    """[This function evaluates the postfix expression]

    Args:
        exp ([String]): [This the postfix expression ]

    Returns:
        [String]: [The ans of expression after evaluation]
    """    
    st = stack.stack()
    exp = exp.split()
    for i in exp:
        if i.isdigit():
            st.push(i)

        else:
            op1 = st.pop()
            op2 = st.pop()
            st.push(str(eval(str(op2+i+op1))))
    return st.pop()



print(eval_post("22 3 1 ** + 9 - "))

#User input Use this
# print(eval_post(input("Enter the exp:")))
    