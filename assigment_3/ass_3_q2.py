

#Recursive solution to the n-queens problem

def n_queens(n):

    #function for checking if a queen can be placed
    def can_place_queen(board, row, col):

        #check column for queen
        for i in range(row):
            if board[i][col] == "Q":
                return False
            
        #check diagonal right to left
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i][j] == "Q":
                return False
            
        #check diagonal from left to right
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j] == "Q":
                return False
            
        #Return true if no queens is found
        return True
    
    def find_solutions(row, board, solutions):

        #Base case of recursion checks if all n rows of the board has been processed
        if row == n:
            #all rows have been processed and we can append this solution to solutions
            solutions.append("\n".join(["".join(row) for row in board]))
            return

        #Re
        for col in range(n):
            if can_place_queen(board, row, col): #using function to check if queen can be placed
                board[row][col] = "Q" # placing queen
                find_solutions(row + 1, board, solutions) # recursively call function and move to next row(row + 1)
                board[row][col] = "."

    board = [["." for _ in range(n)] for _ in range(n)] # board initialization
    solutions = [] #keep track of solutions
    find_solutions(0, board, solutions)

    if len(solutions) == 0:
        return "No possible solutions"
    return solutions

#Test
for solution in n_queens(4):
    print(solution,end="\n\n")