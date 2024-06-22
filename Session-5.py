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
restoreIpAddresses('25525511135')
