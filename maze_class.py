from maze_solver import Window, Line,Point, Cell
import random
import time
class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
        seed=None
    ):
        self.x1=x1
        self.y1=y1
        self.num_cols=num_cols
        self.num_rows=num_rows
        self.cell_size_y=cell_size_y
        self.cell_size_x=cell_size_x
        self._win=win
        self._cells=[]
        if seed :
            random.seed(seed)
        self.create_cell()
        self._break_entrance_and_exit()
        self.break_wall_r(0, 0)
        self.reset_cells_method()
        

    
    def create_cell(self):

        for i in range(self.num_rows):
            col_cells = []
            for j in range(self.num_cols):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.draw_cell(i, j)
                

    def draw_cell(self, i, j):
        if self._win is None:
            return
        x1=self.x1 + (j)*self.cell_size_x
        y1=self.y1 + (i)*self.cell_size_y
        x2=self.x1 + (j+1)*self.cell_size_x
        y2=self.y1 + (i+1)*self.cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.02)
    
    def _break_entrance_and_exit(self):
        if self._win is None:
            return
        self._cells[0][0].has_top_wall=False
        self.draw_cell(0,0)
        self._animate()
        self._cells[self.num_rows-1][self.num_cols-1].has_bottom_wall=False
        self.draw_cell(self.num_rows-1,self.num_cols - 1)
        self._animate()
    
    def break_wall_r(self,i,j):
        self._cells[i][j].visited=True
        while True:
            new_list=[]
            if j>0:
                if not self._cells[i][j-1].visited:
                    k=j-1
                    new_list.append([i,k])
            if j+1<self.num_cols:
                if not self._cells[i][j+1].visited:
                    k=j+1
                    new_list.append([i,k])
            if i+1<self.num_rows:
                if not self._cells[i+1][j].visited:
                    k=i+1
                    new_list.append([k,j])
            
            if i>0:
                if not self._cells[i-1][j].visited:
                    k=i-1
                    new_list.append([k,j])
            if len(new_list)==0:
                self.draw_cell(i,j)
                return
            
            ka=random.randrange(len(new_list))
            my=new_list[ka]
            k=my[0]
            l=my[1]
            
            if l==j-1:
                      self._cells[i][j].has_left_wall=False
                      self._cells[k][l].has_right_wall=False
                      
                      
            if l==j+1:
                      self._cells[i][j].has_right_wall=False
                      self._cells[k][l].has_left_wall=False
                      
                      
            if k==i-1:
                      self._cells[i][j].has_top_wall=False
                      self._cells[k][l].has_bottom_wall=False
                      
                      
            if k==i+1:
                      self._cells[i][j].has_bottom_wall=False
                      self._cells[k][l].has_top_wall=False
            self.break_wall_r(k,l)         
                      

    def reset_cells_method(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._cells[i][j].visited=False
    
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self.num_rows - 1 and j == self.num_cols - 1:
            return True

        if (
            i > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i - 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        if (
            i < self.num_rows - 1
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[i + 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        if (
            j > 0
            and not self._cells[i][j].has_left_wall
            and not self._cells[i][j - 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        if (
            j < self.num_cols - 1
            and not self._cells[i][j].has_right_wall
            and not self._cells[i][j + 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        return False
    
    def solve(self):
        return self._solve_r(0,0)
        

        
                

    
    

                  
                      
                  
                
          
            



    



    