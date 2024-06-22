from itertools import combinations, combinations_with_replacement

#Session 18 Aug 2023 Complete
#Question 1 Solved
def calcSubset(A, res, subset, index):
    res.append(subset[:])
    for i in range(index, len(A)):
        subset.append(A[i])
        calcSubset(A, res, subset, i + 1)
        subset.pop()
def subsets(A):
    subset = []
    res = []
    index = 0
    calcSubset(A, res, subset, index)
    return res

def vSubset(arr):
    diff=float('inf')
    li=subsets(arr)
    li.remove([])
    for i in li:
        for j in li:
            if i==j:
                continue
            if abs(sum(i)-sum(j))<diff:
                diff=abs(sum(i)-sum(j))
            else:
                continue
    return diff
#arr=[97,12,19,90]
#vSubset(arr)
#Question 2 Solved
def funSum(a,b):
    return a+b-2*(a&b)
def result(a):
    sum=0
    for i in range(len(a)):
        sum+=funSum(funSum(a[i][1],a[i][2]),a[i],[0])
    return sum
'''a=list(combinations([1,1,2,3], 3))
result(a)'''
#Question 3 Solved Maybe
def intersection(a1,a2):
    temp=[]
    for i in a1:
        if i in a2 and i not in temp:
            temp.append(i)
    if temp==[]:
        return [-1]
    return temp
def heightB(a,u,v):
    n=len(a)
    res=[] 
    i=0
    while i!=len(u):
        temp1,temp2=[u[i]],[v[i]]
        for o in range(u[i],n):
            if a[u[i]-1]<a[o]:
                temp1.append(o+1)
        for o in range(v[i],n):
            if a[v[i]-1]<a[o]:
                temp2.append(o+1)
        i+=1
        res.append(intersection(temp1,temp2))
    ans=[]
    for i in res:
        ans.append(min(i))
    return ans
'''A=[1,3,2]
U=[1,3,2]
V=[2,1,3]
heightB(A,U,V)'''

#Session 5 Sep 2023 Complete
# #Question 3 solved
def maximize(n,A,B):
    val=''
    su=0
    temp=[]
    for i,j in A,B:
        t=pow(i,j)+pow(j,i)
        if t>9:
            while t!=0:
                su+=t%10
                t=t//10
            val+=str(su)
        else:
            val+=str(t)
    for i in val:
        temp.append(int(i))
    temp.sort(reverse=True)
    val=0
    for i in temp:
        val+=i
        val=val*10
    val=val//10
    return int(val)
'''A=[2,2]
B=[2,2]
maximize(2,A,B)
'''
#Question 2 Maybe solved
def computer(n,m,store,customer):
    a=0
    prof=0
    
    for i in store:
        pri=store[0][2]
        ind=0
        for j in customer:
            ind+=1
            if i[0]>=j[0] and i[1]>=j[1] :
                if pri<j[2]:
                    pri=j[2]
                    a=ind
        prof+=pri-i[2]
        customer.pop(a-1)
        store.pop(0)
    return prof
'''n=1
m=1
store=[[3,3253,744]]
customer=[[1,2012,798]]
computer(n,m,store,customer)'''
#Question 1 solved
def pattern(r,query):
    mod=1000000007
    b=[]
    for q in query:
        count=0
        res=[i for i in range(q,r+1)]
        a=combinations_with_replacement(res, 2)
        for i in a:
            if i[0]>=q and i[1]<=r:
                if i[0]<=i[1]:
                    lcm=compute_lcm(i[0],i[1])
                    if lcm>=q and lcm<=r:
                        count+=1
        b.append(count)
    if sum(b)>mod:
        return sum(b)%mod
    return sum(b)
    
def compute_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

#Session 8 Nov 2023
#Question 1
def subRev(Arr):
    return Arr.reverse()
def posOne(A,N,K,P,M):
    for i in range(N-K):
        if 1 in A[i:i+K]:
            pass
def operation(A,K,M,P,i):
    pass


#Question 2 Completed **Doubt
def special(Arr,N):
    Arr.reverse()
    ind=Arr.index(max(Arr))
    su=max(Arr)
    val=1
    
    for i in range(ind+1,N):
        val+=1
        a=ind
        if ind>=N-1:
            break
        for j in range(a,N):
            if sum(Arr[j:j+val])<su and j+val<=N:
                su=sum(Arr[j:j+val])
                ind=j+val
                break
    if val==1:
        return 1
    return val-1
'''N=4
A=[4,3,2,1]
special(A,N)'''

#Question 3 Tree graph Que***

#Session 16 Feb 2024
