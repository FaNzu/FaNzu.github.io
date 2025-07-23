# wiki — Down under CTF 2025 (OSINT)

[← Back to DUC CTF 2025](../ctf-duc-2025.md)

Category: Mics

Points:

Author: pix

## Description

Use the Wiki to find the flag...

NOTE: This challenge is a continuation of ["Horoscopes"](horoscopes.md), we recommend you complete that challenge first!

AU: nc chal.2025.ductf.net 30015
US: nc chal.2025-us.ductf.net 30015

## Summary and solution

After doing some trial and error on what sites were available to us, it quickly turned into a daunting task as we found the wiki.
So we made a masterlist of all the links, which seemed to open to us.

```
about-us.gmi about-us
community-hub.gmi community-hub
verification-codes.gmi verification-codes
pages/2001_a_space_odyssey.gmi 2001_a_space_odyssey
pages/2010_odyssey_two.gmi 2010_odyssey_two
... 100 lines more :D
```

So i made a scrapper and ran through all the pages.

```python
import ssl
import socket
import os
from urllib.parse import urljoin

input_file = "filtered_pages.txt"
HOST = "chal.2025-us.ductf.net"
PORT = 30015
BASE_URL = f"gemini://{HOST}/"
OUTPUT_DIR = "output"

with open(input_file, "r", encoding="utf-8") as f:
    paths = f.readlines()

def fetch_gemini_url(url: str) -> str:
    parsed_url = url if url.startswith("gemini://") else f"gemini://{HOST}/{url}"
    request = parsed_url + "\r\n"

    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    with socket.create_connection((HOST, PORT)) as sock:
        with context.wrap_socket(sock, server_hostname=HOST) as tls:
            tls.sendall(request.encode("utf-8"))
            response = b""
            while True:
                try:
                    data = tls.recv(4096)
                    if not data:
                        break
                    response += data
                except:
                    break
    return response.decode("utf-8", errors="ignore")

def sanitize_filename(path: str) -> str:
    name = path.replace("pages/", "").replace("/", "_").replace(".gmi", "")
    return "".join(c if c.isalnum() or c in "-_." else "_" for c in name)

def save_as_markdown(path: str, content: str):
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    filename = sanitize_filename(path) + ".md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# gemini://{HOST}/{path}\n\n")
        f.write(content.strip())

    print(f"✅ Saved: {filepath}")

def main():
    for path in paths:
        print(f"🔗 Fetching: {path}")
        content = fetch_gemini_url(path)
        save_as_markdown(path, content)

if __name__ == "__main__":
    main()
```

This downloaded all the pages into markdown for me and saved them locally. Where the flag is located in `pages/rabid_bean_potato.gmi`

## ✅ Final Flag

    DUCTF{rabbit_is_rabbit_bean_is_bean_potato_is_potato_banana_is_banana_carrot_is_carrot}