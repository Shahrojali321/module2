"""Defination:Python program which takes a sequence of numbers and check if all numbers are unique"""
flag = 0
def unique_number(test_list):
    """check if all numbers are unique"""
    for i in range(len(test_list)):
        for j in range(len(test_list)):
            if i !=j:
                if test_list[i] == test_list[j]:
                    flag = 1 
    if (not flag):
        print("List contains all unique element")
    else:
        print("List does not contain all unique element")  
    return test_list
#forming the list 
test_list=[]
n=int(input("Enter the length of the list:"))
for i in range(0,n):
    element=int(input("Enter the elements of list : "))
    test_list.append(element)
print(f'The list is: {test_list}')
result=unique_number(test_list)


