import math


initial = 65975
final = 600851475143


def factors(x):
    regFactors = []
    for b in range(2,int(math.sqrt(x))):
        if x % b == 0:
            regFactors.append(b)
    
    return regFactors

def primeNumber(x):
    if x<2:
        return False
    
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
    
def primeFactors(x):
    prime = []
    for b in x:
        if(primeNumber(b)):
            prime.append(b)
    return prime
            
def printFactors(x):
    for a in x:
        print(a)
    return

printFactors(primeFactors(factors(initial)))
print("")
printFactors(primeFactors(factors(final)))


