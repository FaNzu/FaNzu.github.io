# Down To Modulate Frequencies! — Down under CTF 2025 (OSINT)

[← Back to DUC CTF 2025](../ctf-duc-2025.md)

Category: Mics

Points:

Author: pix

## Description

One of the scavengers found an abandoned station still transmitting. It's been so long no one remembers how to decode this old tech, can you figure out what was being transmitted?

Decode the alphanumeric message and wrap it in DUCTF{}.

handout: [dtmf.txt](../assets/dtmf.txt)

## Summary and solution

This seems to be a [Dual-tone multi-frequency](https://en.wikipedia.org/wiki/DTMF_signaling) chal, where the handout is the frequencies written out in a txt. We also quickly realized the frequencies are in roughly 11 unique variants. This we guessed was a references to keypad's from a keypad of an older phone.
But we need to translate these frequencies into something more usable:
* 1906: 1
* 2033: 2
* 2174: 3
* 1979: 4
* 2106: 5
* 2247: 6
* 2061: 7
* 2188: 8
* 2329: 9
* 2150: *
* 2277: 0
* 2418: #

Because it was quite a lot of manual work to go through all of our frequecies tests, we generated a script to fast tests different outcomes for us
```python
# DTMF Decoder - Fixed version to capture the last character

# Define DTMF frequency sums (sum of high+low frequencies ×10)
dtmf_map = {
    1906: '1',
    2033: '2',
    2174: '3',
    1979: '4',
    2106: '5',
    2247: '6',
    2061: '7',
    2188: '8',
    2329: '9',
    2150: '*',
    2277: '0',
    2418: '#'
}

# Phone keypad mapping for multi-press
keypad = {
    '1': [' ', ' ', ' '],
    '2': ['A', 'B', 'C'],
    '3': ['D', 'E', 'F'],
    '4': ['G', 'H', 'I'],
    '5': ['J', 'K', 'L'],
    '6': ['M', 'N', 'O'],
    '7': ['P', 'Q', 'R', 'S'],
    '8': ['T', 'U', 'V'],
    '9': ['W', 'X', 'Y', 'Z'],
    '*': ['*', '*', '*'],
    '0': [' ', ' ', ' '],
    '#': ['#', '#', '#']
}

def decode_dtmf(dtmf_code):
    chunks = [dtmf_code[i:i+4] for i in range(0, len(dtmf_code), 4)]
    
    digits = []
    for chunk in chunks:
        num = int(chunk)
        closest = min(dtmf_map.keys(), key=lambda x: abs(x - num))
        digits.append(dtmf_map[closest])
    
    message = []
    current_digit = None
    count = 0
    
    for d in digits:
        if d == '#':
            if current_digit:
                presses = min(count, len(keypad[current_digit])) - 1
                message.append(keypad[current_digit][presses])
            current_digit = None
            count = 0
        else:
            if d == current_digit:
                count += 1
            else:
                if current_digit:
                    presses = min(count, len(keypad[current_digit])) - 1
                    message.append(keypad[current_digit][presses])
                current_digit = d
                count = 1
    
    # Handle any remaining digits after last '#'
    if current_digit:
        presses = min(count, len(keypad[current_digit])) - 1
        message.append(keypad[current_digit][presses])
    
    return ''.join(message)

dtmf_code = ("2247224722472418224722472418210621062106241823292329232924182247224724181979197919792418"
             "2247224724182174217424182188241819791979197924182174217424182061206120612061241821062106"
             "2418197919791979241821742418206120612061206124182329241819791979197924182106210621062418"
             "2106210621062418206120612061241821742174241822472418217421742418224724182033203324182174"
             "2174241820612061206124182188241819791979241819791979197924182061206120612061")

decoded_message = decode_dtmf(dtmf_code)
flag = f"DUCTF{{{decoded_message}}}"
print(flag)
```

which this we ran it through a keypad and got the following:

## ✅ Final Flag

    DUCTF{ONLYNINETIESKIDSWILLREMEMBERTHIS}