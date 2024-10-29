import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os


def new_file() :
        global file
        root.title('Untitled')
        file = None
        text.delete(1.0, 'end')                             # Delete everything from 0th character of 1 line till end


def open_file() :
        global file
        file = filedialog.askopenfilename(defaultextension= '.txt', filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        
        if file == "" :
               try:
                      root.title(os.path.basename(file))
                      text.delete(1.0, 'end')
                      with open(file, 'r') as f:
                             text.insert(1.0, f.read())
               except Exception as e:
                      messagebox.showerror("Error", f"Could not open file: {e}")


def save_file() :
        global file
        if file is None:
               file = filedialog.asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt', filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
               if not file:
                     file = None 
               else: 
                     try:
                            with open(file, 'w') as f:
                                   f.write(text.get(1.0, 'end'))
                            root.title(os.path.basename(file))
                            messagebox.showinfo('Save', "File saved successfully!")
                     except Exception as e:
                            messagebox.showerror("Error", f"Could not save file: {e}")
        else:
                try:
                     with open(file, 'w') as f:
                        f.write(text.get(1.0, 'end'))
                     messagebox.showinfo('Save', "File saved successfully!")
                except Exception as e:
                     messagebox.showerror("Error", f"Could not save file: {e}")


def save_file_as() :
        global file
        file = filedialog.asksaveasfilename(defaultextension= '.txt', filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        
        if file: 
                try:
                       with open(file, 'w') as f:
                              f.write(text.get(1.0, 'end'))
                       root.title(os.path.basename(file))
                       messagebox.showinfo('Save', f"File saved as {os.path.basename(file)}")
                except Exception as e:
                       messagebox.showerror("Error", f"Could not save file as: {e}")


def exit_app():
    if messagebox.askyesno("Exit", "Would you like to save changes before exiting?"):
        save_file()  
    root.destroy()  


def cut() :
        text.event_generate("<<Cut>>")

def copy() :
        text.event_generate("<<Copy>>")

def paste() :
        text.event_generate("<<Paste>>")

def delete():
    try:
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete the selected text?")
        if confirm:
            text.delete("sel.first", "sel.last")
    except tk.TclError:
        messagebox.showinfo("Delete", "No text selected to delete.")



def dark_theme() :
       text.config(bg="black", fg="white", insertbackground="white")
       root.config(bg="black")
       main_menu.config(bg="black", fg="white")


def light_theme() :
       text.config(bg="white", fg="black", insertbackground="black")
       root.config(bg="white")
       main_menu.config(bg="white", fg="black")


def info() :
        messagebox.showinfo('About the Notepad', "This Notepad is created by Shubha on 27th Oct 2024")


if __name__ == '__main__' :
        
        root = tk.Tk()


        # SCREEN 
        root.geometry('1152x635')
        root.title('Notepad')
        #root.wm_iconbitmap()


        # TEXT AREA
        text = tk.Text(root, undo=True, wrap="word")                                            
        text.pack(fill='both', expand=True, ipadx=20, ipady=20)
        file = None


        # SCROLL BAR
        scroll = tk.Scrollbar(text)
        scroll.pack(side='right', fill='y')
        scroll.config(command = text.yview)
        text.config(yscrollcommand= scroll.set)


        # MENU BAR
        main_menu = tk.Menu(root)

        file_menu = tk.Menu(main_menu, tearoff = 0)
        file_menu.add_command(label = 'New', command = new_file)
        file_menu.add_command(label = 'Open', command = open_file)
        file_menu.add_command(label = 'Save', command = save_file)
        file_menu.add_command(label = 'Save As', command = save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label = 'Exit', command = exit_app)
        main_menu.add_cascade(label='File', menu=file_menu)

        edit_menu = tk.Menu(main_menu, tearoff = 0)
        edit_menu.add_command(label = 'Cut', command = cut)
        edit_menu.add_command(label = 'Copy', command = copy)
        edit_menu.add_command(label = 'Paste', command = paste)
        edit_menu.add_command(label = 'Delete', command = delete)
        #edit_menu.add_separator()
        main_menu.add_cascade(label='Edit', menu=edit_menu)

        view_menu = tk.Menu(main_menu, tearoff = 0)
        theme = tk.Menu(view_menu, tearoff=0)
        theme.add_command(label='Dark', command=dark_theme)
        theme.add_command(label='Light', command=light_theme)
        view_menu.add_cascade(label='Theme', menu = theme)
        view_menu.add_separator()
        view_menu.add_command(label = 'About', command = info)
        main_menu.add_cascade(label='View', menu = view_menu)

        root.config(menu=main_menu)

        root.mainloop()
