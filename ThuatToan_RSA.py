

p = 17
q = 23
e = 5
n = p * q
phi = (p - 1) * (q - 1)

# Hàm tính nghịch đảo modular (modular inverse)
def egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        g, x1, y1 = egcd(b, a % b)
        return (g, y1, x1 - (a // b) * y1)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Không tồn tại nghịch đảo modular')
    return x % m

d = modinv(e, phi)

def ma_hoa(thong_diep):
    return [pow(ord(ch), e, n) for ch in thong_diep]

def giai_ma(danh_sach_ma):
    return ''.join(chr(pow(c, d, n)) for c in danh_sach_ma)

if __name__ == "__main__":
    P = "NguyenThiLyNa"
    C = ma_hoa(P)
    print("Khóa công khai (n, e):", (n, e))
    print("Khóa bí mật d:", d)
    print("Bản rõ (mã số):", [ord(ch) for ch in P])
    print("Bản mã:", C)
    print("Giải mã:", giai_ma(C))
