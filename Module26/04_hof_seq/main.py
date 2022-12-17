def QHofstadter(s: list):
    a = s[:]
    count = 0
    if a != [1, 1]:
        return
    while count != 10:
        count += 1
        q = a[-a[-1]] + a[-a[-2]]
        a.append(q)
        yield q


user = QHofstadter([1, 1])
for x in user:
    print(x, end=' ')
