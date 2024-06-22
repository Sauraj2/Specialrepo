import math


def maximumLengthSubstring(s) :
    tem=set(s)
    freq={}
    for i in tem:
        freq[i]=0
    ii=ans=0
    for i in range(len(s)):
        freq[s[i]]+=1
        while freq[s[i]]==3:
            freq[s[ii]]-=1
            ii+=1
        ans=max(ans,i-ii+1)
    return ans

def minOperations(k):
    ans=math.inf
    t=0
    for i in range(1,k+1):
        t=math.ceil(k/i)
        ans=min(ans,i-2+t)
    return ans
minOperations(11)