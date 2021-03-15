import stack 



def check_brackets(exp):
    """[THis function checks wheter the brackets are blanced or not]

    Args:
        exp ([String]): [The expresion whose brackets are to be checked]

    Returns:
        [Boolean]: [Wheter the expersiion is balnaced or not]
    """    
    st = stack.stack()
    for i in exp:
        if i == '(' or i == '{' or i == '[':
            st.push(i)
        elif i == ')':
            if st.is_empty():
                return False
            elif st.peek() != '(':
                return False
            st.pop()
        elif i == '}':
            if st.is_empty():
                return False
            elif st.peek() != '{':
                return False
            st.pop()        
        elif i == ']':
            if st.is_empty():
                return False
            elif st.peek() != '[':
                return False
            st.pop()
    
    return st.is_empty()



# s = input("Enter the expression")
print(check_brackets("{{(a+b+c)+b}"))
print(check_brackets("{(a+b+c)+b}"))
        





