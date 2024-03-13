def ubah_huruf(sentence):
    pattern = ""
    huruf = {chr(i + ord('a')): chr((i + 10) % 26 + ord('a')) for i in range(26)}
    huruf.update({chr(i + ord('A')): chr((i + 10) % 26 + ord('A')) for i in range(26)})
    return "".join(huruf.get(c, c) for c in sentence)

    return pattern

if __name__ == '__main__':
    print(ubah_huruf("SEPULSA OKE")) # COZEVCK YUO
    print(ubah_huruf("ALTERRA ACADEMY")) # KVDOBBK KMKNOWI
    print(ubah_huruf("INDONESIA")) # SXNYXOCSK
    print(ubah_huruf("GOLANG")) # QYVKXQ
    print(ubah_huruf("PROGRAMMER")) # ZBYQBKWWOB