def Nqueen(arr,n):
    ntemp=len(arr)
    if n==0:
        print(arr)
        return True
    for i in range(ntemp):
        for j in range(ntemp):
            if safeCheck(arr,i,j,ntemp)==True:
                continue
            arr[i]=arr[i][:j]+'Q'+arr[i][j+1:ntemp]
            if Nqueen(arr,n-1)==True:
                arr[i]=arr[i]=arr[i][:j]+'.'+arr[i][j+1:ntemp]
                return
            arr[i]=arr[i]=arr[i][:j]+'.'+arr[i][j+1:ntemp]
    return False

def safeCheck(arr,i,j,n):
    for a in range(n):
        if arr[i][a]=='Q':
            return True
        if arr[a][j]=='Q':
            return True
    a=i
    b=j
    while a>=0 or b>=0:
        a-=1
        b-=1
        if a<0 or b<0:
            break
        if arr[a][b]=='Q':
            return True
    a=i
    b=j
    while a>=0 or b<n:
        a-=1
        b+=1
        if a<0 or b>=n:
            break
        if arr[a][b]=='Q':
            return True
    a=i
    b=j
    while a<n and b<n:
        a+=1
        b+=1
        if a>=n or b>=n:
            break
        if arr[a][b]=='Q':
            return True
    a=i
    b=j
    while a<n or b>=0:
        a+=1
        b-=1
        if a>=n or b<0:
            break
        if arr[a][b]=='Q':
            return True
    return False
n=4
c='.'*n
arr=[c]*n

#Nqueen(arr,n)
