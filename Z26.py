def encrypt_z26(plaintext, k):
    ciphertext = ""
    for ch in plaintext:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            val = ord(ch) - base
            cipher_val = (val + k) % 26
            ciphertext += chr(base + cipher_val)
        else:
            ciphertext += ch 
    return ciphertext

P = "NguyenThiLyNa"
k = 27  
C = encrypt_z26(P, k)
print("Plaintext:", P)
print("Ciphertext:", C)

