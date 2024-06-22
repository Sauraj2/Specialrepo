def subarrayBitwiseORs(arr):
    res = set()
    main = set()

    for a in arr:
        local = set()
        local.add(a)
        for b in main:
            local.add(b|a)
        main = local
        res |= main
        
    return len(res)

def longestSubarray(nums):
    i=0
    count=0
    siz=0
    for j in range(len(nums)):
        if nums[j]==0:
            count+=1
        while count>1:
            if nums[i]==0:
                count-=1
            i+=1
        siz=max(siz,j-i)
    return siz

def unmarkedSumArray(nums,queries):
    temp=sorted(nums)
    res=[]
    mark=[0 for i in range(len(nums))]
    qc=0
    for i,j in queries:
        su=0
        if mark[i]==0:
            temp.remove(nums[i])
        mark[i]=1
        so=0
        if j<mark.count(0):
            while so<j:
                for a in range(len(nums)):
                    if temp[0]==nums[a] and mark[a]==0:
                        temp.remove(temp[0])
                        mark[a]=1 
                        so+=1
                    if so==j:
                        break
            for z in range(len(mark)):
                if mark[z]==0:
                    su+=nums[z]
            res.append(su)
        else:
            for i in range(qc,len(queries)):
                res.append(0)
            return res
        qc+=1
    return res
#unmarkedSumArray([16,16,16,7,14,2,2,16],[[0,2],[1,3],[7,0],[3,0],[4,4],[5,3]])

def bottle(numBottles,numExchange):
    modu,emp=1,0
    res=numBottles
    while modu!=0:
        emp=numBottles%numExchange
        modu=numBottles//numExchange
        numBottles=emp+modu
        res+=modu
    return res

def resultArray(nums):
    a=1
    last=nums[1]
    temp=[]
    temp.append(nums[0])
    temp.append(nums[1])
    for i in range(2,len(nums)):
        if last<temp[a-1]:
            temp.insert(a,nums[i])
            a+=1
        else:
            temp.append(nums[i])
            last=nums[i]
    return temp

def minimumPushes(word):
    a=set(word)
    temp={}
    c=2
    multi=1
    res=0
    for i in a:
        temp[i]=word.count(i)
    temp=sorted(temp.items(),key=lambda x:x[1],reverse=True)
    for i in temp:
        if c==10:
            multi+=1
            c=2
        res+=(i[1]*multi)
        c+=1
    return res

def commonChars(words):
    dic={}
    c=1
    res=[]
    n=len(words)
    for i in set(list(words[0])):
        dic[i]=[words[0].count(i)]
    for a in words[1:]:
        for b in set(list(a)):
            if b in dic.keys():
                dic[b].append(words[c].count(b))
        c+=1
    for k,v in dic.items():
        if len(dic[k])==n:
            for i in range(0,min(v)):
                res.append(k)
    return res

def longestCommonSubsequence(text1, text2):
    l1=len(text1)
    l2=len(text2)
    dp_matrix=[[0]*(l2+1) for _ in range(l1+1)]
    
    for i in range(1,l1+1):
        for j in range(1,l2+1):
            if text1[i]==text2[j]:
                dp_matrix[i][j]=dp_matrix[i-1][j-1]+1
            else:
                dp_matrix[i][j]=max(dp_matrix[i-1][j],dp_matrix[i][j-1])
    return dp_matrix[l1][l2]

def numRescueBoats(people, limit):
    people.sort()
    x=0
    l=0
    r=len(people)-1
    while l<=r:
        x+=1
        if people[l]+people[r]<=limit:
            l+=1
        r-=1
    return x

def checkPowersOfThree(n):
        temp=n
        while temp!=1:
            if temp%3==2:
                return False
            temp=temp//3
        return True

def minimumSteps(s):
    cot=0
    s=list(s)
    for i in range(len(s)):
        if s[i]=='0':
            while s[i-1]=='1' and i>0:
                s[i],s[i-1]=s[i-1],s[i]
                i-=1
                cot+=1
    return cot
import copy
def gameOfLife(board):
    temp=copy.deepcopy(board)
    cont=0
    for i in range(len(board)):
        for j in range(len(board[i])):
            cont=0
            cont+=checkBox(i+1,j,temp)
            cont+=checkBox(i-1,j,temp)
            cont+=checkBox(i,j+1,temp)
            cont+=checkBox(i,j-1,temp)
            cont+=checkBox(i+1,j+1,temp)
            cont+=checkBox(i-1,j-1,temp)
            cont+=checkBox(i-1,j+1,temp)
            cont+=checkBox(i+1,j-1,temp)
            if board[i][j]==1:
                if cont<2:
                    board[i][j]=0
                elif cont>=2 and cont<=3:
                    board[i][j]=1
                elif cont>3:
                    board[i][j]=0
            elif board[i][j]==0:
                if cont==3:
                    board[i][j]=1    
def checkBox(i,j,board):
    if i>=0 and j>=0 and i<len(board) and j<len(board[0]):
        if board[i][j]==1:
            return 1
        else:
            return 0
    else:
        return 0

def letterCombinations(digits):
    if not digits:
            return []
    temp=[]
    dic={
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'
    }
    def backT(comb,nextd):
        if not nextd:
            temp.append(comb)
            return
        for letter in dic[nextd[0]]:
            backT(comb+letter,nextd[1:])
    backT('',digits)
    return temp

def jump(nums):
    jumps = 0
    cur_max_reach = 0
    next_max_reach = 0
    
    for i in range(len(nums) - 1):
        next_max_reach = max(next_max_reach, i + nums[i])
        if i == cur_max_reach:
            jumps += 1
            cur_max_reach = next_max_reach
            
    return jumps
#jump([2,3,1,1,4])

def maxSlidingWindow(nums, k):
    temp=[]
    i=k
    n=len(nums)
    sta=nums[:k]
    while i<=n:
        temp.append(max(sta))
        sta.pop(0)
        if i<n:
            sta.append(nums[i])
        i+=1
    return temp
from collections import deque
#maxSlidingWindow([1],1)
def convertToTitle(columnNumber):
    output = ""
    while columnNumber>0:
        output=chr(ord('A')+(columnNumber-1)%26)+output
        columnNumber=(columnNumber-1)//26
    return output




