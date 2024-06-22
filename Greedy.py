import bisect
from itertools import accumulate
import math


def greedy(num,n,k):
    son,f=0,0
    num.sort()
    if k<=n//2:
        f=sum(num[n-k:])
        son=sum(num[:n-k])
    else:
        f=sum(num[k:])
        son=sum(num[:k])
    
    return abs(f-son)

def maximumUnits(boxTypes,truckSize):
    ans=0
    boxTypes=sorted(boxTypes,key=lambda x:x[1],reverse=True)
    for i,j in boxTypes:
        if truckSize==0:break
        if truckSize>i:
            ans+=(i*j)
            truckSize-=i
        else:
            ans+=(truckSize*j)
            truckSize=0
    return ans

def maximumTime(time):
    time=time.split(':')
    for i in range(len(time)):
        for j in range(len(time[i])):
            if i==0:
                if time[i][0]=='?':
                    if time[i][1]=='?':
                        time[i]=time[i].replace('?','2',1)
                        continue
                    if int(time[i][1])<4:
                        time[i]=time[i].replace('?','2',1)
                    else:
                        time[i]=time[i].replace('?','1',1)
                    
                if time[i][1]=='?':
                    if int(time[i][0])==2:
                        time[i]=time[i].replace('?','3',1)
                    else:
                        time[i]=time[i].replace('?','9',1)
                    
            if i==1:
                if time[i][0]=='?':
                    time[i]=time[i].replace('?','5',1)
                    
                if time[i][1]=='?':
                    time[i]=time[i].replace('?','9',1)
                    
    
    return time[0]+':'+time[1]

def minOperations(nums):
    count=0
    for i in range(len(nums)-1):
        if nums[i]>=nums[i+1]:
            count+=nums[i]-nums[i+1]+1
            nums[i+1]+=nums[i]-nums[i+1]+1
    return count

def maximum69Number (num):
    ma=num
    temp=str(num)
    for i in range(len(temp)):
        temp=str(num)
        if temp[i]=='9':
            temp=int(temp[:i]+'6'+temp[i+1:])
            ma=max(ma,temp)
            continue
        elif temp[i]=='6':
            temp=int(temp[:i]+'9'+temp[i+1:])
            ma=max(ma,temp)
            continue
    return ma

def splitNum(num):
        st=str(num)
        temp=[]
        val1,val2=0,0
        for i in range(len(st)):
            temp.append(int(st[i]))
        temp.sort()
        n=len(temp)
        mid=n//2
        flag=False
        for i in range(mid):
            val1*=10
            val2*=10
            if flag==False:
                flag=True
                val1+=min(temp)
                temp.remove(min(temp))
                val2+=min(temp)
                temp.remove(min(temp))
                continue
            val1+=min(temp)
            temp.remove(min(temp))
            val2+=min(temp)
            temp.remove(min(temp))
        if temp!=[]:
            val1*=10
            val1+=min(temp)
            temp.remove(min(temp))
        return val1+val2

def minOperations(boxes):
    temp=[]
    target=0
    n=len(boxes)
    for target in range(n):
        count=0
        for i in range(target+1,n):
            if boxes[i]=='1':
                count+=i-target
        for j in range(0,target):
            if boxes[j]=='1':
                count+=target-j
        temp.append(count)
    return temp

def similarPairs(words):
    i=0
    n=len(words)
    count=0
    while i<n:
        for a in range(i,n):
            if a==i:
                continue
            if set(words[i])==set(words[a]):
                count+=1
        i+=1
    return count

def leftRightDifference(nums):
    temp=[]
    for i in range(len(nums)):
        value=0
        value+=sum(nums[:i])
        temp.append(value)
    
    for j in range(len(nums),0,-1):
        value=0
        value=sum(nums[j:])
        temp[j-1]=abs(temp[j-1]-value)
    return temp

def longestPalindrome(s) :
    count=0
    odd=0
    s=list(s)
    se=set(s)
    for i in se:
        if s.count(i)%2==1:
            count+=s.count(i)
            odd+=1
        else:
            count+=s.count(i)
    if odd!=0:
        count=(count-odd)+1
    return count

def canCompleteCircuit(gas, cost):
    diff=[]
    if sum(gas)<sum(cost):
            return -1
    n=len(gas)
    for i in range(n):
        diff.append(gas[i]-cost[i])
    res,total=0,0
    for i in range(n):
        total+=diff[i]
        if total<0:
            res=i+1
            total=0
    return res
#canCompleteCircuit([5,8,2,8],[6,5,6,6])

def candy(ratings):
    n=len(ratings)
    candy=[1]*n
    for i in range(n-1):
        if ratings[i]==ratings[i+1] :
            continue
        if ratings[i]<ratings[i+1]:
            candy[i+1]+=candy[i]
        else:
            if candy[i]<=candy[i+1]:
                candy[i]+=candy[i+1]
    for j in range(n-1,0,-1):
        if ratings[j]<ratings[j-1]:
            if candy[j]>=candy[j-1]:
                candy[j-1]=candy[j]+1
            else:
                continue
    return sum(candy)

def largestNumber(nums):
    nums[:]=map(str,nums)
    for i in range(len(nums)-1):
        for j in range(len(nums)-1):
            if int(nums[j]+nums[j+1])>int(nums[j+1]+nums[j]):
                continue
            else:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
    temp=''
    for i in nums:
        temp+=i     
    return temp

