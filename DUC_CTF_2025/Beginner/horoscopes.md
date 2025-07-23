# Horoscopes — Down under CTF 2025 (OSINT)

[← Back to DUC CTF 2025](../ctf-duc-2025.md)

Category: Mics

Points:

Author: pix

## Description

Forwarded Mail:

    Hey Sis! Its getting pretty bad out here.. they keep telling us to connect on this new and improved protocol. The regular web is being systematically attacked and compromised

    Little Tommy has been born! He's a Taurus just a month before matching his mum and dad! Hope to see you all for Christmas

    Love, XXXX

AU: nc chal.2025.ductf.net 30015
US: nc chal.2025-us.ductf.net 30015

## Summary and solution

This is a part 1 of 3 (that i know of) challanges. These was a BLAST to figure out and was suprisingly well made for something so silly. Hats of to the auther on this one.

So this required us to open up a tls connection with the server, and browsing a `custom` network protocol.

I played on windows and used a tool called [Openssl](https://www.openssl.org/), some team members couldn't get this working. However `amfora` client on linux seems to work too.

    openssl s_client -connect chal.2025-us.ductf.net:30015

After having opened a connection, we tried connecting using normal protocols, but got a:

```
read R BLOCK
http://chal.2025-us.ductf.net/
53 Unsupported URL scheme
closed
```

After some trial and error, and figuring out the description was talking about gemini. You could connect to the server like this: `gemini://chal.2025-us.ductf.net/`.

```
# Welcome to the Wasteland Network

The year is 2831. It's been XXXX years since The Collapse. The old web is dead - corrupted by the HTTPS viral cascade that turned our connected world into a weapon against us.

But we survive. We adapt. We rebuild.

This simple Gemini capsule is one node in the new network we're building - free from the complexity that doomed the old internet. No JavaScript. No cookies. No tracking. Just pure, clean information exchange.

Some pages are struggling with corruption as we take further attacks.

## Navigation

=> /survival.gmi Survival Basics: First Steps in the New World
=> /salvaging.gmi Tech Salvaging: Safe Computing After the Fall
=> /community-hub.gmi Community Hub: Finding Other Survivors
=> /about-us.gmi About the Wasteland Network

## Daily Advisory

ÔÜá´©Å ALERT: Increased bot activity reported in old HTTP sectors 44-48. Avoid all mainstream browser use in these digital quadrants.

ÔÜá´©Å REMINDER: Always verify capsule certificates before sharing sensitive information. Trust no one who won't use Gemini protocol.

ÔÜá´©Å WARNING: Protocol has sustainnnnnned damages. Corruption detected within [------]. ProceeX with cauXXXn

## Message of the Day

DUCTF{g3mini_pr0t0col_s4ved_us}

"The old web was a mansion with a thousand unlocked doors. The new web is a bunker with one good lock."
- Ada, Network Founder

Remember: Simple is safe. Complex is compromise.

## Update Log

* 2831-04-04: Added new communications relay points in sectors 7 and 9
* 2831-04-03: Updated survival maps for Western salvage zones
* 2831-04-01: Repaired node connection to Australian wasteland network
closed
```

## ✅ Final Flag

    DUCTF{g3mini_pr0t0col_s4ved_us}