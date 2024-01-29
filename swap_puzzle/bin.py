sorted=[list(range(i*self.n+1, (i+1)*self.n+1)) for i in range(self.m)]
        """
       Creates a list equal to the sorted grid
        """
if sorted==self.state: return True
else: return False

assert(A==self.state)

for right in range (j,self.n-1):
                Solution.append(((i,right),(i,right+1)))
                self.swap((i,right),(i,right+1))
            for up in range (i-goal[0]):
                Solution.append(((i-up,self.n-1),(i-up-1,self.n-1)))
                self.swap((i-up,self.n-1),(i-up-1,self.n-1))
            for left in range (j-goal[1]):
                Solution.append(((goal[0],self.n-1-left),(goal[0],self.n-left-2)))
                self.swap((goal[0],self.n-1-left),(goal[0],self.n-left-2))

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
            
            if(i,j) != goal:
                for right in range (j,self.n-1):
                    Solution.append(((i,right),(i,right+1)))
                    self.swap((i,right),(i,right+1))
                for up in range (i-goal[0]):
                    Solution.append(((i-up,self.n-1),(i-up-1,self.n-1)))
                    self.swap((i-up,self.n-1),(i-up-1,self.n-1))
                for left in range (j-goal[1]):
                    Solution.append(((goal[0],self.n-1-left),(goal[0],self.n-left-2)))
                    self.swap((goal[0],self.n-1-left),(goal[0],self.n-left-2))


        return Solution      

for i in range(6,2, -1):
        print(i)