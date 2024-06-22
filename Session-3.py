def modifyString(s):
        n=len(s)
        for i in range(n):
            st='a'
            if s[i]=='?':
                if s[i-1]==st and i!=0:
                    st=chr(ord(st)+1)
                if s[i+1]==st and i!=n-1:
                    st=chr(ord(st)+1)
                s=s.replace('?',st,1)
        return s
                
def decrypt(code, k):
    n=len(code)
    temp=[0]*n
    if k>0:
        first=sum(code[:k])
        for i in range(n):
            first=first-code[i]+code[(k+i)%n]
            temp[i]=first
    elif k<0:
        first=sum(code[k:])
        for i in range(n):
            temp[i]=first
            first=first+code[i]-code[(k+i)%n]
    else:
        return temp
    return temp

def findLengthOfShortestSubarray(arr):
    n=len(arr)
    s,e=0,n-1
    while s<n-1 and arr[s]<=arr[s+1] :
        s+=1
    if s==n-1:
        return 0
    
    while e>=s and arr[e]>=arr[e-1]:
        e-=1
    if e==0:
        return n-1
    res=min(n-s-1,e)
    i,j=0,e
    while i<=s and j<n:
        if arr[j]>=arr[i]:
            res=min(res,j-i-1)
            i+=1
        else:
            j+=1
    return res
#findLengthOfShortestSubarray([1,2,3,10,4,2,3,5])
def addToArrayForm(num,k):
        val=0
        temp=[]
        n=len(num)
        for i in range(n):
            val+=num[i]
            if i!=n-1:
                val*=10
        val=val+k
        while val!=0:
            temp.append(val%10)
            val=val//10
        return temp[::-1]

def corpFlightBookings(bookings, n):
        temp=[0]*(n+1)
        for i in bookings:
            temp[i[0]-1]+=i[2]
            temp[i[1]]-=i[2]
        tmp=0
        for i in range(n):
            tmp+=temp[i]
            temp[i]=tmp
            
        return temp[:n]
    
#corpFlightBookings([[2,2,35],[1,2,10]],2)

def alphabetBoardPath(target):
    i,j=0,0
    ans=[]
    for c in target:
        diff=ord(c)-ord('a')
        row,col=divmod(diff,5)
        while i>row:
            i-=1
            ans.append('U')
        while j>col:
            j-=1
            ans.append('L')
        while i<row:
            i+=1
            ans.append('D')
        while j<col:
            j+=1
            ans.append('R')
        ans.append('!')
        return ''.join(ans)

class Solution:
    number_of_ways={
        1:1,
        2:2
    }
    def climbStairs(self,n) -> int:
        def num_ways(top_step):
            if top_step not in self.number_of_ways:
                self.number_of_ways[top_step]=num_ways(top_step-1)+ num_ways(top_step-2)
            return self.number_of_ways[top_step]
        return num_ways(n)
    
def hardestWorker(n,logs):
    time=0
    high=0
    li=[]
    mi=float('inf')
    for i in logs:
        if high<=i[1]-time:
            high=i[1]-time
        li.append(i[1]-time)
        time=i[1]
    for i in range(len(li)):
        if li[i]==high:
            if logs[i][0]<mi:
                mi=logs[i][0]
    return mi
    
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def get_head(self):
        return self.head
    def insert(self,val):
        newNode=ListNode(val)
        if self.head is None:
            self.head=newNode
            return
        currNode=self.head
        while currNode.next:
            currNode=currNode.next
        currNode.next=newNode
    
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeNodes(head):
    if not head:
        return None
    head.next=removeNodes(head.next)
    if head.next and head.val<head.next.val:
        return head.next
    return head
'''
l1=LinkedList()
l1.insert(5)
l1.insert(2)
l1.insert(13)
l1.insert(3)
l1.insert(8)
removeNodes(l1.get_head())'''

def getMaximumConsecutive(coins):
    coins.sort()
    cur=0
    for i in range(len(coins)):
        if coins[i]-1>cur:
            break
        cur+=coins[i]
    return cur+1

def threeSumClosest(nums, target):
        nums.sort()
        ans=nums[0]+nums[1]+nums[2]

        for left in range(len(nums)-2):
            mid=left+1
            right=len(nums)-1
            while mid<right:
                guess=nums[left]+nums[mid]+nums[right]
                if abs(guess-target)<abs(ans-target):
                    ans=guess
                if guess<target:
                    mid+=1
                elif guess>target:
                    right-=1
                else:
                    return target
        return ans

def candy(rating):
    n=len(rating)
    candy=[1]*n
    for i in range(n-1):
        if rating[i]==rating[i+1]:
            continue
        if rating[i]<rating[i+1]:
            candy[i+1]+=candy[i]+1
        else:
            if candy[i]<=candy[i+1]:
                candy[i]+=candy[i+1]
    for j in range(n-1,0,-1):
        if rating[j]<rating[j-1]:
            if candy[j]>=candy[j-1]:
                candy[j-1]=candy[j]+1
            else:
                continue
    return sum(candy)

def minRemoveToMakeValid(self, s: str) -> str:
    s=list(s)
    temp=[]
    a=''
    for i,ch in enumerate(s):
        if ch=='(':
            temp.append(i)
        elif ch==')':
            if temp:
                temp.pop()
            else:
                s[i]=''
    while temp:
        s[temp.pop()]=''
    for i in s:
        a+=i
    return a

def canBeTypedWords(text, brokenLetters):
        temp=text.split(' ')
        brok=list(brokenLetters)
        cou=0
        for i in temp:
            flag=True
            for j in range(len(brok)):
                if brok[j] in i:
                    flag=False
                    continue
                
                    
            if flag==True:    
                cou+=1
        return cou

def titleToNumber(columnTitle):
    num=0
    for i in columnTitle:
        num=num*26+ord(i)-64
    return num

def bitmanu(a,s):
    if (a>>s)&1==1:
        return True
    else:
        return False
#bitmanu(50,3)

def convery(s,nums):
    ans=[]
    for i in range(nums):
        ans.append('')
    cot=1
    flag=False
    if nums==1:
        return s
    for i in range(len(s)):
        if cot==1:
            flag=False
        if cot==nums:
            flag=True
        if flag==True:
            ans[cot-1].append(s[i])
            cot-=1
        if flag==False:
            ans[cot-1].append(s[i])
            cot+=1
    return ans

def removeKdigits(num,k):
        val=0
        temp=num
        res=float('inf')
        for i in range(len(num)-k+1):
            temp=num
            val=int(num[:i]+num[i+k:])
            res=min(val,res)
        return res

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
longestSubarray([0,1,1,1,0,1,1,0,1])















