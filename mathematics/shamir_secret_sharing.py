#!/usr/bin/env python

import fractions
import random
import sys

# http://rosettacode.org/wiki/Least_common_multiple
def lcm(a, b):
    return abs(a * b) / fractions.gcd(a, b) if a and b else 0

def computePolynomial(secret, x, coefficients):
    return sum(map(lambda power: coefficients[power - 1] * x ** power, range(1, len(coefficients) + 1)), secret)

def divide(secret, minimum, maximum):
    coefficients = [ random.randint(1000, 10000) for i in range(minimum - 1) ]
    coefficients = (166, 94)
    keys = []
    for i in range(1, maximum + 1):
        keys.append([ i, computePolynomial(secret, i, coefficients) ])
    return keys

def computeFreeCoefficient(index, keys):
    xIndex = keys[index][0]
    yIndex = keys[index][1]

    others = filter(lambda i: i != index, range(len(keys)))

    numerator = reduce(lambda x, y: x * -y, map(lambda i: keys[i][0], others), 1)
    denominator = reduce(lambda x, y: x * (xIndex - y), map(lambda i: keys[i][0], others), 1)

    return (yIndex * numerator, denominator)

def reconstructSecretForOne(*keys):
    #
    #         (x  - x1) (x  - x2)
    # l0(x) = -------------------   and so on...
    #         (x0 - x1) (x0 - x2)
    #
    # f(x) = sum(lambda i: li(x), range(len(keys)))
    #
    # Free co-efficient is the secret
    #
    fraction = []
    for i in range(len(keys)):
        numerator, denominator = computeFreeCoefficient(i, keys)
        fraction.append((numerator, denominator))

    computedLcm = reduce(lambda x, y: lcm(x, y), [ f[1] for f in fraction ], 1)
    numerator = 0
    for n, d in fraction:
        numerator += n * (computedLcm / d)

    return numerator / computedLcm

def reconstructSecret(*keys):
    count = len(keys[0][1])
    keysPerIndex = []
    for i in range(count):
        keysForI = []
        for k, kKeys in keys:
            keysForI.append((k, kKeys[i]))
        keysPerIndex.append(keysForI)

    return ''.join([ chr(reconstructSecretForOne(*i)) for i in keysPerIndex ])

if __name__ == '__main__':
    secret = sys.argv[1]
    minimumParticipants = int(sys.argv[2])
    maximumShares = int(sys.argv[3])

    allKeys = {}
    allRandomKeys = {}
    for character in secret:
        keys = divide(ord(character), minimumParticipants, maximumShares)
        for k, s in keys:
            if k not in allKeys:
                allKeys[k] = []
            allKeys[k].append(s)

    randomIndexes = random.sample(allKeys.keys(), minimumParticipants)
    randomKeys = [ (k, allKeys[k]) for k in randomIndexes ]

    print 'All keys:', allKeys
    print 'Select %d keys: %s' % (minimumParticipants, randomKeys)

    print 'Secret:', reconstructSecret(*randomKeys)
