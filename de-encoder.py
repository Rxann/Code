import dcoder
option = input("Encode or decode: ")
aa = "encode"
ab = "decode"
msg = input("> ")
encoder = dcoder.text2caesar(f"{msg}")
decoder = dcoder.caesar2text(f"{msg}")

if option == aa:
    print(encoder)

if option == ab:
    print(decoder)