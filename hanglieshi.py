print("copyright©2020 by Chen Chen")
print("this is a program to deal with hanglieshi!")
# n 是用于计录阶数的固定值
n = input("please input the jiesu of the hanglieshi")
n = int(n)
print("please input the aij and the j form 0 to n when the i is 0 then the i add 1 to n!")
hanglie = {}
hang = []
for i in range(0,n):
    for j in range(0,n):
        number = input()
        number = int(number)
        hang.append(number)
    print(hang)
    hanglie[i] = hang
    hang = []
#print(hanglie)
#print(hanglie[0][1]) 这两句只是为了检测是否录入成功

#以下22行到66行的内容目的是进行计算，计算方法是定义法，此外必须使用函数否则重用性差
#建立这三个参量，用于产生排列数
a = []
flag = []
ans = []
count = 0
list_ans = {}
for i in range(0,n):
    a.append(i+1)
    flag.append(0)
    ans.append(0)

#产生排列数的函数
def fun(a,flag,i,ans):
    global count
    if i == n-1:
        for j in range(0,n):
            if flag[j] == 0:
                ans[i] = a[j]
                print(ans)
                t = 0

                # 以下部分将会用于求逆序数t
                for k in range(1, n):
                    for k_ in range(0, k):
                        if ans[k_] > ans[k]:
                            t += 1

                # 以下部分用于给list_ans赋值
                list_ans[count] = []
                for k in range(0, n):
                    list_ans[count].append(ans[k])
                # 目的是留出让逆序数能放的地方
                if t % 2 == 0:
                    list_ans[count].append(1)
                else:
                    list_ans[count].append(-1)
                count += 1
                return
    else:
        for j in range(0,n):
            if flag[j] == 0:
                ans[i] = a[j]
                flag[j] = 1
                fun(a,flag,i+1,ans)
                flag[j] = 0

#借用以上产生的排列数将它们归结在i的顺排列之下，便于后面不断取值相乘
list_ij = {}
for i in range(0,n+1):#n+1的目的是留出让逆序数能放的地方
    list_ij[i] = []
#print(list_ij) #检验list_ij是否就位
a_1 = []
for i in range(0,n):
    a_1.append(i+1)
i = 0
fun(a_1,flag,i,ans)
#求n的阶乘，也就是排列的方式
m = 1
for k in range(1,n+1):
    m = m*k
for j in range(0,m):
    for i in range(0,n+1):#n+1的目的是留出让逆序数能放的地方
        list_ij[i].append(list_ans[j][i])

print(list_ans)
print(list_ij)
print(hanglie)

product = 1
sum_ = 0
for i in range(0,m):
    for j in range(0,n):
        k = list_ij[j][i]-1
        product *= hanglie[j][k]
    j += 1
    print(list_ij[j][i])
    product *= list_ij[j][i]#目的是乘上逆序数
    sum_ += product
    product = 1
print("最终结果是")
print(sum_)
