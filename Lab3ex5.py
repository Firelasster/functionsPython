def isUnique(DataList):
    setRes = set(DataList)
    if len(DataList) == len(setRes):
        return True
    else:
        return False


DataList = [1, 3, 2, 4]
print(isUnique(DataList))
