import tkinter as tk
from Window import Window

def main():
    root = tk.Tk()
    root.title("Contact Book")
    root.geometry("750x750")

    app = Window(root)
    root.mainloop()

if __name__ == "__main__":
    main()
