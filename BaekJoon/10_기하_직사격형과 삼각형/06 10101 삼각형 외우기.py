a = int(input())
b = int(input())
c = int(input())

if a + b + c != 180:
    print("Error")
else:
    s = set()
    s.update([a, b, c])
    if len(s) == 1:
        print("Equilateral")
    elif len(s) == 2:
        print("Isosceles")
    else:
        print("Scalene")