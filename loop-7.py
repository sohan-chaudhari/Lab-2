import math
def nCr(n, r):
    if r > n:
        return 0
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

def nPr(n, r):
    if r > n:
        return 0 
    return math.factorial(n) // math.factorial(n - r)


n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

combinations = nCr(n, r)
permutations = nPr(n, r)
print(f"your combinations is = {combinations}")
print(f"your permutations is = {permutations}")

