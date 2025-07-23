# Zeus — Down under CTF 2025 (Beginner)

[← Back to DUC CTF 2025](../ctf-duc-2025.md)

Category: Beginner

Points:

Author: jzt

## Description

To Zeus Maimaktes, Zeus who comes when the north wind blows, we offer our praise, we make you welcome!

Handout: [google api storage](https://storage.googleapis.com/downunderctf-2025-noctf-files/noctf-files/e8CmMDbnsXs3EcmKAxYrW?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=GOOG1ELBSKCSEHWDHBGZCFZBP3RXLJBHVAZJTTYKCMYMRJRM6O5N35G46S26H%2F20250718%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20250718T171000Z&X-Amz-Expires=1200&X-Amz-SignedHeaders=host&X-Amz-Signature=8b0bc91b37f5f0e810f2b9870fe9b0b809ec728ee475a09b6e80f0fde5c942fe)

## Summary and solution

We are given a ELF file, which obfuscates the flag. By getting the c code with [Dogbolt](https://dogbolt.org/), we get something like this rewriten in python.

```c++
encrypted = bytes([
0x09, 0x34, 0x2a, 0x39, 0x27, 0x10, 0x1f, 0x0c, 0x1d, 0x56,
0x6c, 0x5c, 0x51, 0x12, 0x15, 0x01, 0x08, 0x3e, 0x04, 0x18,
0x1c, 0x1e, 0x41, 0x5a, 0x52, 0x59, 0x12, 0x06, 0x06, 0x09,
0x12, 0x34, 0x15, 0x0b, 0x17, 0x6e, 0x54, 0x5c, 0x53, 0x12,
0x0e, 0x0f, 0x32, 0x15, 0x03, 0x11, 0x3a, 0x00, 0x5a, 0x4a,
0x4e
])

key = b"Maimaktes1337"
key_len = len(key)

# Decrypt
decrypted = bytearray()
for i in range(len(encrypted)):
decrypted.append(encrypted[i] ^ key[i % key_len])

print(decrypted.decode())
```

## ✅ Final Flag

    DUCTF{king_of_the_olympian_gods_and_god_of_the_sky}
