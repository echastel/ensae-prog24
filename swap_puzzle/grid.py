"""
This is the grid module. It contains the Grid class and its associated methods.
"""
from graph import Graph
import random
import matplotlib.pyplot as plt
import itertools
import copy

class Grid():
    """
    A class representing the grid from the swap puzzle. It supports rectangular grids. 

    Attributes: 
    -----------
    m: int
        Number of lines in the grid
    n: int
        Number of columns in the grid
    state: list[list[int]]
        The state of the grid, a list of list such that state[i][j] is the number in the cell (i, j), i.e., in the i-th line and j-th column. 
        Note: lines are numbered 0..m and columns are numbered 0..n.
    """
    
    def __init__(self, m, n, initial_state = []):
        """
        Initializes the grid.

        Parameters: 
        -----------
        m: int
            Number of lines in the grid
        n: int
            Number of columns in the grid
        initial_state: list[list[int]]
            The intiail state of the grid. Default is empty (then the grid is created sorted).
        """
        self.m = m
        self.n = n
        if not initial_state:
            initial_state = [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]            
        self.state = initial_state

    def __str__(self): 
        """
        Prints the state of the grid as text.
        """
        output = f"The grid is in the following state:\n"
        for i in range(self.m): 
            output += f"{self.state[i]}\n"
        return output

    def __repr__(self): 
        """
        Returns a representation of the grid with number of rows and columns.
        """
        return f"<grid.Grid: m={self.m}, n={self.n}>"

    def is_sorted(self):
        """
        Checks is the current state of the grid is sorte and returns the answer as a boolean.
        """
        k=1
        for i in range (self.m):
            for j in range (self.n):
                if self.state[i][j]!=k :
                    return False
                else : k+=1
        return True

    def swap(self, cell1, cell2):
        """
        Implements the swap operation between two cells. Raises an exception if the swap is not allowed.

        Parameters: 
        -----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the column number of the cell. 
        """
        i1,j1,i2,j2=cell1[0],cell1[1],cell2[0],cell2[1]
        if i1>self.m or i2>self.m or j1>self.n or j2>self.n or (abs(i1-i2)+abs(j1-j2)>1) :# we make sure the swap is "legal"
            print(f"swap",(i1,j1),(i2,j2), "is impossible")
        else : 
            old_cell1= self.state[i1][j1]
            self.state[i1][j1]=self.state[i2][j2]
            self.state[i2][j2]=old_cell1

    def swap_seq(self, cell_pair_list):
        """
        Executes a sequence of swaps. 

        Parameters: 
        -----------
        cell_pair_list: list[tuple[tuple[int]]]
            List of swaps, each swap being a tuple of two cells (each cell being a tuple of integers). 
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
        #we're just calling several times the swap method we just defined to make this new method
        for i in cell_pair_list:
            self.swap(i[0],i[1])
    
    def matrix_to_tuple(self,G1):
        """
        "Transforms" a grid into a tuple.
        Returns a tuple that lists the numbers in the grid, 
        (from the top left corner to the bottom right corner) 

        Parameters: 
        -----------
        G1: list
            The list you want to transform in a tuple (has to be the same size as "self")
        """
        Sum=[]
        for i in G1:
            Sum+=i
        Grid_tuple = tuple(Sum)
        return Grid_tuple

    def get_graph(self):
        """
        Returns a graph where the nodes are all the possible states the grid could be in

        """
        Dots=[]
        for i in self.state :
            for j in i :
                Dots.append(j)
        #Dots is a list of the nodes
        Nodes = list(itertools.permutations(Dots))
        self.graph=Graph(Nodes)  #we're defining the attribute graph of the class grid
        L=len(Nodes)
        for i in range(L) :
            for j in range(i+1,L) :
                if self.there_is_a_swap(Nodes[i],Nodes[j]) :
                    self.graph.add_edge(Nodes[i],Nodes[j])
        return(self.graph)

    

    def there_is_a_swap(self,G1,G2):
        """
        Determines if two grids are separated only by a swap, 
        i.e. if you can go from the grid G1 to the grid G2 by swapping to numbers in G1
        Parameters: 
        -----------
        G1: tuple
            The ordered tuple of the nodes of the first grid(has to be the same size as "self")
            you want to compare with G2 to see if you could go from G1 to G2 with a single swap.
        G2: tuple
            The ordered tuple of the nodes of the second grid(has to be the same size as "self")
            you want to compare with G1 to see if you could go from G1 to G2 with a single swap.
        """

        diff=[]
        for i in range (len(G1)):
            if G1[i]!=G2[i] :
                diff.append(i)
        if len(diff)!=2: 
            return False
        else : #we made sure that exactly two numbers had changed positions between G1 and G2
            #now we convert the respective indexes of the two differences into their position
            # in the grid
            pos1=(diff[0]//self.n,diff[0]%self.n-1)
            pos2=(diff[1]//self.n,diff[1]%self.n-1)
            i1,j1=pos1[0],pos1[1]
            i2,j2=pos2[0],pos2[1]
            G1=self.tuple_to_matrix(G1)
            G2=self.tuple_to_matrix(G2)
            if i1>self.m or i2>self.m or j1>self.n or j2>self.n or (abs(i1-i2)+abs(j1-j2)>1) :
                return False
        return True

    def tuple_to_matrix (self,G) :
        """
        "transforms" a tuple into a grid.
        Returns a list[list[int]] with the numbers in the order described by the tuple

        Parameters: 
        -----------
        G: tuple
            The tuple is ordered, the grid this method returns will have the same dimension as "self"
        """
        L=[[]]
        for k in G[0:self.n]:
            L[0].append(k)
        for i in range (1,self.m):
            L.append([])
            for k in G[i*self.n:(i+1)*self.n]:
                L[i].append(k)
        return L

    def position (self,value):
        """
        Returns a tuple (i,j) representing the position of "value" in the grid
        i is the lign "value" is in 
        j is the column "value" is in 

        Parameters: 
        -----------
        value: int
            The value whose position you want to get
        """
        for i in range (self.m):
            for j in range (self.n):
                if self.state[i][j]==value:
                    return (i,j)
    
    def print_grid (self): #représentation graphique séance 1 question 4
        fig,ax = plt.subplots()
        #hide axes
        fig.patch.set_visible(False)
        ax.axis('off')
        ax.axis('tight')
        ax=plt.table(cellText=self.state,cellLoc='center')
        fig.tight_layout()
        plt.show()

    def get_solution(self):
            """
            Solves the grid and returns the sequence of swaps at the format 
            [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
            """
            solved=Grid(self.m,self.n)
            Solution=[] 
        
            for k in range (1, self.m*self.n+1):
                    (i,j)=self.position(k) #the position of the value k in the given grid
                    goal= solved.position(k)
                    print((i,j))
                    if j> goal[1]: # if the value is too much to the right
                            for left in range (j-goal[1]):
                                    
                                    Solution.append(((i,j-left),(i,j-left-1)))
                                    self.swap((i,j-left),(i,j-left-1))
                    if j< goal[1]: # if the value is too much to the left
                            for right in range (j, goal[1]):

                                    Solution.append(((i,right),(i,right+1)))
                                    self.swap((i,right),(i,right+1))
                    if i > goal[0]: # if the value is not on the correct line
                            for up in range (i, goal[0], -1):
                                    Solution.append(((up,goal[1]),(up - 1,goal[1])))
                                    self.swap((up,goal[1]),(up-1,goal[1]))
            return Solution 

    def get_solution2 (self):
        """
            Solves the grid and returns the sequence of swaps at the format 
            [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        solved=[list(range(i*self.n+1, (i+1)*self.n+1)) for i in range(self.m)] 
        dst=self.matrix_to_tuple(solved)
        src=self.matrix_to_tuple(self.state)
        G=self.get_graph()
        Seq=G.bfs(src,dst)
        Seq_Grid=[]
        for i in Seq:
            Seq_Grid.append(self.tuple_to_matrix(i))
        Solution=[]
        for k in range(len(Seq)-1):
            Solution.append(self.find_swap(Seq_Grid[k],Seq_Grid[k+1]))
        return Solution

    def get_solution_q8(self):
        
        """
        Finds a shortest path from self.state to solved by BFS.  

        Output: 
        -------
        path_current: list[tuple(tuple)] | None
            The shortest swap sequence from src to dst. Returns None if dst is not reachable from src
        """ 
        dst=[list(range(i*self.n+1, (i+1)*self.n+1)) for i in range(self.m)] 
        src=self.state
        list_of_swaps=[]
        for i in range (self.m -1):
            for j in range(self.n -1):
                list_of_swaps.append(((i,j),(i,j+1)))
                list_of_swaps.append(((i,j),(i+1,j)))
        list_of_swaps.append(((self.m-1,self.n-2),(self.m-1,self.n-1)))
        list_of_swaps.append(((self.m-2,self.n-1),(self.m-1,self.n-1)))
        
        
        Been_there=[]
        To_explore=[]
        
        
        To_explore.append((src,[]))
        
        while len(To_explore)>0 :
            current, path_current=To_explore.pop(0)
            Been_there.append(current)
            if current == dst:
                Been_there.append(current)
                return(path_current)
                        
            for i in list_of_swaps: 
                neighbor= self.swap_matrix(current,i)
                if neighbor not in Been_there and neighbor not in [i[0] for i in To_explore]:
                    New_path=copy.deepcopy(path_current)+[i]
                    To_explore.append((neighbor, New_path))
        return None
    
    def swap_matrix(self, matrix, swap):
        point1=swap[0]
        
        point2=swap[1]
        
        new_matrix=copy.deepcopy(matrix)
        new_matrix[point1[0]][point1[1]],new_matrix[point2[0]][point2[1]]= matrix[point2[0]][point2[1]],matrix[point1[0]][point1[1]]
        return(new_matrix)

    def find_swap(self,G1,G2):
        """
        Determines the swap that allows you to go 
        from the grid in the state G1 
        to the grid in the state G2 
        
        Parameters: 
        -----------
        G1: list
            
        G2: list
            
        """
        
        print(G1,G2)
        for i in range (len(G1)) :
            for j in range (len(G1[0])) :
                if G1[i][j] != G2[i][j]:
                    if j+1<self.n:
                        if G1[i][j]==G2[i][j+1] :
                            return ((i,j),(i,j+1))
                    if i+1<self.m:
                        if G1[i][j]==G2[i+1][j] :
                            return ((i,j),(i+1,j))

    @classmethod
    def grid_from_file(cls, file_name): 
        """
        Creates a grid object from class Grid, initialized with the information from the file file_name.
        
        Parameters: 
        -----------
        file_name: str
            Name of the file to load. The file must be of the format: 
            - first line contains "m n" 
            - next m lines contain n integers that represent the state of the corresponding cell

        Output: 
        -------
        grid: Grid
            The grid
        """
        with open(file_name, "r") as file:
            m, n = map(int, file.readline().split())
            initial_state = [[] for i_line in range(m)]
            for i_line in range(m):
                line_state = list(map(int, file.readline().split()))
                if len(line_state) != n: 
                    raise Exception("Format incorrect")
                initial_state[i_line] = line_state
            grid = Grid(m, n, initial_state)
        return grid


