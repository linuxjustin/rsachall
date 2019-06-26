def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m





p = 416064700201658306196320137931
 
q = 590872612825179551336102196593

n = 245841236512478852752909734912575581815967630033049838269083
e = 3
c = 219878849218803628752496734037301843801487889344508611639028

fi = (p-1)*(q-1)
d = modinv(e, fi)
print ("%x" % pow(c, d, n)).decode("hex")
