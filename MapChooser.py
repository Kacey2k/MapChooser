import tkinter as tk
import random

# we solve pratice problems.
def random_map():
    maps = ['pl_badwater', 'pl_badwater', 'pl_badwater', 'pl_badwater', 'pl_badwater', 'pl_badwater', 'pl_badwater', 'pl_badwater', 'pl_badwater', 'pl_badwater', 'pl_badwater', 'pl_badwater', 'pl_badwater', 'pl_badwater', 'pl_badwater', 'pl_badwater', 'pl_badwater', 'pl_pier']
    chosen_map = random.choice(maps)
    output_field.config(text=chosen_map)

# window
root = tk.Tk()
root.title("TF2 Map Picker 5000")
# text
text_label = tk.Label(root, text="Which map should I play today?", font=("Arial", 16))
text_label.pack(pady=20)
# button
roll_button = tk.Button(root, text="Pick Random Map!", command=random_map)
roll_button.pack(pady=10)
# output
output_field = tk.Label(root, text="", font=("Arial", 14), fg="blue")
output_field.pack(pady=20)

root.mainloop()
