# 🌾 Grain of truth (OSINT) - L3AK CTF 2025

[← Back to L3AK CTF 2025](ctf-l3ak-2025.md)

Category: OSINT

Points: 50

Author: Suvoni, 0x157

![screenprint_04.png](assets/screenprint_04.png)

## Summary

Dropped into a dry, featureless landscape, we had little to go on — except for one crucial detail: a telephone pole number plate. With the right tools, that was more than enough.

## Investigation

Based on the environment and the road signage style, we suspected Asia, and more specifically Taiwan.

The real breakthrough came with [Plonkit](https://www.plonkit.net/taiwan#1), a GeoGuessr resource explaining how to interpret Taiwanese utility pole codes. These codes can be used to determine the township, region, and grid location of a specific pole.

Using this info, we reverse-engineered the coordinates and confirmed the location via satellite view.

📍 [View on Google Maps](https://maps.app.goo.gl/YeafRYgKzqGrPQvv7)

Coordinates:

    23.555863243591038, 120.44644165279037

## ✅ Final Flag

    L3AK{Wh0_Kn3W_El3ctr1C_p0L3S_W3R3_so_Us3FuL!}