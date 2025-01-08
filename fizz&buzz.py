for i in range(1,101):
    if(i%5==0 and i%3==0):
        print("fizzbuzz")
    elif(i%5==0):
        print("buzzz")
    elif(i%3==0):
        print("fizzz")
    else:
        print(i)