# Philtered — Down under CTF 2025 (Beginner)

[← Back to DUC CTF 2025](../ctf-duc-2025.md)

Category: Beginner

Points:

Author: sidd.sh

## Description

Can you phigure this one out?

AU: https://web-philtered-0a2005e5b9bf.2025.ductf.net
US: https://web-philtered-0a2005e5b9bf.2025-us.ductf.net

Handout: [file 1](https://storage.googleapis.com/downunderctf-2025-noctf-files/noctf-files/_ncymVRBgRE8_Ot_mIRih?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=GOOG1ELBSKCSEHWDHBGZCFZBP3RXLJBHVAZJTTYKCMYMRJRM6O5N35G46S26H%2F20250718%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20250718T180000Z&X-Amz-Expires=1200&X-Amz-SignedHeaders=host&X-Amz-Signature=6c54cf510638a6cd6107581c91e0bbd381cbacc1837cebb8b19bb196839e43cc)

## Summary & Exploitation

We're given the source code of index.php, which reveals a simple blacklisting mechanism for file access. Here's a key excerpt:

```
public $blacklist = ['php', 'filter', 'flag', '..', 'etc', '/', '\\'];
```

Any request parameters that include these blacklisted terms are replaced with a default safe file (philtered.txt):

```
if ($this->contains_blacklisted_term($value)) {
$value = 'philtered.txt';
}
```

At first glance, this prevents loading files like flag.php or using ../ for directory traversal. However, there's a hidden setting that can be manipulated:

```
public $allow_unsafe = false;
```

If we can change this to true, the contains_blacklisted_term function simply returns false, disabling the entire filtering mechanism.

## ✅ Bypassing the Filter

The assign_props function allows overriding class properties through URL parameters — including allow_unsafe and nested values like config[path].

So, this URL will disable the filter and load the flag file:

https://web-philtered-0a2005e5b9bf.2025-us.ductf.net/index.php?allow_unsafe=true&config[data_folder]=&config[path]=flag.php

- allow_unsafe=true disables filtering 
- config[path]=flag.php sets the file we want to load 
- config[data_folder]= avoids any prepending of unwanted folder paths

## ✅ Final Flag

    DUCTF{h0w_d0_y0u_l1k3_y0ur_ph1lters?}
