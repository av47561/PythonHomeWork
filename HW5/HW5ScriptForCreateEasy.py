import os
n = 9
i = 1
while i <= n:
    os.mkdir('{}{}'.format('dir_', i))
    i = i + 1

