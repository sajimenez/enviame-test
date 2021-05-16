import math


def get_days(distance):
    if distance < 0 or distance > 2000:
        return 'Error: Distance must be between 0 and 2000 Kms'
    n = math.floor(distance / 100)
    print(n)
    f = [0, 1, 1, 2, 3]
    if n > 4:
        for i in range(5, n+1):
            f.append(f[-1] + f[-2])
            print(f)
        return f[-1]
    return f[n]


if __name__ == '__main__':
    import random
    distance = random.randint(0, 2000)
    print(f'Distance: {distance} Kms')
    print(f'Days: {get_days(distance)}')
