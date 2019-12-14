import tkinter as tk 

def circle(dist, radius_1, radius_2):
    rad_sq = (radius_1+radius_2)**2
    dist *= dist 
    if dist == rad_sq:
        return 1 
    elif dist < rad_sq:
        return -1 
    else:
        return 0 
    
class App:
    def __init__(self):
        self.app = tk.Tk()

        Labels = ['Distance', 'Radius Of Circle 1', 'Radius of Circle 2', 'Output: ']

        
        self.CANVAS_WIDTH = 600
        self.CANVAS_HEIGHT = 600 

        self.outputs = ['Circles don\'t intersect', 'Circles are tangent to each other', 'Circles Intersect at two points.']

        self.frame = tk.Frame(self.app)
        self.frame.grid(row=0, column=0)

        self.canvas = tk.Canvas(self.app, height=self.CANVAS_HEIGHT, width=self.CANVAS_WIDTH, background='white')
        self.canvas.grid(row=0, column=1)

        self.StringVars = [tk.StringVar() for _ in range(len(Labels))]

        Entries = [tk.Entry(self.frame, textvariable=self.StringVars[i]) for i in range(len(Labels))]
        for i in range(len(Labels)-1):
            tk.Label(self.frame, text=Labels[i]).grid(row=i)
            Entries[i].grid(row=i, column=1)
            Entries[i].bind('<KeyRelease>', self.onKeyPressed)

        i = 3
        tk.Label(self.frame, textvariable=self.StringVars[i]).grid(row=i)

        self.app.mainloop()

    def onKeyPressed(self, event):
        try:
            self.canvas.delete('all')
            d = int(self.StringVars[0].get())

            radius_1 = int(self.StringVars[1].get())
            radius_2 = int(self.StringVars[2].get())


            width = self.canvas.winfo_width()
            height = self.canvas.winfo_height()


            x1, y1 = self.CANVAS_WIDTH/2, self.CANVAS_WIDTH/2

            #x1, y1 = radius_1, radius_1
            x2, y2 = x1+d, y1

            self.canvas.create_oval(x1-radius_1, y1-radius_1, x1+radius_1, y1+radius_1)
            self.canvas.create_oval(x2-radius_2, y2-radius_2, x2+radius_2, y2+radius_2)
            
            if d == 0:
                output = 'Circles are concentric.'
            else:
                output = self.outputs[circle(d, radius_1, radius_2)]

            self.StringVars[-1].set(f'Output:\n{output}')

        except Exception as e:
            pass

def main():
    App()

if __name__ == "__main__":
    main()