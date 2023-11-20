def encrypt(text, shift):
    alpha='abcdefghijklmnopqrstuvwxyz'
    n=len(text)
    x=0
    fin=""
    for i in range(n):
        a=text[i]
        for j in range(26):
            if alpha[j]==a:
                  x=j
        t=(x+shift)%26
        fin+=alpha[t]
    return fin
def decrypt(text,shift):
    alpha='abcdefghijklmnopqrstuvwxyz'
    n=len(text)
    x=0
    fin=""
    for i in range(n):
        a=text[i]
        for j in range(26):
            if alpha[j]==a:
                  x=j
        t=(x-shift)%26
        fin+=alpha[t]
    return fin

v="iamamonster"
enc=encrypt(v,8)
dec=decrypt(enc,8)
print("Original string= ", v)
print("Encoded string: ", enc)
print("Decoded string", dec)
