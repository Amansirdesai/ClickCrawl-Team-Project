import tkinter as tk
from tkinter import messagebox
import base64

def decrypt():
    password = code.get()

    if password == "1234":
        screen2 = tk.Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = text1.get("1.0", tk.END).strip()
        try:
            decoded_message = base64.b64decode(message).decode("ascii")
        except base64.binascii.Error as e:
            decoded_message = f"Decryption error: {e}"

        tk.Label(screen2, text="DECRYPT", font="arial", fg="White", bg="#00bd56").place(x=10, y=10)
        text2 = tk.Text(screen2, font="Roboto 10", bg="White", relief=tk.GROOVE, wrap=tk.WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(tk.END, decoded_message)

    elif password == "":
        messagebox.showerror("Decryption", "Input Password")
    elif password != "1234":
        messagebox.showerror("Decryption", "Invalid Password")


def encrypt():
    password = code.get()

    if password == "1234":
        screen1 = tk.Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get("1.0", tk.END)
        encoded_message = base64.b64encode(message.encode("ascii")).decode("ascii")

        tk.Label(screen1, text="ENCRYPT", font="arial", fg="White", bg="#ed3833").place(x=10, y=10)
        text2 = tk.Text(screen1, font="Roboto 10", bg="White", relief=tk.GROOVE, wrap=tk.WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(tk.END, encoded_message)

    elif password == "":
        messagebox.showerror("Encryption", "Input Password")
    elif password != "1234":
        messagebox.showerror("Encryption", "Invalid Password")


def main_screen():
    global screen, code, text1

    screen = tk.Tk()
    screen.geometry("375x398")
    screen.title("PctApp")

    try:
        image_icon = tk.PhotoImage(file="Keys.png")
        screen.iconphoto(False, image_icon)
    except tk.TclError:
        print("Warning: Could not load icon file.")

    def reset():
        code.set("")
        text1.delete("1.0", tk.END)

    tk.Label(screen, text="Enter text for encryption and decryption", fg="black", font=("Times New Roman", 13)).place(x=10, y=10)
    text1 = tk.Text(screen, font="Roboto 20", bg="white", relief=tk.GROOVE, wrap=tk.WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    tk.Label(screen, text="Enter Secret key for encryption and decryption", fg="black", font=("Times New Roman", 13)).place(x=10, y=170)
    code = tk.StringVar()
    tk.Entry(screen, textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)

    tk.Button(screen, text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    tk.Button(screen, text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    tk.Button(screen, text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)

    screen.mainloop()

if __name__ == "__main__":
    main_screen()






