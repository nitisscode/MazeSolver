#import random library deque library and Fore library for colors
import random
from collections import deque
from colorama import Fore


#blank maze array for maki it a 2D array and N for the maze size
maze=[]
N=0

# maze generator function
def GenerateMaze(maze):
    global N
    N=int(input("Enter the size of the maze(n*n): "))
    for i in range(N):
        arr=random.choices(["▓","◌"],weights=(25,80),k=N)

        maze.append(arr)  

    maze[0][0]="S"
    maze[N-1][N-1]="E"
    
    PrintMaze(N,maze)



# maze printing function
def PrintMaze(N,maze):
    print("Generated Maze:")


    for i in range(N):
        for j in range(N):
            
            if(maze[i][j]=="◌"):
                print(Fore.BLUE+maze[i][j],end=" ")
            
            elif(maze[i][j]=="▓"):
                print(Fore.RED+maze[i][j],end=" ")  
            
            elif(maze[i][j]=="S" or maze[i][j]=="E"):
                print(Fore.GREEN+maze[i][j],end=" ")    
       
        print()
    
    print(Fore.RESET) #Reset colors    
    
    main()   #main function caaling             
    



 

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

    return False     


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

def Path_Marking(result,maze):
    if(result==False):
        print("No path found from S to E")
        return 
    for i in range(len(result)):
        x,y=result[i]
        if((x==0 and y==0) or (x==len(maze)-1 and y==len(maze)-1)):
            continue
        else:
            for j in range(len(maze)):
                for k in range(len(maze)):
                    if(j==x and k==y):
                        maze[j][k]="◍"
                
    for i in range(len(maze)):
        for j in range(len(maze)):
            if(maze[i][j]=="▓"):
                print(Fore.RED+maze[i][j],end="  ")
            elif(maze[i][j]=="◌"):
                print(Fore.BLUE+maze[i][j],end="  ")
            elif(maze[i][j]=="S" or maze[i][j]=="E" or maze[i][j]=="◍"):
                print(Fore.GREEN+maze[i][j],end="  ")
        print()
    
    print(Fore.RESET)   #Reset colors
    
    PrintPath(result)  #function calling for indexs of path 
    
    
                   

                      
def main():
    global maze
    print("1. Print the Path")
    print("2. Generate another Puzzle")
    print("3. Exit the Game")
    choose=input("Enter your choice: ")
    
    if(choose=="1"):
        result=PathFind(N,maze)
        Path_Marking(result,maze)
    elif(choose=="2"):
        maze=[]
        GenerateMaze(maze) 
    elif(choose=="3"):
        print("Exit...!")        

      





#maze funtion  calling
GenerateMaze(maze)

#Reset colors
print(Fore.RESET)
