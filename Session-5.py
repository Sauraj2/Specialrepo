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

