from hashlib import md5, sha256  # the hash functions
from itertools import product  # fancy python itertools class to create the cartesian product of a list
from string import printable as chars # all the characters that might be in the flag, renamed to chars since I get annoyed when my IDE autocompletes to printable instead of print

hashes = """4b43b0aee35624cd95b910189b3dc231
cd0aa9856147b6c5b4ff2b7dfee5da20aa38253099ef1b4a64aced233c9afe29
3e23e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d
0d61f8370cad1d412f80b84d143e1257
63ee3b90f0bc64026eafa8cde95c5f410c847be841536b7240d778688cfed72a
6874f52cfc77bd71e9394fa143bedd8f30811e91b8e64ff8818323df42d4af31
cbd27e9b76c7ad85ae3f36cbe78e546d45327ed1a50787d9c3b989af27e62bf0
44ba660a6bd8ff6b11b3423f9f3bf0dff4550cc6eb7b2e8a09ed3d4694faeb83
5e07d6fdc602b0f9b99f6ea24c39e65835992faac400264c52449bc409cf4efa
7b774effe4a349c6dd82ad4f4f21d34c
c0828e0381730befd1f7a025057c74fb
c195aeabeeee007891190b9ff8a32c70
a87ff679a2f3e71d9181a67b7542122c
67d4143062b55c25f383c9fabbbf1422fad06a2fe0644b43da67c17886dd4bd4
b14a7b8059d9c055954c92674ce60032
50e721e49c013f00c62cf59f2163542a9d8df02464efeb615d31051b0fddc326
97fb5f8538b89f6c1accfd19836b65a73b61fbc2e0cbf84bb858a0fffa3f1592
1b16b1df538ba12dc3f97edbb85caa7050d46c148134290feba80f8236c83db9
24cafc74b88dfafb0524ecc85a76f8bd
3fffd018d2223020be85670d93f565b63df54a9ce3ed2cdf6347a61df016938c
2510c39011c5be704182423e3a695e91
582967534d0f909d196b97f9e6921342777aea87b46fa52df165389db1fb8ccf
cd0aa9856147b6c5b4ff2b7dfee5da20aa38253099ef1b4a64aced233c9afe29
d10b36aa74a59bcf4a88185837f658afaf3646eff2bb16c3928d0e9335e945d2""".split('\n')

table = {}

for L in range(1, 3):
    print("calculating hashes of length", L)
    for tup in product(chars.encode(), repeat=L):
        s = bytearray(tup)
        table[md5(s).digest().hex()] = s.decode()
        table[sha256(s).digest().hex()] = s.decode()

for h in hashes:
    print(table[h], end='')
