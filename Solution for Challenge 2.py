import gmpy2
from gmpy2 import mpz

def factorize_rsa_modulus_iterative(N):
    A = gmpy2.isqrt(N) + 1
    while True:
        x = gmpy2.isqrt(A**2 - N)
        p = A - x
        q = A + x
        if p * q == N:
            return p, q
        A += 1

# N từ câu hỏi 2
N2 = mpz("648455842808071669662824265346772278726343720706976263060439070378797308618081116462714015276061417569195587321840254520655424906719892428844841839353281972988531310511738648965962582821502504990264452100885281673303711142296421027840289307657458645233683357077834689715838646088239640236866252211790085787877")

p2, q2 = factorize_rsa_modulus_iterative(N2)
print("p:", p2)
print("q:", q2)
print("p * q == N:", p2 * q2 == N2)
