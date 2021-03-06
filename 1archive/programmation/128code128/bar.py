#!python

import base64
from PIL import Image
from io import BytesIO
import base64

tuple = {
"11001101100": "!",
"11001100110": "\"",
"10010011000": "#",
"10010001100": "$",
"10001001100": "%",
"10011001000": "&",
"10011000100": "'",
"10001100100": "(",
"11001001000": ")",
"11001000100": "*",
"11000100100": "+",
"10110011100": ",",
"10011011100": "-",
"10011001110": ".",
"10111001100": "/",
"10011101100": "0",
"10011100110": "1",
"11001110010": "2",
"11001011100": "3",
"11001001110": "4",
"11011100100": "5",
"11001110100": "6",
"11101101110": "7",
"11101001100": "8",
"11100101100": "9",
"11100100110": ":",
"11101100100": ";",
"11100110100": "<",
"11100110010": "=",
"11011011000": ">",
"11011000110": "?",
"11000110110": "@",
"10100011000": "A",
"10001011000": "B",
"10001000110": "C",
"10110001000": "D",
"10001101000": "E",
"10001100010": "F",
"11010001000": "G",
"11000101000": "H",
"11000100010": "I",
"10110111000": "J",
"10110001110": "K",
"10001101110": "L",
"10111011000": "M",
"10111000110": "N",
"10001110110": "O",
"11101110110": "P",
"11010001110": "Q",
"11000101110": "R",
"11011101000": "S",
"11011100010": "T",
"11011101110": "U",
"11101011000": "V",
"11101000110": "W",
"11100010110": "X",
"11101101000": "Y",
"11101100010": "Z",
"11100011010": "[",
"11101111010": "\\",
"11001000010": "]",
"11110001010": "^",
"10100110000": "_",
"10100001100": "`",
"10010110000": "a",
"10010000110": "b",
"10000101100": "c",
"10000100110": "d",
"10110010000": "e",
"10110000100": "f",
"10011010000": "g",
"10011000010": "h",
"10000110100": "i",
"10000110010": "j",
"11000010010": "k",
"11001010000": "l",
"11110111010": "m",
"11000010100": "n",
"10001111010": "o",
"10100111100": "p",
"10010111100": "q",
"10010011110": "r",
"10111100100": "s",
"10011110100": "t",
"10011110010": "u",
"11110100100": "v",
"11110010100": "w",
"11110010010": "x",
"11011011110": "y",
"11011110110": "z",
"11110110110": "{",
"10101111000": "|",
"10100011110": "}",
"10001011110": "~",
}


base = """iVBORw0KGgoAAAANSUhEUgAAAYEAAABkCAIAAADvxRv2AAABzUlEQVR4nO3UO27DMBQAQSP3v7NS
GDECkqLoapuZwvCHosRnYF+vP9d1fV7fb95OFsxffr5f7jCsn1cOPy3vOCyYf/p/4XLPzcrl+7uZ
DMPZnGX5PI+D3Yz0/FDz2If73k1yuNfyr5mfZHPe5Q7DYz/u/PhfHB5zHsvd4pM9v12wf7DlJIcL
Dye2uXBz8OXH+arzxcu7/LwAOhoElDQIKGkQUNIgoKRBQEmDgJIGASUNAkoaBJQ0CChpEFDSIKCk
QUBJg4CSBgElDQJKGgSUNAgoaRBQ0iCgpEFASYOAkgYBJQ0CShoElDQIKGkQUNIgoKRBQEmDgJIG
ASUNAkoaBJQ0CChpEFDSIKCkQUBJg4CSBgElDQJKGgSUNAgoaRBQ0iCgpEFASYOAkgYBJQ0CShoE
lDQIKGkQUNIgoKRBQEmDgJIGASUNAkoaBJQ0CChpEFDSIKCkQUBJg4CSBgElDQJKGgSUNAgoaRBQ
0iCgpEFASYOAkgYBJQ0CShoElDQIKGkQUNIgoKRBQEmDgJIGASUNAkoaBJQ0CChpEFDSIKCkQUBJ
g4CSBgElDQJKGgSUNAgoaRBQ0iCgpEFASYOAkgYBJQ0CShoElDQIKP0CFV07qO+o/rgAAAAASUVO
RK5CYII="""

def basetocode(base):
    image = Image.open(BytesIO(base64.b64decode(base)))

    pixels = image.load()
    # Iterate over pixels of the first row
    extracted = ''

    for x in range(0,image.width):
        r,_,_ = pixels[x,50]
        if(r == 0):
            extracted += "1"
        else:
            extracted += "0"

    line = extracted
    n = 11
    out = [line[i:i+n] for i in range(0, len(line), n)]

    code = ""

    for i in out:
        # print(int(i,2))
        code+=tuple[i]

    return code

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('challenge.404ctf.fr', 30566))

n=0
for i in range(128):
    m = sock.recv(1024)
    base = m.decode().split("\n")[1+n]
    n=1
    print(m.decode())

    code = basetocode(base)
    sock.send(code.encode()+b"\n")

m = sock.recv(1024)
print(m.decode())
