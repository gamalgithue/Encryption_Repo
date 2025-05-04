import random

p = 23  
g = 5  

# Each party chooses a private key
alice_private = random.randint(1, p - 2)
bob_private = random.randint(1, p - 2)

# Each party computes their public key
alice_public = pow(g, alice_private, p) # (5^3) % 13 = 125 % 13 = 8
bob_public = pow(g, bob_private, p)

# Exchange public keys and compute shared secret
alice_shared_secret = pow(bob_public, alice_private, p)
bob_shared_secret = pow(alice_public, bob_private, p)

print(f"Alice's private key: {alice_private}")
print(f"Bob's private key: {bob_private}")
print(f"Alice's public key: {alice_public}")
print(f"Bob's public key: {bob_public}")
print(f"Alice's shared secret: {alice_shared_secret}")
print(f"Bob's shared secret: {bob_shared_secret}")

# The shared secret should be the same
assert alice_shared_secret == bob_shared_secret
