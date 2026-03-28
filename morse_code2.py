#!/usr/bin/env python3
"""Morse code — encode, decode, timing calculation."""
import sys

CODE = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..","0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----."}
DECODE = {v:k for k,v in CODE.items()}

def encode(text):
    return " / ".join(" ".join(CODE.get(c, "") for c in word.upper() if c in CODE) for word in text.split())

def decode(morse):
    words = morse.split(" / ")
    return " ".join("".join(DECODE.get(c, "?") for c in word.split()) for word in words)

def visual(text):
    for c in text.upper():
        if c == " ": print("       ", end=""); continue
        if c not in CODE: continue
        for s in CODE[c]:
            print("█" if s == "-" else "▪", end=" ")
        print("  ", end="")
    print()

def cli():
    if len(sys.argv) < 2: print("Usage: morse_code2 encode|decode <text>"); sys.exit(1)
    cmd, text = sys.argv[1], " ".join(sys.argv[2:])
    if cmd == "encode": print(encode(text)); visual(text)
    elif cmd == "decode": print(decode(text))
    else: print(encode(sys.argv[1])); visual(sys.argv[1])

if __name__ == "__main__": cli()
