import tkinter as tk
from tkinter import ttk

# Class representing the Prevent Transfer Overrides UI panel
class PreventTransferOverridesPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()  # Build the UI elements

    def create_widgets(self):
        # ---------------------------------------------------
        # Header Section: Title and refresh button
        # ---------------------------------------------------
        header_frame = ttk.Frame(self)
        header_frame.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        title_label = ttk.Label(
            header_frame,
            text="Prevent Transfer Overrides",
            font=("Arial", 14, "bold")
        )
        title_label.pack(side="left")

        refresh_button = ttk.Button(header_frame, text="🔄")
        refresh_button.pack(side="right")

        # ---------------------------------------------------
        # Instruction Section: Note text in blue
        # ---------------------------------------------------
        instruction_label = ttk.Label(
            self,
            text="NOTE: If you want to manage your overrides manually...",
            foreground="blue",  # Blue text for instructions
            wraplength=400,
            justify="left"
        )
        instruction_label.grid(row=1, column=0, columnspan=2, sticky="w", padx=5, pady=2)

        # ---------------------------------------------------
        # Warning Section: Warning text in red with bold font
        # ---------------------------------------------------
        warning_label = ttk.Label(
            self,
            text="WARNING: Adding dinos to this list will prevent them from being transferred...",
            foreground="red",  # Red text for warning
            wraplength=400,
            justify="left",
            font=("Arial", 10, "bold")
        )
        warning_label.grid(row=2, column=0, columnspan=2, sticky="w", padx=5, pady=2)

        # ---------------------------------------------------
        # Control Buttons Section: Add, Edit, and Remove buttons
        # ---------------------------------------------------
        button_frame = ttk.Frame(self)
        button_frame.grid(row=3, column=0, sticky="w", padx=5, pady=5)

        add_button = ttk.Button(button_frame, text="+")
        add_button.pack(side="left", padx=2)

        edit_button = ttk.Button(button_frame, text="✏️")
        edit_button.pack(side="left", padx=2)

        remove_button = ttk.Button(button_frame, text="❌")
        remove_button.pack(side="left", padx=2)

        # ---------------------------------------------------
        # Data Table Section: Treeview table with vertical scrollbar
        # ---------------------------------------------------
        table_frame = ttk.Frame(self)
        table_frame.grid(row=4, column=0, sticky="nsew", padx=5, pady=5)

        # Configure grid weights so the table expands with the window
        self.rowconfigure(4, weight=1)
        self.columnconfigure(0, weight=1)
        table_frame.rowconfigure(0, weight=1)
        table_frame.columnconfigure(0, weight=1)

        # Define the Treeview with one column ("Dino")
        columns = ("Dino",)
        tree = ttk.Treeview(table_frame, columns=columns, show="headings")
        tree.heading("Dino", text="Dino")
        tree.insert("", tk.END, values=("Dino",))  # Insert an example row
        tree.grid(row=0, column=0, sticky="nsew")

        # Create and attach a vertical scrollbar to the Treeview
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")

# ---------------------------------------------------
# Main function to run the UI as a standalone application
# ---------------------------------------------------
def main():
    root = tk.Tk()
    root.title("Prevent Transfer Overrides")
    root.geometry("600x400")  # Set a starting window size

    # Create and pack the PreventTransferOverridesPanel into the root window
    panel = PreventTransferOverridesPanel(root)
    panel.pack(fill="both", expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()
