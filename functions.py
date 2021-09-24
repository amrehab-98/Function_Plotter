import numpy as np
from tkinter import messagebox


def callback_isdigit(input):
    if input == "" or input == "-":
        return True
    try:

        float(input)
    except:
        return False
    return True

# def callback_function(input):
#     if (input[-1] in ['x','*','+','-','/','^',' ','.'] or input[-1].isdigit()):
#         print(input)
#         return True
                        
#     elif input == "":
#         return True

#     else:
#         messagebox.showinfo("Invalid Input", "please enter a number or a valid character \"x,+,-,*,/,^,.\"")
#         return False


def validate(function_field, min_field, max_field, subplot, canvas):
    passed = True
    y_string = str(function_field.get())
    for i in y_string:
        if not i.isdigit() and i not in ['x','*','+','-','/','^',' ','.']:
            messagebox.showinfo("Invalid Input", "f(x) can only contain valid characters\n\t\"x,+,-,*,/,^,.\"")
            passed = False
            break

    if passed:
        plot_callback(function_field, min_field, max_field, subplot, canvas)
def plot_callback(function_field, min_field, max_field, subplot, canvas):
    y = str(function_field.get()).replace("^", "**")
    min = float(min_field.get())
    max = float(max_field.get())
    x = np.linspace(min, max, 1000)
    y = eval(y)
    subplot.clear()
    subplot.plot(x, y)
    subplot.ticklabel_format(useMathText=True, axis='both')
    canvas.draw()