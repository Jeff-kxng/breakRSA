import gmpy2

# Define the values of N, y, and e
N = gmpy2.mpz(
    "179769313486231590772930519078902473361797697894230657273430081157732675805505620686985379449212982959585501387537164015710139858647833778606925583497541085196591615128057575940752635007475935288710823649949940771895617054361149474865046711015101563940680527540071584560878577663743040086340742855278549092581"
)
y = gmpy2.mpz(
    "22096451867410381776306561134883418017410069787892831071731839143676135600120538004282329650473509424343946219751512256465839967942889460764542040581564748988013734864120452325229320176487916666402997509188729971690526083222067771600019329260870009579993724077458967773697817571267229951148662959627934791540"
)
e = gmpy2.mpz(65537)

# Find sqrt_N and set up A
sqrt_N = gmpy2.isqrt(N)
A = sqrt_N + 1

# Find x such that x^2 = A^2 - N
x = gmpy2.isqrt(A**2 - N)

# Calculate factors p and q
p = A - x
q = A + x

# Calculate phi(N)
phi_N = (p - 1) * (q - 1)

# Calculate the private key d
d = gmpy2.invert(e, phi_N)

# Decrypt y to find x
x = gmpy2.powmod(y, d, N)

# Convert x to hexadecimal representation
hex_x = x.digits(16)

# Find the position of '00' in hex_x and extract the message
position_m = hex_x.find("00")
m = hex_x[position_m + 2:]

# Print the results
print("hex_x =", hex_x)
print("Length of hex_x:", len(hex_x))
print("Notice the odd length due to the initial '0x00' and '0x02' removed during decryption.")
print("Position of the 2nd '0x00':", position_m)
print("The plaintext is:", bytes.fromhex(m).decode("ascii"))
