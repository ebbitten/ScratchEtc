def isPower(n)
    max=int(n**.5)
    found=False
    for i in range(1,n+1):
        if found==True:
            break
        for j in range(2,n+1):
            if i**j==n:
                found=True
                break
            if j**i==n and i>1:
                found=True
                break
    return(found)

print(isPower(1))