def canPlaceFlowers(flowerbed, n):
    le=len(flowerbed)
    a=0
    if le<n:
        return False
    if flowerbed[0]==0:
        if le==1:
            return True
        a=0
    else:
        a=1
    for i in range(a,le-1):
        if n==0:
            break
        if a==0 and i==0:
            if flowerbed[i+1]==0:
                flowerbed[i]=1
                n-=1
            continue
        if i==le-2:
            if flowerbed[i]==0 and flowerbed[i+1]==0:
                flowerbed[i+1]=1
                n-=1
                continue
        if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
            flowerbed[i]=1
            n-=1
            continue
    if n!=0:
        return False
    return True

def maxIncreaseKeepingSkyline(grid):
    #lst=[max(i) for i in zip(*grid)]
    #lst1=[max(i) for i in grid]
    height=0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            temp=adjustheight(grid,i,j)
            height+=(temp-grid[i][j])
            grid[i][j]=temp
    return height
def adjustheight(grid,h,v):
    ma1,ma2=0,0
    ma1=max(grid[h])
    for j in range(len(grid)):
        if ma2<grid[j][v]:
            ma2=grid[j][v]
    return min(ma1,ma2)

def minPatches(nums, n):
    reach,i=0,0
    count=0
    while reach<n:
        if i>len(nums):
            reach+=reach+1
            count+=1
        elif nums[i]<=reach+1 and i<len(nums):
            reach+=nums[i]
            i+=1
        else:
            reach+=reach+1
            count+=1
    return count

def increasingTriplet(nums):
    n1,n2=float('inf')
    for i in nums:
        if n1<i:
            n1=i
        elif n2<i:
            n2=i
        else: return True
    return False

def arrayPairSum(nums):
    nums.sort()
    su=0
    for i in range(0,len(nums),2):
        su=su+min(nums[i],nums[i+1])
    return su

def findMinArrowShots(points):
    n=len(points)
    points=sorted(points,key=lambda x:x[1])
    maxa=-float('inf')
    ans=0
    for i in range(0,n):
        if maxa<points[i][0]:
            ans+=1
            maxa=points[i][1]
    return ans

#Weird
def findMinMoves(machines):
    count=0
    n=len(machines)
    su=sum(machines)
    target=su//n
    dresses=0
    if su%n!=0:
        return -1
    for i in range(n):
        dresses+=machines[i]-target
        count=max(count,abs(dresses),machines[i]-target)
#findMinMoves([0,3,0])

def minSteps(s,t):
    d1={}
    d2={}
    count=0
    for i in s:
        if i in d1:
            d1[i]+=1
        else:
            d1[i]=1
    for i in t:
        if i in d2:
            d2[i]+=1
        else:
            d2[i]=1
    for i in d1.keys():
        if i in d2:
            if d1[i]>d2[i]:
                count+=d1[i]-d2[i]
        else:
            count+=d1[i]      
    return count

def longestOnes(nums,k):
    ma,t=0,-1
    c=-1
    temp=[]
    a=k
    count=0
    n=len(nums)
    if k==0:
        for i in range(n):
            if nums[i]==0:
                if ma<count:
                    ma=count
                count=0
            else:
                count+=1
        return ma

    for i in range(n):
        if a==0 and nums[i]==0:
            if ma<count:
                ma=count
            a+=1
            c=temp.pop(0)
            nums[c]=0
            if t==-1:
                count-=(c+1)
            else:
                count-=(c-t)
            t=c
        if nums[i]==0 and a!=0:
            nums[i]=1
            temp.append(i)
            a-=1
        if nums[i]==1:
            count+=1
    if count>ma:
        return count
    return ma

    '''l=r=0
    n=len(nums)
    for r in range(n):
        if nums[r]==0:
            k-=1
        if k<0:
            if nums[l]==0:
                k+=1
            l+=1
    return r-l+1'''


def countOperationsToEmptyArray(nums):
    n=len(nums)
    nums = [[nums[i], i] for i in range(len(nums))]
    nums.sort()
    ans,m=0,0
    for i in range(n):
        if i>0 and nums[i][1] < nums[i-1][1]:
            ans+=n-m
            m=i
    ans+=n-m
    return ans
    '''count=0
    while nums!=[]:
        if min(nums)==nums[0]:
            nums.pop(0)
            count+=1
        else:
            temp=nums.pop(0)
            nums.append(temp)
            count+=1
    return count'''

#queue(heap) need optimization
def minStoneSum(piles,k):
    ma=0
    ind=0
    for i in range(k):
        ind=piles.index(max(piles))
        ma=max(piles)
        ma-=(ma//2)
        piles[ind]=ma
        
    return sum(piles)
#problem bisect -binary
def minOperations(nums, queries):
    nums.sort()
    N = len(nums)
    res = []
    preSum = [0] + list(accumulate(nums))
    for q in queries:
        i = bisect.bisect_left(nums, q)
        res.append(q * i - preSum[i] + (preSum[-1] - preSum[i]) - q * (N - i))
        
    '''count=[]`
    c=0
    for i in range(len(queries)):
        c=0
        for j in range(len(nums)):
            c+=abs(nums[j]-queries[i])
        count.append(c)'''


