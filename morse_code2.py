#!/usr/bin/env python3
"""Morse code — encode and decode."""
import sys
C={"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..","0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----."}
D={v:k for k,v in C.items()}
def encode(t): return " / ".join(" ".join(C.get(c,"") for c in w.upper() if c in C) for w in t.split())
def decode(m): return " ".join("".join(D.get(c,"?") for c in w.split()) for w in m.split(" / "))
def cli():
    if len(sys.argv)<3: print("Usage: morse_code2 encode|decode <text>"); sys.exit(1)
    print(encode(" ".join(sys.argv[2:])) if sys.argv[1]=="encode" else decode(" ".join(sys.argv[2:])))
if __name__ == "__main__": cli()
