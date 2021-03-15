import stack

def priority(operater):
    """[THis function returns the priority of operater]

    Args:
        operater ([String]): [operater]

    Returns:
        [int]: [priority]
    """
    if operater == '**':
        return 3

    if operater == '+':
        return 1
    elif operater == '-':
        return 1
    elif operater == '*':
        return 2
    else:
        return 2


def infix_to_postfix(exp):
    """[This converts thr infix operation to postfix expression]

    Args:
        exp ([String]): [Infix operation]

    Returns:
        [String]: [Postfix operation]
    """    
    operater_stack = stack.stack()
    operands_stack = stack.stack()
    exp = exp.split()
    for i in exp:
        if i.isdigit():
            operands_stack.push(i)
        else:
            if i == '(':
                operater_stack.push(i)
            elif i == ')':
                while operater_stack.peek() != '(':  
                    v2 = operands_stack.pop()
                    v1 = operands_stack.pop()
                    op = operater_stack.pop()
                    #postfix_exp += v1 + v2 + op
                    operands_stack.push(str(v1+" " + v2+" " + op+" "))

                
                operater_stack.pop()
            else:
                while(operater_stack.get_size() != 0 and operater_stack.peek()!='(' and priority(i) <= priority(operater_stack.peek())):
                    v2 = operands_stack.pop()
                    v1 = operands_stack.pop()
                    op = operater_stack.pop()
                    #postfix_exp += str(v1 + v2 + op)
                    operands_stack.push(str(v1+" " + v2+" " + op+" "))
                operater_stack.push(i)

    while operater_stack.get_size() != 0:
        v2 = operands_stack.pop()
        v1 = operands_stack.pop()
        op = operater_stack.pop()
        operands_stack.push(str(v1+" " + v2+" " + op+" "))
        #postfix_exp += str(v1 + v2 + op)

    return  operands_stack.peek()



print(infix_to_postfix("22 + ( 3 / 4 ) ** 5"))
#User Input
# print(infix_to_postfix(input("Enter the expression")))

