x = 1
y = 1
z = 2
n = 3

for i in range(x+1):
    # print("x: ",i)
    for j in range(y+1):
        # print("y: ",j)
        for k in range(z+1):
            # print("z: ",k)
            if i + j + k != n:
                print(i,j,k)