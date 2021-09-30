import numpy as np
from tkinter import messagebox

# this function is used to validate the max and min fields so they can have only numbers


def callback_isdigit(input):
    if input == "" or input == "-":
        return True
    try:
        float(input)
    except Exception:
        return False
    return True


# used for input validation of function field and to call plot if the input is valid.
# if input is invalid it opens a message box to help the user.


def validate(function_field, min_field, max_field, subplot, canvas):
    y_str = function_field.get()
    min_str = min_field.get()
    max_str = max_field.get()

    isValid = True
    # check empty function field
    if len(y_str) == 0 or y_str.isspace():
        messagebox.showwarning("Missing Field", "Empty function field")
        isValid = False
    # check empty minimum field
    elif len(min_str) == 0:
        messagebox.showwarning("Missing Field", "Missing minimum value field")
        isValid = False
    # check empty maximum field
    elif len(max_str) == 0:
        messagebox.showwarning("Missing Field", "Missing maximum value field")
        isValid = False
    # check if max <= min
    elif float(min_str) >= float(max_str):
        messagebox.showwarning(
            "Wrong Input", "Maximum value should be greater than Minumum value"
        )
        isValid = False
    # checks if function field contains a non valid character.
    for i in y_str:
        if not i.isdigit() and i not in [
            "x",
            "*",
            "+",
            "-",
            "/",
            "^",
            " ",
            ".",
            "(",
            ")",
        ]:
            messagebox.showwarning(
                "Invalid Input",
                'f(x) can only contain valid characters\n\t"x,+,-,*,/,^,.,(,)"',
            )
            isValid = False
            break
    # prevents the input from containing ** which is invalid and can be used as power
    if "**" in y_str:
        messagebox.showerror("Error", "Invalid math expression")
        isValid = False
    # if the input is valid call plot function
    if isValid is True:
        plot(function_field, min_field, max_field, subplot, canvas)


# plots the graph into the subplot


def plot(function_field, min_field, max_field, subplot, canvas):
    # get user input
    y = str(function_field.get()).replace("^", "**")
    min = float(min_field.get())
    max = float(max_field.get())
    x = np.linspace(min, max, 1000)

    # evaluate the user entered function if it's not valid it outputs a message.
    try:
        y = eval(y)
    except Exception:
        messagebox.showerror("Error", "Invalid math expression")
    # should work if f(x) equals a constant to fix dimensions
    if "x" not in function_field.get():
        y = np.full(x.shape, y)

    # clears the previous plot and plots a new one using scientific notation ticks.
    subplot.clear()
    subplot.plot(x, y)
    subplot.ticklabel_format(useMathText=True, axis="both")
    canvas.draw()
