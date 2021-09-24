# Import libraries
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

root = Tk()
root.geometry("750x250")
function_field = Entry(root, width= 100)
function_field.pack()

min_field = Entry(root, width = 20)
max_field = Entry(root, width = 20)
min_field.pack()
max_field.pack()

def plot():
    min = float(min_field.get())
    max = float(max_field.get())
    x = np.linspace(min, max, 1000)
    y = str(function_field.get()).replace("^", "**")
    y = eval(y)
    fig = plt.figure(figsize = (10, 5))
    # Create the plot
    plt.plot(x, y)
  
    # Show the plot
    plt.show()

plot_btn = Button(root, text="Plot", command=plot)
plot_btn.pack()

root.mainloop()