from itertools import combinations

def lexiFreq(arr,k):
    temp=set(arr)
    temp=list(temp)
    c=[]
    ans=[]
    for i in temp:
        c.append(arr.count(i))
    while k!=0:
        ma=max(c)
        if c.count(ma)==1:
            ind=c.index(ma)
            ans.append(temp[ind])
            c.remove(ma)
            temp.remove(temp[ind])
            k-=1
        else:
            ind=[]
            a=c.count(ma)
            while len(ind)!=a:
                i=c.index(ma)
                ind.append(temp[i])
                c.remove(ma)
                temp.remove(temp[i])
            ind.sort()    
            for i in ind:
                if k>0:
                    k-=1
                    ans.append(i)
                else:
                    break
    return ans

def frequencySort(s):
    ans=''
    temp=[]
    se=list(set(s))
    for i in se:
        temp.append([i,s.count(i)])
    temp=sorted(temp,key=lambda x:x[1],reverse=True)
    for i,j in temp:
        ans+=i*j
    return ans

def combi(arr):
    comb=combinations(arr, 3)
    c=0
    for i in comb:
        if sum(i)==0:
            print(i)
            c+=1
    return c

def subArr(Arr,target):
    i,j=0,1
    su=0
    n=len(Arr)
    while i<n and j<=n:
        su=sum(Arr[i:j])
        if su<target and j<n:
            j+=1
            continue
        elif su>target:
            i+=1
            continue
        elif target==su:
            print(f'{i} to {j} index')
            return
    return False

def floorF(Arr,i,j,new,old):
    n=len(Arr)
    if i>n or i<0 or j>n or j>n:
        return
    if Arr[i][j]!=old:
        return
    Arr[i][j]=new

    floorF(Arr,i+1,j,new)
    floorF(Arr,i,j+1,new)
    floorF(Arr,i-1,j,new)
    floorF(Arr,i,j-1,new)

def floorFill(Arr,i,j,new):
    old=Arr[i][j]   
    floorF(Arr,i,j,new,old)
#Arr=[[2,0,0,1,0],[2,1,2,1,0],[0,0,1,2,0],[1,2,0,2,1],[1,2,0,1,2]]

def subarraySum(nums, k):
    if len(nums)==0:
        return 0
    count=0
    mapp={0:1}
    cur_sum=0
    for i in range(len(nums)):
        cur_sum+=nums[i]
        if cur_sum-k in mapp:
            count+=mapp[cur_sum-k]
        if cur_sum in mapp:
            mapp[cur_sum]+=1
        else:
            mapp[cur_sum]=1
    return count
#subarraySum([1,0,1,2,-1],2)

def maxArea(height):
    left=0
    right=len(height)-1
    maxArea=0
    while left<right:
        area=(right-left)*min(height[left],height[right])
        maxArea=max(maxArea,area)
        if height[left]>height[right]:
            left+=1
        else:
            right-=1
    return maxArea

def getCommon(nums1,nums2):
    left=0
    right=0
    while left<len(nums1) and right<len(nums2):
        if nums2[right]==nums1[left]:
            return nums2[right]
        if nums2[right]>nums1[left]:
            left+=1
        else:
            right+=1
    return -1

def kadane(nums):
    ans=nums[0]
    maxSum=nums[0]
    for i in range(1,len(nums)):
        maxSum=max(nums[i],maxSum+nums[i])
        ans=max(ans,maxSum)
    return ans

class LinkedList:
    def __init__(self):
        self.head=None
        
    def insert(self,value):
        newNode=ListNode(value)
        newNode.next=None
        if self.head==None:
            newNode.prev=None
            self.head=newNode
            return
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode
            newNode.prev=temp


class ListNode:
    def __init__(self, val):
        self.prev=None
        self.val = val
        self.next = None

def remove(head,i):
    if i==0:
        return head
    if head.next==None:
        head=None
    else:
        head.next=head.next.next
        
    return remove(head,i-1)
    
#incomplete
def removeZeroSumSublists(head):
    temp=head
    while temp!=None:
        flag=False
        while temp!=None and temp.val+temp.next.val==0:
            temp=prev
            temp=remove(temp,2)
            flag=True
        prev=temp
        if flag==False:
            temp=temp.next
    return head

l=LinkedList()
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(-3)
l.insert(-2)

#removeZeroSumSublists(l.head)

def groupAnagrams(strs):
    dic={}
    sr=''
    ans=[]
    for i in strs:
        sr=''
        key=sorted(i)
        for a in key:
            sr+=a
        if sr not in dic:
            dic[sr]=[i]
            continue
        dic[sr].append(i)
    for i in dic.values():
        ans.append(i)
    return ans

#incomplete
def numSubarraysWithSum(nums, goal):
        count=0
        for i in range(len(nums)):
            su=nums[i]
            for j in range(i,len(nums)):
                if i==j:
                    if goal==su:
                        count+=1
                else:
                    su+=nums[j]
                    if goal==su:
                        count+=1
                        continue
                    su-=i
        return count
#numSubarraysWithSum([0,0,0,0,0],0)

def lengthOfLongestSubstring(s):
    if len(s)==0:
            return 0
    ma,count=0,0
    for i in range(len(s)):
        temp=''
        if ma<count:
            ma=count
        count=0
        for j in range(i,len(s)):
            if s[j] in temp:
                break
            temp=temp+''+s[j]
            count+=1
    if count>ma:
        ma=count
    return ma

def majorityElement(nums):
        temp=set(nums)
        ma=0
        res=0
        for i in temp:
            if nums.count(i)>ma:
                ma=nums.count(i)
                res=i
        return res










