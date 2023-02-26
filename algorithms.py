import math


def gcd(a, b):
    while b != 0:
        tmp = b
        b = a % b
        a = tmp
    return a


def egcd(a, b):
    '''
    Find x, y such that a.x + b.y = gcd(a, b)
    '''

    # Initialize s_0, t_0, s_1, t_1
    x, y, u, v = 0, 1, 1, 0

    while a != 0:
        # Find q_i-1 and r_i
        q, r = b//a, b % a

        # s_i = s_i-2 - s_i-1*q_i-1 (s = x - u*q)
        # t_i = t_i-2 - t_i-1*q_i-1 (t = y - v*q)
        s, t = x-u*q, y-v*q

        # b = a, a = r, ...
        b, a, x, y, u, v = a, r, u, v, s, t

    gcd = b
    return gcd, x, y


def inverse_mod(n, m):
    '''
    Find x such that n.x mod m = 1
    '''
    gcd, x, y = egcd(n, m)
    return x % m


def legendre(n, p):
    '''
    Check whether n number is a quadratic residue
    '''
    return pow(n, (p - 1) // 2, p) == 1


def factor_powers2(n):
    '''
    # Factoring out powers of 2 of n
    '''
    q, s = n, 0
    while (q % 2 == 0):
        q = q // 2
        s += 1
    return q, s


def tonelli_shanks(n, p):
    '''
    Find x such that x^2 = n (mod p) with n is a quadratic residue
    '''

    # Factoring out powers of 2 as the form p - 1 = q.2^s
    q, s = factor_powers2(p - 1)

    # p mod 4 = 3
    if (s == 1):
        return pow(n, (p + 1) // 4, p)

    # Find z in Zp/Z such that z is a quadratic non-residue (z/p) = -1 (mod p)
    for z in range(2, p):
        if (legendre(z, p) == p - 1):
            break

    m = s
    c = pow(z, q, p)
    t = pow(n, q, p)
    r = pow(n, (q+1)//2, p)

    while (t % p != 1):
        # Find least i such that t^(2^i) = 1 mod p
        for i in range(1, m):
            t = pow(t, 2, p)  # t = t^2 mod p
            if (t % p == 1):
                break

        b = pow(c, 1 << (m - i - 1), p)
        c = pow(b, 2, p)
        t = (t * c) % p
        r = (r * b) % p
        m = i

    return r


def crd(A, M):
    '''
    Chinese remainder theorem
    '''
    N = 1
    for m in M:
        N *= m

    x = 0
    for i in range(0, len(M)):
        Ni = N // M[i]
        Mi = inverse_mod(Ni, M[i])
        x += A[i]*Ni*Mi

    return x % N

print(crd([2,3,5], [5,11,17]))