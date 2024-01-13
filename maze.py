#import random library deque library and Fore library for colors
import random
from collections import deque
from colorama import Fore


#blank maze array for maki it a 2D array and N for the maze size
maze=[]
N=int(input("Enter the size of the maze: "))

# maze generator function
def GenerateMaze(N,maze):
    #s=["◌","▓"]
    for i in range(N):
        arr=random.choices(["▓","◌"],weights=(25,75),k=N)

        maze.append(arr)  

    maze[0][0]="S"
    maze[N-1][N-1]="E"
    
    PrintMaze(N,maze)



# maze printing function
def PrintMaze(N,maze):
    for i in range(N):
        for j in range(N):
            
            if(maze[i][j]=="◌"):
                print(Fore.BLUE+maze[i][j],end=" ")
            
            elif(maze[i][j]=="▓"):
                print(Fore.RED+maze[i][j],end=" ")  
            
            elif(maze[i][j]=="S" or maze[i][j]=="E"):
                print(Fore.GREEN+maze[i][j],end=" ")    
       
        print()          
    



#maze funtion  calling
GenerateMaze(N,maze) 

#Reset colors
print(Fore.RESET)


# Bfs algorithm for path find in 2D maze
def PathFind(N,maze):
    start=(0,0)
    queue=deque([(start,[])])
    visited=[]

    while queue:
        current,path=queue.popleft()
        x,y=current

        if(maze[x][y]=="E"):
            return path + [(x,y)]

        if(current not in visited):
            visited.append(current)    

            neighbors=get_neighbors(N,maze,current)
            for neighbor in neighbors:
                queue.append((neighbor, path+[current]))

    return "No path found from S to E"     


# Function call from pathFind to check next indexes
def get_neighbors(N,maze,current):
    x,y=current
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    neighbors = []

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if(nx>=0 and nx<N and ny>=0 and ny<N and maze[nx][ny]!="▓"):
            neighbors.append((nx, ny))
    return neighbors


#path print function for print path in indexes
def PrintPath(result):
    print(result)


# calling pathfind function and store result and calling printpath function
result=PathFind(N,maze)
PrintPath(result)  
