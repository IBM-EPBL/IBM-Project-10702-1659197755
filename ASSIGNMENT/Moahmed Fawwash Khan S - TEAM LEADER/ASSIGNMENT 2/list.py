def insert(list1, ind, element):
    list1.insert(ind, element)

def prin(list1):
    print(list1)
    
def remove(list1,element):
    list1.remove(element)

def append(list1,element):
    list1.append(element)

def sort(list1):
    list1.sort()

def pop(list1):
    list1.pop()

def reverse(list1):
    list1.sort(reverse = True)



print("Select operation.")
print("1.Insert an element")
print("2.Print the list")
print("3.Remove an element")
print("4.Append an element")
print("5.Sort the list")
print("6.Pop the last element")
print("7.Sort the list in reverse order")
print("8.Break the program")
list1 = [1,2,3,4,5,6,7,8,9,10]

while True:
    
    choice = input("\nEnter choice(1/2/3/4/5/6/7): ")
    if choice in ('1', '2', '3', '4', '5', '6', '7', '8'):

        if choice == '1':
            a = int(input("Enter the index which the element is to be added: "))
            b = int(input("Enter the number to be added in the list"))
            insert(list1, a, b)
            
        elif choice == '2':
            prin(list1)
            
        elif choice == '3':
            a = int(input("Enter the number to be removed from the list"))
            remove(list1, a)
            
        elif choice == '4':
            a = int(input("Enter the number to be appended to the list"))
            append(list1, a)
            
        elif choice == '5':
            print("Sorting the list...")
            sort(list1)
            
        elif choice == '6':
            print("Poping the last element...")
            pop(list1)
            
        elif choice == '7':
            print("Sorting the list in reverse order...")
            reverse(list1)
            
        elif choice == '8':
            break
    else:
        print("Invalid input...\n")
