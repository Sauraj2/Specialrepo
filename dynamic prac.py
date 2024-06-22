def fib(num,memo):
    if num in memo:
        return memo[num]
    if num<=2:
        return 1
    memo[num]= fib(num-1,memo)+fib(num-2,memo)
    return memo[num]

def gridTravel(x,y,memo):
    key=str(x)+','+str(y)
    if key in memo:
        return memo[key]
    if x==0 or y==0:
        return 0
    if x==1 and y==1:
        return 1
    memo[key]= gridTravel(x-1,y,{})+gridTravel(x,y-1,{})
    return memo[key]

def canSum(target,num,memo):
    if target in memo:
        return memo[target]
    if target==0:
        return True
    if target<0:
        return False
    for i in num:
        if canSum(target-i,num,{})==True:
            memo[target]=True
            return True
    memo[target]=False
    return False

def howSum(target,num,memo):
    if target in memo:
        return memo[target]
    if target==0:
        return []
    if target<0:
        return None
    for i in num:
        rem=target-i
        result=howSum(rem,num)
        if result!=None:
            memo[target]=[*result,i]
            return memo[target]
    memo[target]=None
    return None

def bestSum(target,num,memo):
    short=None
    if target in memo:
        return memo[target]
    if target==0:
        return []
    if target<0:
        return None
    for i in num:
        rem=target-i
        result=bestSum(rem,num,memo)
        if result!=None:
            comb=[*result,i]
            if short==None or (len(short)>len(comb)):
                short=comb
    memo[target]=short
    return short
bestSum(7,[7,5,3,4],{})