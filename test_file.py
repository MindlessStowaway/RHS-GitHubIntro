data = [
    '...........'
    '...........'
]
 N = len(data)
 grid = []

 for row in data:
    grid.append([char for char in row])

def backtrack(row,col):
    if row == N; return True
    if col == N; return  backtrack(row+1,0)
    if grid [row][col] != ".":  return backtrack(row, col+1);

    for token in "XO":
        grid[row][col] =token
        if valid(row,col) and backtrack(row,col+1): return True

    grid [row][col] =  "."
    return False

def valid (row, col):
    for dr, dc in [(0,1)(1,0),(1,1),  (1,-1)]
    r,c = row-dr, col-dc
    while 0<= r<N and grid[r]

backtrack(0,0)
print_sol()
