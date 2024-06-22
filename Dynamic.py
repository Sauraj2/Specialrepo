#recursion
def fibo(num):
    if num<=2:
        return 1
    return fibo(num-1)+fibo(num-2)

def rec(num):
    if num==0:
        return
    print(num)
    return rec(num-1)

def dyna(num,memo):
    if num in memo:
        return memo[num]
    if num<=2:
        return 1
    memo[num]=dyna(num-1,memo)+dyna(num-2,memo)
    return memo[num]

def gridprob(m,n,memo):
    key=str(m) +','+str(n)
    if key in memo:
        return memo[key]
    if m==0 or n==0:
        return 0
    if m==1 and n==1:
        return 1
    memo[key]=gridprob(m-1,n,memo)+gridprob(m,n-1,memo)
    return memo[key]
#gridprob(18,18,{})

def canSum(target,list,memo):
    if target in memo:
        return memo[target]
    if target==0:
        return True
    if target<0:
        return False
    for i in range(len(list)):
        if canSum(target-list[i],list,memo)==True:
            memo[target]=True
            return True
    memo[target]=False
    return False

#confuse
def howSum(target,list,memo):
    if target in memo:
        return memo[target]
    if target==0:
        return []
    if target<0:
        return None
    for i in range(len(list)):
        rem=target-list[i]
        result=howSum(rem,list,memo)
        if result!=None:
            memo[target]= [*result,list[i]]
            return memo[target]
    memo[target]=None
    return None

def bestSum(target,list,memo):
    short=None
    if target in memo:
        return memo[target]
    if target==0:
        return []
    if target<0:
        return None
    for i in list:
        rem=target-i
        result=bestSum(rem,list,memo)
        if result!=None:
            comb=[*result,i]
            if short==None or (len(comb)<len(short)):
                short=comb
    memo[target]=short
    return short
#print(bestSum(8,[2,3,5],{}))

def canConst(target,words,memo):
    if target in memo:
        return memo[target]
    if target=='':
        return True
    for i in words:
        if i==target[:len(i)]:
            
            rem=target[len(i):]
            if canConst(rem,words,memo)==True:
                memo[target]==True
                return memo[target]
    memo[target]=False
    return False

#canConst('abcdef',['ab','abc','cd','def','abcd'],{})
#canConst('skateboard',['bo','rd','ate','t','ska','sk','boar'])
#canConst('enterapotentpot',['a','p','ent','enter','ot','o','t'])

def countConst(target,words,memo):
    count=0
    if target in memo:
        return memo[target]
    if target=='':
        return 1
    for i in words:
        if i==target[:len(i)]:
            result=countConst(target[len(i):],words,memo)
            count+=result
    memo[target]=count
    return count

#countConst('enterapotentpot',['a','p','ent','enter','ot','o','t'],{})

def minFallingPathSum(matrix):
    n=len(matrix[0])
    sum,res=0,0
    for i in range(1):
        for j in range(n):
            sum=matrix[i][j]
            mi=helper(matrix,i+1,j,sum)
            if res==0:
                res=mi
            res=min(res,mi)
    return res
def helper(martix,i,j,sum):
    sum1,sum2,sum3=0,0,0
    while i<len(martix):
        sum1+=martix[i][j]
        if j-1>=0:
            sum2+=martix[i][j-1]
        else:
            sum2+=max(martix[i])
        if j+1<len(martix):
            sum3+=martix[i][j+1]
        else:
            sum3=max(martix[i])
        i+=1
    sum+=min(sum1,sum2,sum3)
    return sum
        
    

#minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]])


