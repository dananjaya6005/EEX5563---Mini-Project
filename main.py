import tkinter as tk
from tkinter import messagebox
from memory_manager import firstFit
from tkinter import ttk


class MemoryAllocatorApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x400")
        self.root.title("EEX5563 - Memory Allocator")
        
        self.block_size_label = tk.Label(root, text="Block Sizes (comma separated):", font=('Helvetica', 12 , 'bold') )
        self.block_size_label.pack(padx=10, pady=10)
        self.block_size_entry = tk.Entry(root , font=('Helvetica', 12 ) ,width= 40)
        self.block_size_entry.pack(ipadx=10, ipady=6 )

        self.process_size_label = tk.Label(root, text="Process Sizes (comma separated):", font=('Helvetica', 12 , 'bold'))
        self.process_size_label.pack( padx=10, pady=10)
        self.process_size_entry = tk.Entry(root , font=('Helvetica', 12 ) ,width= 40)
        self.process_size_entry.pack( ipadx=10, ipady=6)

        self.allocate_button = tk.Button(root, text="Allocate", command=self.allocate , font=('Helvetica', 12 , 'bold') , bg='#B25068' , fg='white' , width= 20)
        self.allocate_button.pack(padx=10, pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    # Set up the result table
        self.result_table = ttk.Treeview(root, columns=("process_no", "process_size", "block_no"), show='headings')
        self.result_table.heading("process_no", text="Process No.")
        self.result_table.heading("process_size", text="Process Size")
        self.result_table.heading("block_no", text="Block No.")
        self.result_table.pack()
        


        

    def allocate(self):
        block_sizes = list(map(int, self.block_size_entry.get().split(',')))
        process_sizes = list(map(int, self.process_size_entry.get().split(',')))
        m = len(block_sizes)
        n = len(process_sizes)

        allocation = firstFit(block_sizes, m, process_sizes, n)
        print(allocation)
        

        #insert the data into the table

        for i in range(n):
            if allocation[i] != -1:
                self.result_table.insert("", "end", values=(i+1, process_sizes[i], allocation[i]+1))
            else:
                self.result_table.insert("", "end", values=(i+1, process_sizes[i], "Not Allocated"))


    
def main():
    root = tk.Tk()
    app = MemoryAllocatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
