version = list(map(int, input().split('.')))
version[-1] += 1
for x in range(len(version) - 1, -1, -1):
    if version[x] == 10:
        version[x - 1] += 1
        version[x] = 0
version = list(map(str, version))
print('.'.join(version))
