#Q1
while True:
    n = int(input("nhap_a:"))
    if n >= 5:
        break
    else:
        print("re_enter")
def calculate_S1(n):
    return sum(range(1, n + 1))
def calculate_S2(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def calculate_S3(n):
    result = 0
    for i in range(1, n + 1):
        result += 1 / (i + 1)
    return result

s1 = calculate_S1(n)
s2 = calculate_S2(n)
s3 = calculate_S3(n)
print(s1,s2,s3)
import math
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
       print(f"{n} is not a prime number")
       break
    else:
        print(f"{n} is a prime number")
#Q2
m = int(input("type_in_m:"))
n = int(input("type_in_n:"))
import math
def prime_check(num):
    primes = []
    for i in range(2, int(math.sqrt(num))+1):
        if num % i ==0:
            return 0
        else:
            return primes
def find_common_prime(m,n):
    primes_m = set(prime_check(m))
    primes_n = set(prime_check(n))
    common_primes = primes_m.intersection(primes_n)
    return sorted(list(common_primes))
def gcd(m,n):
    while n:
        m, n = n, m%n
        return abs(m)
def lcm(m,n):
    return abs(m*n)//gcd(m,n)
common_primes = find_common_prime(m,n)
print("Common prime dividers:",common_primes)
gcd = gcd(m,n)
print("Greatest common divider:",gcd)
lcm = lcm(m,n)
print("Least common mutiple:",lcm)
        

        



        