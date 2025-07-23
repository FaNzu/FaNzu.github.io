# yippee — Down under CTF 2025 (OSINT)

[← Back to DUC CTF 2025](../ctf-duc-2025.md)

Category: OSINT

Points:

Author: Nosurf

## Description

We were going through a stack of pictures and postcards that we found in the hope that we can put together a timeline of events. This one looks interesting, on the back of the photo there a hand drawn picture of what looks to be a waratah flower, but that's it.

Can you locate where this is?

Wrap the location name in DUCTF{} (case insensitive, no spaces)

![yippee.png](../assets/yippee.png)

## Summary and solution

We looked up the flower mentioned, which is native to southeastern australia (New South Wales, Victoria, and Tasmania). 
Secondly we looked up tides in au, which seems to hit either north-east or west. Meaning the area between tasmania and mainland can be ignored. 
Then we looked up what is rip tides/rip currents, which is a specific type of dangrous water current. https://www.surflifesaving.org.nz/stay-safe/beach-hazards/rips

Then we found an old daily mail about the most dangerous beaches in australia which had a image of the beach.
https://www.dailymail.co.uk/news/article-5189675/Australias-dangerous-beaches-drownings.html

## ✅ Final Flag

    DUCTF{Flynns_Beach}
