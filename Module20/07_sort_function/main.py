def tpl_sort(cort):
    for x in cort:
        if x != int(x):
            return cort
    corted = sorted(list(cort))
    return tuple(corted)

print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))