import tkinter as tk
from tkinter import messagebox

# Check if number is valid
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[box_row+i][box_col+j] == num:
                return False
    return True

# Backtracking solver
def solve(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                for num in range(1, 10):
                    if is_valid(board, r, c, num):
                        board[r][c] = num
                        if solve(board):
                            return True
                        board[r][c] = 0
                return False
    return True

# Solve button logic
def solve_sudoku():
    board = []
    global user_filled  # Keep track of manually filled cells
    user_filled = [[False] * 9 for _ in range(9)]
    
    for i in range(9):
        row = []
        for j in range(9):
            val = entries[i][j].get()
            if val == "":
                row.append(0)
            else:
                try:
                    num = int(val)
                    if num < 1 or num > 9:
                        raise ValueError
                    row.append(num)
                    user_filled[i][j] = True  # Mark user input
                except ValueError:
                    messagebox.showerror("Invalid Input", f"Invalid entry at row {i+1}, column {j+1}")
                    return
        board.append(row)

    if solve(board):
        for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(0, str(board[i][j]))
                if user_filled[i][j]:
                    entries[i][j].config(fg="black")
                else:
                    entries[i][j].config(fg="green")
    else:
        messagebox.showinfo("Result", "No solution exists.")

# Create GUI
root = tk.Tk()
root.title("Sudoku Solver")

entries = []
user_filled = [[False]*9 for _ in range(9)]

for i in range(9):
    row_entries = []
    for j in range(9):
        e = tk.Entry(root, width=3, font=("Arial", 18), justify="center")
        e.grid(row=i, column=j, padx=2, pady=2)
        row_entries.append(e)
    entries.append(row_entries)

solve_btn = tk.Button(root, text="Solve", command=solve_sudoku, font=("Arial", 14), bg="green", fg="white")
solve_btn.grid(row=9, column=0, columnspan=9, pady=10)

root.mainloop()
