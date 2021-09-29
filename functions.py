import numpy as np
from tkinter import messagebox


def callback_isdigit(input):
    if input == "" or input == "-":
        return True
    try:
        float(input)
    except Exception:
        return False
    return True


def validate(function_field, min_field, max_field, subplot, canvas):
    y_str = function_field.get()
    min_str = min_field.get()
    max_str = max_field.get()

    isValid = True
    if len(y_str) == 0 or y_str.isspace():
        messagebox.showwarning("Missing Field", "Empty function field")
        isValid = False
    elif len(min_str) == 0:
        messagebox.showwarning("Missing Field", "Missing minimum value field")
        isValid = False
    elif len(max_str) == 0:
        messagebox.showwarning("Missing Field", "Missing maximum value field")
        isValid = False
    elif float(min_str) >= float(max_str):
        messagebox.showwarning("Wrong Input", "max field should be more than min field")
        isValid = False

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

    if "**" in y_str:
        messagebox.showerror("Error", "Invalid math expression")
        isValid = False

    if isValid is True:
        plot(function_field, min_field, max_field, subplot, canvas)


def plot(function_field, min_field, max_field, subplot, canvas):
    y = str(function_field.get()).replace("^", "**")
    min = float(min_field.get())
    max = float(max_field.get())
    x = np.linspace(min, max, 1000)

    try:
        y = eval(y)
    except Exception:
        messagebox.showerror("Error", "Invalid math expression")

    if "x" not in function_field.get():
        y = np.full(x.shape, y)

    subplot.clear()
    subplot.plot(x, y)
    subplot.ticklabel_format(useMathText=True, axis="both")
    canvas.draw()
