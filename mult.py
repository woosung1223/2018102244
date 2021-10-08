# 8 x 9 table

for i in range(1, 9):
    print(f"{i} 단", end = " : ")
    for j in range(1, 10):
        print("%3d"%(i *j), end = "")
    print()
