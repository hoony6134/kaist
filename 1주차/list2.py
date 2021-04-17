line1=input() # '10 2'를 입력
N, K=line1.split(" ")
N = int(N) #10
K = int(K) #2

line2=input()
list = line2.split(" ") #문자열로 나옴
for i in range(len(list)):
    list[i]=int(list[i]) #문자열 -> 숫자열로 전환
