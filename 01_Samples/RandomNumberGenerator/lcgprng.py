def lcg(x, a, c, m):
    while True:
        x = (a * x + c) % m
        yield x
#
# Provided that c is nonzero, the LCG will have a full period for all seed values if and only if:
#     c and m are relatively prime,
#     a-1 is divisible by all prime factors of m,
#     a-1 is a multiple of 4 if m is a multiple of 4.
#

def random_uniform_sample(n, interval, seed=0):
    a, c, m = 1103515245, 12345, 2 ** 31
    bsdrand = lcg(seed, a, c, m)

    lower, upper = interval[0], interval[1]
    sample = []

    for i in range(n):
        observation = (upper - lower) * (next(bsdrand) / (2 ** 31 - 1)) + lower
        sample.append(round(observation))

    return sample


if __name__ == "__main__":
    # 30 numbers between 0 and 100
    rus = random_uniform_sample(30, [1, 9999])
    print(rus)
