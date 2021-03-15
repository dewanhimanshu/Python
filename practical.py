def pattern1(n,patternType):
    """[To print a pattern 1 ]
    

    Args:
        n ([int]): [number of rows]
        patternType
    """    
    if patternType == '1':
        count = 1
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(count*count,end=' ')
                count = count + 1
            print()
    elif patternType == '2':
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(i,end='')
            print()
    else:
        print("Wrong Input")
    





n = int(input("ENter the number of rows for pattern :"))
patternType = input("Enter the patter type(Valid input is 1 and 2 only:")
pattern1(n,patternType)




