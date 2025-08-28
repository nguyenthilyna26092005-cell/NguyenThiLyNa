def MaHoa_Caesar(text, k):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            else: 
                result += chr((ord(char) - ord('a') + k) % 26 + ord('a'))
        else:
            result += char
    return result
BanGoc = "NguyenThiLyNa"
k = 13
BanMa = MaHoa_Caesar(BanGoc, k)
print("BanGoc:", BanGoc)
print("Key(k):", k)
print("BanMa:", BanMa)
