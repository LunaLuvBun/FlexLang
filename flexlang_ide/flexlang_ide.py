import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os
import subprocess

class FlexLangIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("FlexLang IDE")
        self.file_path = ""
        self.project_path = ""

        # Set up the menu
        self.menu = tk.Menu(root)
        self.root.config(menu=self.menu)

        # Add File menu
        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New Project", command=self.new_project)
        self.file_menu.add_command(label="Open Project", command=self.open_project)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Run Game", command=self.run_game)
        self.file_menu.add_command(label="Exit", command=root.quit)

        # Set up the editor
        self.editor = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Consolas", 12))
        self.editor.pack(expand=1, fill='both')

        # Set up the output console
        self.output_console = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10, font=("Consolas", 12), bg="lightgrey")
        self.output_console.pack(fill='x')

    def new_project(self):
        self.project_path = filedialog.askdirectory()
        if not self.project_path:
            return
        os.makedirs(os.path.join(self.project_path, "assets"), exist_ok=True)
        os.makedirs(os.path.join(self.project_path, "scripts"), exist_ok=True)
        messagebox.showinfo("Project Created", f"New project created at {self.project_path}")

    def open_project(self):
        self.project_path = filedialog.askdirectory()
        if not self.project_path:
            return
        self.load_scripts()

    def load_scripts(self):
        scripts_path = os.path.join(self.project_path, "scripts")
        script_files = [f for f in os.listdir(scripts_path) if f.endswith('.fl')]
        self.editor.delete(1.0, tk.END)
        if script_files:
            with open(os.path.join(scripts_path, script_files[0]), 'r') as file:
                self.editor.insert(tk.END, file.read())

    def save_file(self):
        if not self.project_path:
            messagebox.showerror("Error", "No project opened!")
            return
        script_path = filedialog.asksaveasfilename(defaultextension=".fl", initialdir=os.path.join(self.project_path, "scripts"), filetypes=[("FlexLang files", "*.fl"), ("All files", "*.*")])
        if script_path:
            with open(script_path, 'w') as file:
                file.write(self.editor.get(1.0, tk.END))

    def run_game(self):
        if not self.project_path:
            messagebox.showerror("Error", "No project opened!")
            return
        self.output_console.delete(1.0, tk.END)
        try:
            # Here we assume a `flexengine` command exists to run the game
            subprocess.run(["flexengine", self.project_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.output_console.insert(tk.END, "Game is running...\n")
        except subprocess.CalledProcessError as e:
            self.output_console.insert(tk.END, f"Error running game:\n{e.stderr.decode()}\n")

if __name__ == "__main__":
    root = tk.Tk()
    ide = FlexLangIDE(root)
    root.mainloop()
