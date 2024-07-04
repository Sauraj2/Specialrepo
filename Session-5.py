def restoreIpAddresses(s):
    ans=[]
    solve(ans,'',0,s,0)
    return ans

def valid(temp):
    if len(temp)>3 or len(temp)==0:
        return False
    if len(temp)>1 and temp[0]=='0':
        return False
    if len(temp) and int(temp)>255:
        return False
    return True

def solve(ans,outp,ind,s,dots):
    if dots==3:
        if valid(s[ind:]):
            ans.append(outp+s[ind:])
        return
    for i in range(ind,min(ind+3,len(s))):
        if valid(s[ind:i+1]):
            new_out=outp+s[ind:i+1]+'.'
            solve(ans,new_out,i+1,s,dots+1)

def checkPossibility(nums):
        flag=False
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                if flag==True:
                    return False
                nums[i]=nums[i+1]
                flag=True

        return True

def removeDuplicates(s):
    temp=list(s)
    z=''
    i=0
    while i<len(temp)-1 and i>=0:
        if temp[i]==temp[i+1]:
            temp.pop(i)
            temp.pop(i)
            if i>1:
                i-=1
            else:
                i=0
            continue
        i+=1
        
    for i in temp:
        z+=i
    return z

def findShortestSubArray(nums):
        ss=set(nums)
        cot=0
        tep=[]
        mini=float('inf')
        for i in ss:
            if nums.count(i)>cot:
                cot=nums.count(i)
        for i in ss:
            if nums.count(i)==cot:
                tep.append(i)
        for x in tep:
            n=len(nums)
            a=0
            while nums[a]!=x:
                n-=1
                a+=1
            a=len(nums)-1
            while nums[a]!=x:
                n-=1
                a-=1
            mini=min(n,mini)
        return mini

def reverseOnlyLetters(s):
        sit=[]
        temp=list(s)
        for i in range(len(s)):
            if ord(temp[i])>=65 and ord(temp[i])<=90:
                sit.append(temp[i])
                temp[i]='10'
                continue
            if ord(temp[i])>=97 and ord(temp[i])<=122:
                sit.append(temp[i])
                temp[i]='10'
        sit=sit[::-1]
        for i in range(len(temp)):
            if temp[i]=='10':
                temp[i]=sit.pop(0)
        sst=''
        for a in temp:
            sst+=a
        return sst

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def mergeNodes(head):
    sum=0
    temp=ListNode()
    ans=temp
    while head:
        if head.val==0:
            head=head.next
            if head==None:
                break
            while head.val!=0:
                sum+=head.val
                head=head.next
            temp.val=sum
            
            temp.next=ListNode()
            temp=temp.next
            sum=0
    temp=ans
    if not temp:
        return
    while temp.next.next:
        temp=temp.next
    temp=None
    return ans

class LinkedList:
    def __init__(self) :
        self.head=None
    
    def append(self,val):
        new=ListNode(val)
        if not self.head:
            self.head=new
            return
        else:
            las=self.head
            while las.next:
                las=las.next
            else:
                las.next=new
        return
'''apr=LinkedList()
apr.append(0)
apr.append(3)
apr.append(1)
apr.append(0)
apr.append(4)
apr.append(5)
apr.append(2)
apr.append(0)
mergeNodes(apr.head)'''
