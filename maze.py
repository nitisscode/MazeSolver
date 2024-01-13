#import random library
import random
from colorama import Fore


#blank maze array for maki it a 2D array and N for the maze size
maze=[]
N=int(input("Enter the size of the maze: "))

# maze generator function
def GenerateMaze(N,maze):
    s=["◌","▓"]
    for i in range(N):
        arr=random.choices(s,weights=(75,25),k=N)

        maze.append(arr)  

    maze[0][0]=(Fore.GREEN+"S")
    maze[N-1][N-1]=(Fore.GREEN+"E")
    maze[0][0]=("S")
    maze[N-1][N-1]=("E")
    PrintMaze(N,maze)



# maze printing function
def PrintMaze(N,maze):
    for i in range(N):
        for j in range(N):
            if(maze[i][j]=="◌"):
                print(Fore.BLUE+maze[i][j],end=" ")
            elif(maze[i][j]=="▓"):
                print(Fore.RED+maze[i][j],end=" ")  
        print()          
    



#maze funtion  calling
GenerateMaze(N,maze) 

#
print(Fore.RESET)
print(maze)
