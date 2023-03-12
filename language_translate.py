from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox

root = Tk()
root.title("Aysu Language Translator")
root.geometry("870x300")

def translate():
    output_text.delete(1.0, END)

    for key, value in languages.items():
        if (value == input_combo.get()):
            from_language_key = key

    for key, value in languages.items():
        if (value == output_combo.get()):
            to_language_key = key
        
    text = textblob.TextBlob(input_text.get(1.0,END))

    text = text.translate(from_lang = from_language_key, to = to_language_key)

    output_text.insert(1.0, text)

    #except Exception as e:
        #messagebox.showerror("Translator", e)

def clear():
    input_text.delete(1.0, END)
    output_text.delete(1.0, END)

languages = googletrans.LANGUAGES
language_list = list(languages.values())

input_combo = ttk.Combobox(root, width = 50, value=language_list)
input_combo.current(21)
input_combo.grid(row = 0, column=0)

output_combo = ttk.Combobox(root, width = 50, value=language_list)
output_combo.current(26)
output_combo.grid(row = 0, column=2)

input_text = Text(root, height=8, width=40)
input_text.grid(row=1, column=0,pady=40, padx=20)

translate_button = Button(root, text="Translate", command=translate)
translate_button.grid(row=1, column=1, pady=40, padx=20)

output_text = Text(root, height=8, width=40)
output_text.grid(row=1, column=2, pady=40, padx=20)

clear_button =Button(root, text="Clear", height=2, width=8, command=clear)
clear_button.grid(row=2, column=1)
mainloop()