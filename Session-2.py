def minOperations(s):
    conut=0
    c=0
    for a in range(2):
        c=conut
        conut=0
        temp=list(s)
        if a==1:
            conut+=1
            if temp[0]=='1':
                temp[0]='0'
            else:
                temp[0]='1'
        for i in range(len(s)-1):
            if temp[i]=='1':
                if temp[i+1]=='0':
                    continue
                else:
                    temp[i+1]='0'
                    conut+=1
                    continue
            if temp[i]=='0':
                if temp[i+1]=='1':
                    continue
                else:
                    temp[i+1]='1'
                    conut+=1
    if c<conut:
        return c
    return conut        

def maxOperations(nums, k):
    temp=nums[:]
    a=0
    i=0
    val=0
    count=0
    while  i <len(temp):
        a=k-temp[i]
        val=temp[i]
        temp.remove(temp[i])
        if temp.count(a)>0:
            temp.remove(a)
            count+=1
            continue
        temp.insert(i, val)
        i+=1
    return count
#optimized
    '''num_counts={}
        count=0
        for num in nums:
            complement=k-num
            if complement in num_counts and num_counts[complement]>0:
                count+=1
                num_counts[complement]-=1
            else:
                num_counts[num]=num_counts.get(num,0)+1

        return count'''

def countBits(n) :
    temp=[]
    for i in range(n+1):
        temp.append(bin(i).count('1'))
    return temp

def maxVowels(s,k):
        vowels = 'aeiou'
        l=0
        r=k
        m=0
        count=0
        for i in range(k):
            if s[i] in vowels:
                count+=1
        m=max(m,count)
        while r<len(s):
            if s[l] in vowels:
                count-=1
            if s[r] in vowels:
                count+=1
            m=max(m,count)
            l+=1
            r+=1
        return m

def singleNumber(nums):
    for i in nums:
        if nums.count(i)<1:
            return i
        
def makeEqual(words):
    a={}
    for i in words:
        for j in i:
            a[j]=a.get(j,0)+1
    n=len(words)
    for val in a.values():
        if val%n!=0:
            return False
    return True

def maxLengthBetweenEqualCharacters(s):
    ans=-1
    for i in range(len(s)):
        if s.count(s[i])>1:
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    ans=max(ans,j-i-1)
                    
    return ans

def findContentChildren(g,s):
    ans=0
    g.sort()
    s.sort()
    for i in range(len(g)):
        for j in range(len(s)):
            if g[i]<=s[j]:
                ans+=1
                s.remove(s[j])
                break
                
    return ans

def guessNumber(n,pick) :
    l=0
    r=n
    
    while l<=r:
        m=(r+l)//2
        if gNumber(m,pick)==0:
            return m
        elif gNumber(m,pick)==-1:
            r=m-1
        else:
            l=m+1
def gNumber(n,pick):
    if n==pick:
        return 0
    elif n>pick:
        return -1
    else:
        return 1

def compress(chars):
    temp=[]
    cont=1
    if len(chars)==1:
        return len(chars)
    for i in range(len(chars)-1):
        if chars[i]==chars[i+1]:
            cont+=1
        else:
            temp.append(chars[i])
            if cont!=1:
                if cont<=9:
                    temp.append(str(cont))
                else:
                    for j in str(cont):
                        temp.append(j)
            cont=1
    temp.append(chars[len(chars)-1])
    if cont!=1:
        if cont<=9:
            temp.append(str(cont))
        else:
            for j in str(cont):
                temp.append(j)
    z=0
    for a in range(len(chars)):
        if a<len(temp):
            chars[a]=temp[a]
            z+=1
        else:
            del chars[z]
    return len(chars)

def findMatrix(nums):
    
    final=[]
    while len(nums)!=0:
        temp=[]
        for i in range(len(nums)):
            if nums[i] not in temp:
                temp.append(nums[i])
        for i in temp:
            nums.remove(i)
        final.append(temp)
    return final
                
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def oddEvenList(head) :
    odd=head
    evenhead=even=head.next

    while even and even.next:
        odd.next=odd.next.next
        odd=odd.next
        
        even.next=even.next.next
        even=even.next
        
    odd.next=evenhead
    return head

def minCost(colors, neededTime):
    time=0
    flag=False
    a=0
    for i in range(len(colors)-1):
        if colors[i]==colors[i+1]: 
            if flag==True:
                time+=min(a,neededTime[i+1])
                a=max(a,neededTime[i+1])
                flag=True
                continue
            time+=min(neededTime[i],neededTime[i+1])
            a=max(neededTime[i],neededTime[i+1])
            flag=True
            continue
        flag=False
    return time

def numberOfBeams(bank):
    ans,temp=0,0
    for i in bank:
        n=i.count('1')
        if n==0:
            continue
        ans+=temp*n
        temp=n
    return ans


def minOperations(nums):
    
    temp={}
    count=0
    for i in nums:
        temp[i]=temp.get(i,0)+1
    for a in temp:
        while temp[a]>0:
            count+=1
            if temp[a]==1:
                return -1
            if temp[a]%3==0:
                temp[a]-=3
                continue
            else:
                temp[a]-=2
    return count

def lengthOfLIS(nums):
    if not nums:
        return 0    
    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

#lengthOfLIS([10,9,2,5,3,7,101,18])

def binarySearch(nums,find):
    l=0
    r=len(nums)
    while l<=r:
        mid=(l+(r-1))//2
        if nums[mid]==find:
            return mid
        elif nums[mid]<find:
            l=mid+1
        else:
            r=mid-1
    return -1

#binarySearch([1,2,6,8,9,19,31,33,90],33)

def validSquare(p1, p2, p3, p4):
    if p1==p2==p3==p4:return False
    def dist(point1,point2):
        return (point1[0]-point2[0])**2+(point1[1]-point2[1])**2
    D=[
        dist(p1,p2),
        dist(p1,p3),
        dist(p1,p4),
        dist(p2,p3),
        dist(p2,p4),
        dist(p3,p4)
    ]
    D.sort()
    return True if 0<D[0]==D[1]==D[2]==D[3] and D[4]==D[5] else False
