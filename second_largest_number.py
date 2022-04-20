"""Defination:Find the second largest number from the list"""
def second_max(lst):
    new_list=set(lst)
    new_list.remove(max(new_list))
    return new_list

lst=[]
n=int(input("Enter the length of the the list:"))
for i in range(0,n):
    element=int(input("Enter the element of the list:"))
    lst.append(element)
print(f"The list is:{lst}")
result=second_max(lst)
max_number=max(result)
print(f"The Second largest number is: {max_number}")