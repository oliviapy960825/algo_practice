"""
305. Number of Islands II

A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1,1,2,3]
Explanation:

Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
Follow up:

Can you do it in time complexity O(k log mn), where k is the length of the positions?
"""
DIRECTIONS=[(0,1),(0,-1),(1,0),(-1,0)]

class Solution:
    def find(self,x):
        path=[]
        while x!=self.father[x]:
            path.append(x)
            x=self.father[x]
        for i in path:
            self.father[i]=x
        return x
    def union(self,x,y):
        root_x=self.find(x)
        root_y=self.find(y)
        
        if root_x!=root_y:
            self.father[root_x]=root_y
            self.size-=1
            
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        result=[]
        island=set()
        self.size=0
        self.father={}
        for operator in positions:
            x,y=operator[0],operator[1]
            if (x,y) in island:
                result.append(self.size)
                continue
                
            island.add((x,y))
            self.father[(x,y)]=(x,y)
            self.size+=1
            for (d_x,d_y) in DIRECTIONS:
                x_=x+d_x
                y_=y+d_y
                if (x_,y_) in island:
                    self.union((x_,y_),(x,y))
                    
            result.append(self.size)
            
        return result
            
            