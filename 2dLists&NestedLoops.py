number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid)
print(number_grid[0])
print(number_grid[0][1])


print("----------------")
for i in range(len(number_grid)):
    for j in range(len(number_grid[i])):
        print(number_grid[i][j])

#also we can do below

for row in number_grid:
    for col in row:
        print(col)
