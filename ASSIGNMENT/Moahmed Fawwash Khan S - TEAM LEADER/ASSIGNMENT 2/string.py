def concat(var1, var2):
    var3 = " ".join([var1, var2])
    print(var3)

def reverse(string):
    string = string[::-1]
    print(string)

def slic(string):
    s1 = slice(5,11) 
    print(string[s1])

print("Select operation.")
print("1.Concatenate two string")
print("2.Reverse the string")
print("3.Slice the string")
print("4.Break the program")

while True:
    choice = input("Enter choice(1/2/3/4): ")
    string = str(input("\nEnter the string: "))
    if choice in ('1', '2', '3', '4'):
        if choice == '1':
            str1 = str(input("Enter the second string. "))
            concat(string, str1)
        
        elif choice == '2':
            reverse(string)

        elif choice == '3':
            slic(string)

        elif choice == '4':
            break
    else:
        print("Invalid input")
