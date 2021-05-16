from collections import Counter


def get_fibonnacci():
    f = [0, 1, 1]
    while True:
        f = f[1:]
        f.append(f[0] + f[1])
        yield f[-1]


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def get_divisors_qty(n):
    factors = prime_factors(n)
    qty = 1
    for _, power in Counter(factors).items():
        qty *= power + 1
    return qty


def find_fibonacci():
    f = get_fibonnacci()
    while True:
        n = next(f)
        qty = get_divisors_qty(n)
        if qty >= 1000:
            return n, qty


if __name__ == '__main__':
    print(find_fibonacci())
