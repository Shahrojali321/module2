"""Defination:To count the occurrences of a particular element in the list"""
lst=[]
def count_element(lst,n):
    """occurrences of a particular element in the list"""
    for i in lst:
        if element==lst[i]:
            count = count +1
    return count
n=int(input("enter the size of the list:"))
for i in range(0,n):
    e=input("enter the element of the list:")
    lst.append(e)
print(f"the original list :{lst}")
element=input("enter the element which you wnat to count: ")
result = count_element(lst,n)
print(f"The {element} occours {result} times .")

