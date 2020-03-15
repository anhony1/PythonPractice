
# the question given says... Given an integer n, perform the following conditional actions...
# if n is odd, print weird
# if n is even and in the inclusive range of 2 to 5, print not weird
# if n is even and in the range of 6 to 20, print weird
# if n is even and greater than 20, print not weird


n = int(input("Enter a number!"))

value = n % 2

if value != 0:
    print("Weird")
elif value == 0 and n in range(3, 5):

    print("flag2")
    print("Not Weird")
elif value == 0 and n in range(6, 21):
    print("flag1")
    print("Weird")
elif n > 20:
    print("Not Weird")

    print("flag3")