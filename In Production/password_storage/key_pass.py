#author: Mark Minchoff

#import library
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox, ttk
import pandas as pd


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        #configuration
        self.geometry("800x600")
        self.title("Password Manager")
        self.resizable(False, False)
        self.pack_propagate(False)
        menubar = Menu(self)
        self.config(menu=menubar)

        #file menu options
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open File", command=lambda: File_dialog())
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        # load menu options
        loadmenu = Menu(menubar, tearoff=0)
        loadmenu.add_command(label="Load File", command=lambda: Load_excel_data())
        menubar.add_cascade(label="Load", menu=loadmenu)

        #Frame for File Pathway
        file_frame = tk.LabelFrame(self, text="File Pathway")
        file_frame.place(height=60, width=320, relx=.01, x=1)

        #Frame to Edit Data
        update_frame = tk.LabelFrame(self, text="Data Edit")
        update_frame.place(height=100, width=400, relx=.01, x=350)

        #Frame for Data Display
        frame1 = tk.LabelFrame(self, text="Passwords")
        frame1.place(width=785, height=450, rely=.23, relx=.01)
        
        label_file = ttk.Label(file_frame, text="No File Selected",wraplength=300)
        label_file.place(x=4)

        #Creating a tree view with scroll bars for Data Display
        tv1 = ttk.Treeview(frame1)
        tv1.place(x=1, height=411, width=761)
        treescrolly = tk.Scrollbar(frame1,orient="vertical",command=tv1.yview)
        treescrollx = tk.Scrollbar(frame1, orient="horizontal",command=tv1.xview)
        tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
        
        treescrollx.pack(side="bottom", fill="x")
        treescrolly.pack(side="right", fill="y")

        #treeview style
        style = ttk.Style()
        style.theme_use("default")
        tv1.tag_configure('oddrow', background="white")
        tv1.tag_configure('evenrow', background="lightblue")

        #Edit Data
        entry1_label = tk.Label(update_frame, text='Username: ')
        entry1_label.place(x=1)
        entry2_label = tk.Label(update_frame, text='Password: ')
        entry2_label.place(x=1, y=35)
        entry1 = tk.Entry(update_frame)
        entry1.place(x=70)
        entry2 = tk.Entry(update_frame)
        entry2.place(x=70, y=35)

    
        #comamnd/function for finding file to be read
        def File_dialog():
            
            filename = filedialog.askopenfilename(initialdir="/",
                                                  title="Select A File",
                                                  filetype=(("xlsx files", "*.xlsx"),("All Files", "*.*")))
            label_file["text"] = filename
            return None

        def Load_excel_data():
            
            file_path = label_file["text"]
            global count
            count = 0 
            
            try:
                excel_filename = r"{}".format(file_path)
                if excel_filename[-4:] == ".csv":
                    df = pd.read_csv(excel_filename)
                else:
                    df = pd.read_excel(excel_filename)
            except NameError:
                messagebox.showerror('Python Error', 'Pandas was not imported to code!')
                return None
            except ValueError:
                tk.messagebox.showerror("Information", "The file you have chosen is invalid")
                return None
            except FileNotFoundError:
                tk.messagebox.showerror("Information", f"No such file as {file_path}")
                return None

            clear_data()

            tv1["column"] = list(df.columns)
            tv1["show"] = "headings"

          
            for column in tv1["columns"]:
                tv1.heading(column, text=column, anchor='center') # let the column heading = column name
                tv1.column(column, minwidth=0, width=100, stretch=NO, anchor='center')
            
            df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
           


            for row in df_rows:
                if count %2 == 0:
                    tv1.insert("", "end", values=row,tags='evenrow') # inserts each list into the treeview. 
                else:
                    tv1.insert("", "end", values=row,tags='oddrow')
                count += 1

        # i am unsure what the hell this does
        def clear_data():
            tv1.delete(*tv1.get_children())
            return None



if __name__ == "__main__":
    app = App()
    app.mainloop()

