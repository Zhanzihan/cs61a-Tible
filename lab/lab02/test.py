f = [None, None, None, None]
f[0] = lambda x: x
f[1] = lambda x: f[0](x) + 1
f[2] = lambda x: f[1](f[1](x)) + 1
print(f[2](3))