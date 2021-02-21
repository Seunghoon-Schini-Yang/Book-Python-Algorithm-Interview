import collections

print(sorted('eat'))

print(''.join(['a', 'e', 't']))

print(sorted(collections.Counter('eat').items(), key=lambda x: x[0]))

print(hash('sb'))
print(hash(('s', 'b')))

print(hash(True))
print(hash(1))

g = 'abcde'
print(g[1:5])

f = 'abbc'
