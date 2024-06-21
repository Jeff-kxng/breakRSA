import gmpy2

def factorize(N):
    sqrt_24N = gmpy2.isqrt(24 * N)
    A = gmpy2.mpz(sqrt_24N) + 1

    while True:
        x_squared = A * A - 24 * N
        x = gmpy2.isqrt(x_squared)

        if x * x == x_squared:
            # Checking conditions based on the properties derived
            print("(A + x) % 3 =", (A + x) % 3)
            print("(A + x) % 2 =", (A + x) % 2)
            print(
                "Since (A + x) is congruent to 2 modulo 3 and divisible by 2, we have x = 2q - 3p, where A + x = 4q and A - x = 6p"
            )
            p = (A + x) // 4
            q = (A - x) // 6

            if p * q == N:
                return p, q

        A += 1

# RSA modulus N
N = gmpy2.mpz(
    "720062263747350425279564435525583738338084451473999841826653057981916355690188337790423408664187663938485175264994017897083524079135686877441155132015188279331812309091996246361896836573643119174094961348524639707885238799396839230364676670221627018353299443241192173812729276147530748597302192751375739387929"
)

# Factorize N into p and q
p, q = factorize(N)

# Check if p and q are prime
print("p is prime: ", gmpy2.is_prime(p))
print("q is prime: ", gmpy2.is_prime(q))
print(f"p: {p}")
print(f"q: {q}")
