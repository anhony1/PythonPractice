# Create a program that asks the user for his birthday in the format "DD-MM-YYYY" and then tells you which month you
# were born in

print("Please enter your birthday in the format MM-DD-YYYY")
birthday = input()

months = ("Jan", "Feb", "Mar", "Apr", "May", "June", "Aug", "Sept", "Oct", "Nov", "Dec")



index = int(birthday[3:5]) - 1
bd_month = months[index]


print("The month you were born in is", bd_month)