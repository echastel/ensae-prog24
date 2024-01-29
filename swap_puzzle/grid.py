"""
This is the grid module. It contains the Grid class and its associated methods.
"""

import random

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
        if i1>i2+1 or i2>i1+1 or j1>j2+1 or j2>j1+1 or i1>self.m or i2>self.m or j1>self.n or j2>self.n:
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
        for i in cell_pair_list:
            self.swap(i[0],i[1])

    def position (self,value):
        for i in range (self.m):
            for j in range (self.n):
                if self.state[i][j]==value:
                    return (i,j)
    
    

    def get_solution(self):
            """
            Solves the grid and returns the sequence of swaps at the format 
            [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
            """
            sorted=Grid(self.m,self.n)
            Solution=[] 
        
            for k in range (1, self.m*self.n+1):
                    (i,j)=self.position(k) #the position of the value k in the given grid
                    goal= sorted.position(k)
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


