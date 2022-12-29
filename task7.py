def PascTriangle(p):
    row = [1]
    y = [0]
    for x in range(max(p, 0)):
        print(row)
        row = [left + right for left, right in zip(row + y, y + row)]


PascTriangle(6)
input()
