list=[]
for i in range(int(input())):
    name = input()
    score = float(input())
     
    list.append(name)
    list.append(score)

    # if score > (list[i])[1]:
    #     value = 
    #     listsorted.append
    
def minima():    
    mini = list[1]
    for i in range(1,len(list),2):
        if list[i] < mini:
            mini=(list[i])
    return mini 
mi = minima()          
# list.remove(mi)


while mi == minima():
    for i in range(1,len(list),2):
        if list[i] == mi:   
            list.pop(i)
            list.pop(i-1)
            break    
newlist=[]
mi = minima()
while mi == minima():
    for i in range(1,len(list),2):
        if list[i] == mi:   
            newlist.append(list[i-1])  
    break
newlist.sort()
for i in range(0,len(newlist)):
    print(newlist[i])
    









# print(minima()) 
# mi = minima()       
# while mi == minima():
#     for i in range(1,len(list),2):
#         if list[i-1] == mi:   
#             list.remove(i-1)
#             list.remove(i-2)
#             break
             
    
# print(list)    


# print(minima())        


