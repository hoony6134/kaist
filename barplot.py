import matplotlib.pyplot as plt
file=open("input.txt", "r")
day=[]
number=[]
title=input("그래프의 제목을 입력하세요: ")
xlabel=input("x축의 제목을 입력하세요: ")
ylabel=input("y축의 제목도 입력하세요: ")

for line in file.readlines():
    line=line.replace('\n','') #두칸 띄어짐 방지
    input_day, input_number = line.split(' ') #스페이스바 기준으로 이전/이후 값 구분
    day.append(input_day)
    number.append(int(input_number)) #숫자로 인식

#plt.figure(figsize=(10,10))
plt.bar(day,number)
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.show()

#plt.savefig("/Users/limjeonghoon/PycharmProjects/pythonProject1/graph.png")