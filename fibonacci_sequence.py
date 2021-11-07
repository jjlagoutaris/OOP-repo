def fibonacci_sequence():
    nterms = int(input("To how many digits would you like the sequence? "))
    n1, n2 = 0, 1
    count = 0
    if nterms <= 0:
        print("Enter a positive integer. ")
    elif nterms == 1:
        print(n1)
    else:
        while count < nterms:
            print(n1)
            nth = n1+n2
            n1 = n2
            n2 = nth
            count += 1
