import dcoder
option = input("Encode decode or bin: ")
aa = "encode"
ab = "decode"
ac = "bin"
msg = input("> ")
encoder = dcoder.text2caesar(f"{msg}")
decoder = dcoder.caesar2text(f"{msg}")
binencode = dcoder.text2bin(f"{msg}")
if option == aa:
    print(encoder)
if option == ab:
    print(decoder)

if option == ac:
    print(binencode)
    

