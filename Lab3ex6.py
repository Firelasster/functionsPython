def isVoid(*args):
    args = list(args)
    for i in range(len(args)):
        args[i] = set(args[i])
    intersections = args[0]
    for i in range(1, len(args)):
        intersections = intersections & args[i]
    if len(intersections) == 0:
        return True
    else:
        return False

list1 = [1, 2, 2, 4]
list2 = [5, 9]
list3 = [1, 9, 8]
list4 = [0]
print(isVoid(list1, list3, list4))
print(isVoid(list2,list3))
