#import miller_rabin_test file 
from miller_rabin_test import is_prime
import random
def gcd(a, b):
    while b:
        return gcd(b, a%b)
    return a
#extended euclidean algorithm for calculative mod  inverse
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
def best_e(l):
    e = random.randrange(1, l)
    g = gcd(e,l)
    while g != 1:
        e = random.randrange(1, l)
        g = gcd(e,l)
    return e

#generate large primes by randomly selecting prime numbers and testing for primality using miller rabin's test
def generate_prime_candidate(size):
    p = random.getrandbits(size)
    p |= (1 << size - 1) | 1
    return p
def generate_prime_numbers(size = 1024):
    p = 4
    while not is_prime(p):
        p = generate_prime_candidate(size)
    return p
def keys():
    p = generate_prime_numbers()
    q = generate_prime_numbers()
    n = p*q
    totient = (p-1) * (q-1)
    e = best_e(totient)
    d = modinv(e, totient)
    return ((e,n), (d,n))
 
def enc(pk,pt):
    key, n = pk
    cipher_text = [pow(ord(char),key,n) for char in pt]
    return cipher_text
def dec(sk,ct):
    key,n = sk
    plain_text = [chr(pow(char,key,n)) for char in ct]
    return plain_text
def main():
    pk, sk = keys()
    pt = input("Enter the message you want to encrypt:")
    print("Encrypting...")
    ct = enc(pk,pt)
    print("Your cipher text is:", ''.join(map(lambda x: str(x), ct)))
    print("Decrypting...")
    message = dec(sk, ct)
    print("Here is the secret in plain text:",''.join(map(lambda x: str(x), message)))
main()
    
    
    
