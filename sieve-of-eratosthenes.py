def generatePrime(n):
    prime = [1 for i in range(n+1)]
    prime[0] = prime[1] = 0
    for i in range(2,n+1):
        if prime[i]==1:
            for j in range(2,n//i+1):
                prime[i*j]=0
    l=[i for i in range(2,n+1) if prime[i]==1]
    return l