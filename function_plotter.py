# Import libraries
from functions import *
from tkinter import ttk
from ttkthemes import ThemedTk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure



# define window and theme
root = ThemedTk(theme="arc")
style = ttk.Style(root)
style.configure('Label', background= 'white')
root.configure(bg= 'white')
root.title("Function Plotter")
root.resizable(False, False)

reg_isdigit=root.register(callback_isdigit)
# reg_function=root.register(callback_function)

#input fields
function_field = ttk.Entry(root, width = 35)
# function_field.config(validate="key", validatecommand=(reg_function, '%P'))

min_field = ttk.Entry(root)
min_field.config(validate="key", validatecommand=(reg_isdigit, '%P'))

max_field = ttk.Entry(root)
max_field.config(validate="key", validatecommand=(reg_isdigit, '%P'))

#labels
function_field_label = ttk.Label(root, style= 'Label', text = "Enter f(x)\n\t\t\ta*x^b+ c*x^d")
min_field_label = ttk.Label(root, style= 'Label', text = "Minimum")
max_field_label = ttk.Label(root, style= 'Label', text = "Maximum")
    
plot_btn = ttk.Button(root, text="Plot", command=lambda:validate(function_field, min_field, max_field, subplot, canvas))

#defining the plot
figure = Figure(figsize = (4,4), dpi = 100)
subplot = figure.add_subplot(111) 
canvas = FigureCanvasTkAgg(figure)

#pushing everything into the screen

function_field_label.grid(row = 0, column = 0, columnspan = 3, sticky='S'+'W', padx=10 ,pady= 5)
function_field.grid(row = 1, column = 0, columnspan = 2, padx=10, sticky = 'N')

min_field_label.grid(row = 2, column = 0 , sticky = 'N', pady= 5)
min_field.grid(row = 2, column = 1, sticky = 'N')
max_field_label.grid(row = 3, column = 0, padx = 3, sticky = 'N', pady= 5)
max_field.grid(row = 3, column = 1, padx = 3, sticky = 'N')

plot_btn.grid(row = 4, columnspan=2, column=0, sticky = 'N')
canvas.get_tk_widget().grid(row=0, rowspan=5, columnspan=4, column = 4, ipadx=10)




root.mainloop()