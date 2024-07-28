def solveNQueens(n):
    col = set()
    posDiagonal = set() # (r + c)
    negDiagonal = set() # (r - c)

    res = []

    board = [["."] * n for i in range(n)]

    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return

        for c in range(n):
            if c in col or (r + c) in posDiagonal or (r - c) in negDiagonal:
                continue

            col.add(c)
            posDiagonal.add(r+c)
            negDiagonal.add(r-c)
            board[r][c] = "Q"

            backtrack(r+1)

            col.remove(c)
            posDiagonal.remove(r+c)
            negDiagonal.remove(r-c)
            board[r][c] = "."
        
    backtrack(0)

    return res


n = int(input("Enter n: "))
output = solveNQueens(n)
print(f"There are {len(output)} possibilities")
for row in output:
    for r in row:
        print(r)
    print("--------------")

