list =[5,3,8,1,9]
n= len(list)
print(n)
for i in list :
    print(i,end=" ")  
list.insert(2,7)
print("\n")
print(list)
list.pop(1)
print(list)
def serach (list,x):
    for i in range (n):
        if list[i] == x:
            return i
print(serach(list,8))
list.insert(3,10)
print(list)
