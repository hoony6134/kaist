def func(i):
    if(i==0):
        return 0
    return i+func(i-1)
sum = func(int(input("1부터 더할 숫자 입력: ")))
print("1부터",,"까지 더한 수는")
#재귀호출

'''
sum=0
for i in range(9,-1,-1):
    sum+=1
print(sum)
'''
# iterative
