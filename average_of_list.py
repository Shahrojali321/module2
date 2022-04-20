"""Defination:To find the average of numbers in a list."""
def average_list(lst,length):
    """To find the average of numbers in a list."""
    avg=sum(lst)/length
    return avg
lst=[]
length=int(input("Enter the length of list:"))
for i in range(0,length):
    element=int(input("Enter the number of the list:"))
    lst.append(element)
print(f"The list is :{lst}")
result=average_list(lst,length)
print(f"The average of the list is{result}")