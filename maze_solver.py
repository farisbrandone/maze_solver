from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self,width,height):
        self.weight=width
        self.height=height
        self.__root=Tk()
        self.__root.title("my first application in tkinter")
        self.__canvas=Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__state_of_windows=False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    def wait_for_close(self):
        self.__state_of_windows=True
        while self.__state_of_windows:
            self.redraw()
        print("window closed...")
    def close(self):
        self.state_of_windows=False
    def draw_line(self, line,fill_color="blue"):
        line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
class Line:
    def __init__(self, p1,p2):
        self.p1=p1
        self.p2=p2
    def draw(self, canvas, fill_color="white"):
        canvas.create_line(
    self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
)
        canvas.pack(fill=BOTH, expand=1) 

class Cell:
    def __init__(self,_win
):
        self.has_left_wall=True
        self.has_right_wall=True
        self.has_top_wall=True
        self.has_bottom_wall=True
        self._x1=None
        self._x2=None
        self._y1=None
        self._y2=None
        self._win=_win
        self.visited=False

    def draw(self,x1, y1,x2,y2):
        self._x1=x1
        self._y1=y1
        self._x2=x2
        self._y2=y2
        if self.has_left_wall :
            self._win.draw_line(Line(Point(x1, y1),
                                 Point(x1, y2)))
        if not self.has_left_wall :
            self._win.draw_line(Line(Point(x1, y1),
                                 Point(x1, y2)), "white")
        if self.has_top_wall :
            self._win.draw_line(Line(Point(x1, y1),
                                 Point(x2, y1))) 
        if not self.has_top_wall:
             self._win.draw_line(Line(Point(x1, y1),
                                 Point(x2, y1)), "white")
        if self.has_right_wall :
            self._win.draw_line(Line(Point(x2, y1),
                                 Point(x2, y2))) 
        if not self.has_right_wall:
            self._win.draw_line(Line(Point(x2, y1),
                                 Point(x2, y2)), "white")
        if self.has_bottom_wall :
            self._win.draw_line(Line(Point(x1, y2),
                                 Point(x2, y2)))
        if not self.has_bottom_wall:
            self._win.draw_line(Line(Point(x1, y2),
                                 Point(x2, y2)), "white")
            
    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        x_mid = (self._x1 + self._x2) / 2
        y_mid = (self._y1 + self._y2) / 2

        to_x_mid = (to_cell._x1 + to_cell._x2) / 2
        to_y_mid = (to_cell._y1 + to_cell._y2) / 2

        fill_color = "red"
        if undo:
            fill_color = "gray"

        if self._x1 > to_cell._x1:
            line = Line(Point(self._x1, y_mid), Point(x_mid, y_mid))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_y_mid), Point(to_cell._x2, to_y_mid))
            self._win.draw_line(line, fill_color)

        elif self._x1 < to_cell._x1:
            line = Line(Point(x_mid, y_mid), Point(self._x2, y_mid))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_cell._x1, to_y_mid), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, fill_color)

        elif self._y1 > to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y1))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_cell._y2), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, fill_color)

        elif self._y1 < to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y2))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_y_mid), Point(to_x_mid, to_cell._y1))
            self._win.draw_line(line, fill_color) 




    


        