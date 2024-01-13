#import random library
import random

#blank maze array for maki it a 2D array and N for the maze size
maze=[]
N=int(input("Enter the size of the maze: "))

# maze generator function
def GenerateMaze(N,maze):
    s=["◌","▓"]    
    for i in range(N):
        arr=random.choices(s,weights=(75,25),k=N)

        maze.append(arr)  

    PrintMaze(N,maze)

# maze printing function
def PrintMaze(N,maze):
    for i in range(N):
        for j in range(N):
            print(maze[i][j],end=" ")
        print()    
    



#maze funtion  calling
GenerateMaze(N,maze)    