import time


maze = [[1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [0, 1, 0, 0   ],
        [1, 1, 1, 0], [0, 0, 1, 0], [1, 0, 1, 1], [0, 0, 1, "End"]
        ]
maze_runner = "*" #maze runner character
 
def display_maze():
    for d1 in maze:    
        for row in d1:
            print(row, end="  ")    
        print("\n")
        
        
    
def did_maze_runner_win(row, col):    
    if (row == len(maze)-1 and col == len(maze[row])-1) and maze[row][col] == "*":
            return True

def backtracking():
    row = 0
    col = 0

    while True:            
        try:    
            if maze[row][col+1]:
                maze[row][col+1] = maze_runner
                col += 1
        except IndexError:
            pass
        
        try:
            if maze[row+1][col]:
                
                maze[row+1][col] = maze_runner
                row += 1

        except IndexError:
            pass
            
        display_maze()
        if did_maze_runner_win(row, col):
                print("maze_runner won")
                break
            
    
    
def main():
    display_maze()
    print("\n\n")
    backtracking()


if __name__ == "__main__":
    main()