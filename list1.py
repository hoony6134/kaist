list=[]
count=1
for i in range(3):
    list.append([])
    for j in range(3):
        list[i].append(count)
        count+=1
print(list)
