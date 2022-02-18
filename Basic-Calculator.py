name=input('\t \t \t \t \t Please enter your name:\t ')
print(f"Hello {name}, welcome to the calculator application")
while(True):
    o=input('Choose an option:\n a->Addition \n b->Subtraction \n c->Multiplication \n d->Division \n e->Modulus \n')
    a=int(input('Enter first number:'))
    b=int(input('Enter second number:'))
    if o=='a':
        print('Result is = ',a+b)
    elif o=='b':
        print('Result is = ',a-b)
    elif o=='c':
        print('Result is = ',a*b)
    elif o=='d':
        try:
            print('Result is = ',a/b)
        except Exception as e:
            print('0 cannot be entered as denominator, enter something else and try again.')
    elif o=='e':
        try:
            print('Result is = ',a%b)
        except Exception as e:
            print('0 cannot be entered as denominator, enter something else and try again.')