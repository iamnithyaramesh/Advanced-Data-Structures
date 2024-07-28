class NQueens:
    def __init__(self, size):
        self.size = size
        self.board = [[0] * size for _ in range(size)]
    
    def print_solution(self):
        for row in self.board:
            print(" ".join('Q' if cell == 1 else '.' for cell in row))
    
    def is_safe(self, row, col):
        # Check this row on left side
        for i in range(col):
            if self.board[row][i] == 1:
                return False
        
        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        
        # Check lower diagonal on left side
        for i, j in zip(range(row, self.size, 1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        
        return True
    
    def solve_util(self, col):
        # Base case: If all queens are placed then return true
        if col >= self.size:
            return True
        
        # Try placing this queen in all rows one by one
        for i in range(self.size):
            if self.is_safe(i, col):
                # Place this queen in board[i][col]
                self.board[i][col] = 1
                
                # Recur to place rest of the queens
                if self.solve_util(col + 1):
                    return True
                
                # If placing queen in board[i][col] doesn't lead to a solution
                # then remove the queen from board[i][col]
                self.board[i][col] = 0
        
        # If the queen cannot be placed in any row in this column col then return false
        return False
    
    def solve(self):
        if not self.solve_util(0):
            print("Solution does not exist")
            return False
        self.print_solution()
        return True

# Driver Code
if __name__ == '__main__':
    n = 8
    nq = NQueens(n)
    nq.solve()
