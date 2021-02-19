print("...................welcome to advanced calculator........... \n ")
for i in range (1,100000000):
    print ("chose your option.....\n \n1. single number \n2. multiple number \n")

    u_i = int(input("type your option :- "))
    print ("")
    if u_i == 2:
        p = int (input ("type the power : "))
        def square_list(l):
            square = []
            for i in l:
                square.append(i**p)
            return square
        first_number = int(input ("please type your first number : "))
        second_number = int(input ("please type your last number : "))
        numbers = list (range(first_number, second_number + 1))
        print ("")
        print (square_list(numbers))
        print ("................................................................")
        input ("press Enter to continue ")
        print ("\n\n\n")
    else:
        p =  int(input ("type the power : "))
        n = int(input("type the number : "))
        r = n**p
        print ("")
        print (f"your answare is:- {r}" )
        print ("................................................................")
        input ("press Enter to continue ")
        print ("\n\n\n")
        




