def gcd(p,q):
# Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p%q
    return p
def is_coprime(x, y):
    return gcd(x, y) == 1

a = (int(input("Enter an integer :")))
b = (int(input("Enter an integer :")))
print(is_coprime(a , b))
