#cd slip26
# python GUI_slip26_Q2_B.py

# Write  Python  GUI  program  which  accepts  a  sentence  from  the  user  and  alters  it 
# when  a  button  is  pressed.  Every  space  should  be  replaced  by  *,  case  of  all  alphabets 
# should be reversed, digits are replaced by?

import tkinter as tk

def alter_sentence():
    input_text = entry.get()
    altered_text = ''.join('*' if char == ' ' else char.swapcase() if char.isalpha() else '?' for char in input_text)
    result_label.config(text=altered_text)

root = tk.Tk()
root.title("Sentence Alterer")

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

alter_button = tk.Button(root, text="Alter Sentence", command=alter_sentence)
alter_button.pack(pady=5)

result_label = tk.Label(root, text="", wraplength=400)
result_label.pack(pady=10)

root.mainloop()
