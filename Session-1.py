from math import sqrt

def findSpecialInteger(arr):
    for i in arr:
        if arr.count(i)>len(arr)*0.25:
            return i

def getMaximumGenerated(n): 
    temp=[0]*(n+1)
    if n==0:
        return 0
    if n==1:
        return 1
    temp[1]=1
    for i in range(2,n+1):
        if i%2==0:
            temp[i]=temp[i//2]
        if i%2!=0:
            temp[i]=temp[i//2]+temp[i//2+1]
    return max(temp)
        
def transpose(matrix):
    temp=[]
    for i in range(len(matrix[0])):
        newmat=[0]*(len(matrix))
        temp.append(newmat)
        for j in range(len(matrix)):
            newmat[j]=matrix[j][i]
    return temp

def maxSubArray(nums):
    cursum=nums[0]
    maxsum=nums[0]
    for i in nums[1:]:
        cursum=max(i,cursum+i)
        maxsum=max(maxsum,cursum)
    return maxsum

def findShortestSubArray(nums):
        pass

def twoSum(numbers, target):
    l=0
    r=len(numbers)-1
    while l<r:
        s=numbers[l]+numbers[r]
        if s==target:
            return [l+1,r+1]
        elif s<target:
            l+=1
        else:
            r-=1

def numSpecial(mat):
    count=0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j]==1:
                if sum(mat[i])==1:
                    if getColumn(j,mat)==1:
                        count+=1
    return count

def getColumn(j,mat):
    su=0
    for a in range(len(mat)):
        su+=mat[a][j]
    return su

def hammingWeight(n) :
    count=0
    while n!=0:
        count+=n%10
        n=n//10
    return count

def garbageCollection(garbage, travel):
    total=0
    for j in 'MPG':
        tempT=0
        tempC=0
        for i in range(len(garbage)):
            flag=False
            a=garbage[i].count(j)
            if a>0:
                tempC+=a
                flag=True
            if i>0 and flag==True:
                    tempT=sum(travel[0:i])
        if tempC!=0:
            total+=tempT+tempC
    return total

def garbageCollection(garbage, travel):
    n=len(garbage)
    tG,tP,tM=0,0,0
    time=0
    for i in range(n-1, -1, -1):
        x=garbage[i]
        time+=len(x)
        if tG==0 and x.find('G')!=-1: tG=i
        if tP==0 and x.find('P')!=-1: tP=i
        if tM==0 and x.find('M')!=-1: tM=i
    time+=sum(travel[:tG])+sum(travel[:tP])+sum(travel[:tM])
    return time

def judgeSquareSum(c):
    left=0
    right=int(sqrt(c))
    while left<=right:
        cur=left*left+right*right
        if cur==c:
            return True
        if cur>c:
            right-=1
        else:
            left+=1
    return False

def convertToBase7(num) :
    m=''
    flg=bool
    if num==0:
        return '0'
    if num<0:
        flg=True
    num=abs(num)
    while num!=0:
        m+=str(num%7)
        num=num//7
    if flg==True:
        m+='-'
    return m[::-1]

def mergeAlternately(word1,word2) :
        mas=''
        min=''
        final=''
        if len(word1)>len(word2):
            mas=word1
            min=word2
        else:
            mas=word2
            min=word1
        for i in range(len(min)):
            final+=word1[i]+word2[i]
        final+=mas[len(min):]
        return final

def kidsWithCandies(candies, extraCandies):
        mi=max(candies)
        finList=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=mi:
                finList.append(True)
            else:
                finList.append(False)
        return finList

def maxProductDifference(nums):
        if nums ==[]:
            return 0
        nums.sort()
        max=nums[len(nums)-1]*nums[len(nums)-2]
        min=nums[0]*nums[1]
        product=max-min
        return product

def canPlaceFlowers(flowerbed, n):
    k=0
    i,a=0,0
    flag=False
    while a!=1 and flowerbed[0]!=1:
        if flowerbed[i]==0 and flowerbed[i+1]==0:
            k+=1
        if flowerbed[i+1]==1:
            a=1
        i+=1
    for i in range(i,len(flowerbed)):
        if flowerbed[i]==1 and flag==False:
            a=i
            flag=True
            continue
        if flag==True and flowerbed[i]==1:
            temp=i-a-3
            if temp>0:
                k+=temp
            a=i
            
    if k>=n:
        return True
    return False
#canPlaceFlowers([1,0,0,0,0,1],2)

def reverseVowels(s):
    temp=[]
    ind=[]
    for i in range(len(s)):
        if s[i] in 'aeiouAEIOU':
            temp.append(s[i])
            ind.append(i)
    li=list(s)
    for i in range(len(temp)):
        li[ind[i]]=temp[len(temp)-i-1]
    s=''
    for i in li:
        s+=i
    return s

def reverseWords(s):
    s=s.split(' ')   
    temp=''
    for i in s[::-1]:
        if i!='':
            temp+=i+' '
    return temp.rstrip()
        
def moveZeroes(nums):
    
        c=nums.count(0)
        nums.sort()
        nums=nums[c:]
        for i in range(c):
            nums.append(0)

def isSubsequence(s, t):
    if len(s)>len(t): return False
    if len(s)==0: return True
    subseq=0
    for i in range(len(t)):
        if subseq<=len(s)-1:
            if s[subseq]==t[i]:
                subseq+=1
    return subseq==len(s)

def productExceptSelf(nums):
        n=len(nums)
        product=[1]*n
        for i in range(1,n):
            product[i]=product[i-1]*nums[i-1]
        
        right=nums[-1]
        for i in range(n-2,-1,-1):
            product[i]*=right
            right*=nums[i]
        return product

def findMaxAverage(nums,k):
    a=su=sum(nums[:k])
    for i in range(k,len(nums)):
        su+=nums[i]-nums[i-k]
        if su>a:
            a=su      
    return a/k
            
def uniqueOccurrences(arr):
    s=set(arr)
    temp=[]
    for i in s:
        if arr.count(i) in temp:
            return False
        temp.append(arr.count(i))
    return True

def largestAltitude(gain):
        alt=0
        prog=0
        for i in gain:
            prog+=i
            if prog>alt:
                alt=prog
        return alt

def maxWidthOfVerticalArea(points):
    m=0
    points=sorted(points,key=lambda x:x[0])
    for i in range(1,len(points)):
        diff=points[i][0]-points[i-1][0]
        m=max(m,diff)
    return m
    
class LinkedList:
    def __init__(self):
        self.__head=None
    def get_head(self):
        return self.__head
        
    def insertAtEnd(self, data):
        new_node = ListNode(data)
        if self.__head is None:
            self.__head = new_node
            return
        current_node = self.__head
        while(current_node.next):
            current_node = current_node.next
        current_node.next = new_node
        
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteMiddle(head):
    temp=head
    n=0
    while temp!=None:
        n+=1
        temp=temp.next
    
    temp=head
    m=n//2
    n=1
    if m==0:
        return None
    while n!=m:
        temp=temp.next
        n+=1
    if temp.next.next==None:
        temp.next=None
    else:
        temp.next=temp.next.next
    return head

def reverseList(head):
    temp=head
    prev=None
    while temp!=None:
        next=temp.next
        temp.next=prev
        prev=temp
        temp=next
    head=prev
    return head
    
'''l1=LinkedList()
l1.insertAtEnd(1)
l1.insertAtEnd(3)
l1.insertAtEnd(4)
l1.insertAtEnd(7)
l1.insertAtEnd(1)
l1.insertAtEnd(2)
l1.insertAtEnd(6)'''
#reverseList(l1.get_head())

def maxScore(s):
    left=[]
    right=[]
    ma=0
    for i in range(1,len(s)):
        left=s[:i]
        right=s[i:]
        count=left.count('0')+right.count('1')
        ma=max(ma,count)
    return ma

def isPathCrossing(path: str) -> bool:
        x,y=0,0
        visited={(0,0)}
        moves={'N':(0,1),
               'S':(0,-1),
               'E':(1,0),
               'W':(-1,0)
                }
        for i in path: 
            x+=moves[i][0]
            y+=moves[i][1]
            if (x,y) in visited:
                return True
            visited.add((x,y))
        return False
            
