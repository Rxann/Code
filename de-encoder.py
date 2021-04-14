import dcoder
print("Welcome!")
option = input("Encode decode encode binary(bin) or reverse: ")
aa = "encode"
ab = "decode"
ac = "bin"
ae = "reverse"

msg = input("> ")
encoder = dcoder.text2caesar(f"{msg}")
decoder = dcoder.caesar2text(f"{msg}")
binencode = dcoder.text2bin(f"{msg}")
advanced = dcoder.reverse(f"{msg}")

if option == aa:
    print(encoder)
if option == ab:
    print(decoder)

if option == ac:
    print(binencode)

if option == ae:
    print(advanced)

