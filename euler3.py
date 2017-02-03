import math
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

initial = 65975
final = 600851475143


def factors(x):#find factors within range of input, highest factor cannot be larger than square root
    regFactors = []
    for b in range(2,int(math.sqrt(x))):
        if x % b == 0:
            regFactors.append(b)
    
    return regFactors

def primeNumber(x):#Find prime number
    if x<2:
        return False
    
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
    
def primeFactors(x):#Find if array of factors are prime
    prime = []
    for b in x:
        if(primeNumber(b)):
            prime.append(b)
    return prime
            
def printFactors(x):#Print factors
    for a in x:
        print(a)
    return

printFactors(primeFactors(factors(initial)))
print("")
printFactors(primeFactors(factors(final)))


