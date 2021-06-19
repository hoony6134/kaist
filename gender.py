#키와 몸무게로 성별 classification
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors, datasets
from sklearn import svm
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
file=open('gender_dataset.txt')

gender=[]
height=[]
weight=[]

for line in file.readlines():
    line = line.replace('\n', '')
    g,h,w = line.split('\t')
    gender.append(str(g))
    height.append(float(h))
    weight.append(float(w))
# print(gender)
# print(height)
# print(weight)
X=[]
for i in range(len(gender)):
    X.append([height[i],weight[i]])
y=gender
# print(X)
# print(y)
# plt.scatter(X[:,0], X[:,1], c=y, s=30, cmap=plt.cm.Paired)
k_fold=int(input("cross validation할 k_fold값: "))
new_X=[[] for i in range(k_fold)]
new_y=[[] for i in range(k_fold)]

#male
male_count=0
group=0
for i in range(len(gender)):
    if(y[i]=="Male"):
        male_count+=1
        new_X[group].append(X[i])
        new_y[group].append(y[i])
        if(male_count==int(len(gender)/2/k_fold)):
            male_count=0
            group+=1

#female
female_count=0
fgroup=0
for i in range(len(gender)):
    if(y[i]=="Female"):
        female_count+=1
        new_X[fgroup].append(X[i])
        new_y[fgroup].append(y[i])
        if(female_count==int(len(gender)/2/k_fold)):
            female_count=0
            fgroup+=1

# print(len(new_X[0]))

total_percentage=0
models = input("모델의 종류를 입력해주세요(linear,poly,lda,knn):")
for test_group in range(k_fold):
    # if(test_group!=0):continue
    train_X=[]
    train_y=[]
    test_X=[]
    test_y=[]
    for target_group in range(k_fold):
        if(target_group==test_group):
            test_X=new_X[target_group]
            test_y=new_y[target_group]
        elif(target_group!=test_group):
            train_X=train_X+new_X[target_group]
            train_y=train_y+new_y[target_group]
    # print(str("test group: ")+str(test_group))
    # print(len(test_X))
    # print(len(train_X)
    if models=="linear":
        clf = svm.SVC(kernel="linear") #svm_linear
    elif models=="poly":
        clf = svm.SVC(kernel="poly") #svm_poly
    elif models=="lda":
        clf = LinearDiscriminantAnalysis(n_components=1) #lda
    elif models=="knn":
        #knn start
        n_neighbors = 15
        for weights in ['uniform', 'distance']:
            # we create an instance of Neighbours Classifier and fit the data.
            clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
            clf.fit(X, y)
        clf.fit(train_X,train_y)
        #knn end
    else:
        models = input("오류 발생. 다시 시도해주세요.")
        break
    model_answer=clf.predict(test_X)

    total_count=0
    correct_count=0
    for i in range(len(model_answer)):
        total_count+=1
        if(model_answer[i]==test_y[i]):
            correct_count+=1
    percentage=correct_count/total_count*100
    total_percentage+=percentage
    print("테스트 그룹: "+str(test_group+1))
    print("정확도: "+str(percentage)+"% ("+str(correct_count)+"/"+str(total_count)+")\n")
total_percentage/=k_fold
print("----------------------------------------")
print("cross validation 전체 정확도: "+str(total_percentage)+"%")
print("----------------------------------------\n<키와 몸무게로 성별 예측>")
# ax = plt.gca()
# xlim = ax.get_xlim()
# ylim = ax.get_ylim()
# xx = np.linspace(xlim[0], xlim[1], 30)
# yy = np.linspace(ylim[0], ylim[1], 30)
# YY, XX = np.meshgrid(yy, xx)
# xy = np.vstack([XX.ravel(), YY.ravel()]).T
# Z = clf.decision_function(xy).reshape(XX.shape)
# ax.contour(XX, YY, Z, colors='k', levels=[-1,0,1], alpha=0.5, linestyles=['--', '-', '--'])
# ax.scatter(clf.support_vectors_[:,0], clf.support_vectors_[:,1], s=60, facecolors='r')
# plt.show()

while True:
    a,b = map(float,input("키와 몸무게 값을 공백 한 칸을 두고 입력해주세요: ").split(" "))
    newdata = [[a,b]]
    print(clf.predict(newdata))
