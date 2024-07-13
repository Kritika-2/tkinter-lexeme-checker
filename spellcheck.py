
import tkinter as tk
from textblob import TextBlob

def check_spelling():
    word = enter_text.get()
    a = TextBlob(word)
    corrected_word = str(a.correct())
    
    if word.lower() == corrected_word.lower():
        status_label.config(text=f"Text is correct: {corrected_word}", fg="#00ff00")  # Green color for correct text
    else:
        status_label.config(text=f"Text is incorrect: {corrected_word}", fg="#ff0000")  # Red color for incorrect text
    
    meanings = []
    for w in a.words:
        if w.definitions:
            meanings.append(f"{w}: " + ", ".join(w.definitions))
        else:
            meanings.append(f"{w}: No definitions found")
    
    result_window = tk.Toplevel(root)
    result_window.title("Corrected Text and Meaning")
    result_window.geometry("600x300")
    result_window.config(background="#1e1e1e")
    
    cs = tk.Label(result_window, text="Correct text is:", font=("poppins", 20), bg="#1e1e1e", fg="#0db9f0")
    cs.pack(pady=10)
    
    corrected_text = tk.Label(result_window, text=corrected_word, font=("poppins", 20, "bold"), bg="#1e1e1e", fg="#0db9f0")
    corrected_text.pack(pady=10)
    
    meaning_label = tk.Label(result_window, text="Meaning:", font=("poppins", 20), bg="#1e1e1e", fg="#0db9f0")
    meaning_label.pack(pady=10)
    
    meaning_text = tk.Text(result_window, height=5, width=50, font=("poppins", 14), bg="#333333", fg="#ffffff", wrap=tk.WORD)
    for meaning in meanings:
        meaning_text.insert(tk.END, meaning + "\n")
    meaning_text.pack(pady=10)

root = tk.Tk()
root.title("Spelling Checker")
root.geometry("700x400")
root.config(background="#1e1e1e")

heading = tk.Label(root, text="Spelling Checker", font=("Trebuchet MS", 30, "bold"), bg="#1e1e1e", fg="#0db9f0")
heading.pack(pady=(50, 0))

enter_text = tk.Entry(root, justify="center", width=30, font=("poppins", 25), bg="#333333", fg="#ffffff", insertbackground='#ffffff', border=2)
enter_text.pack(pady=10)
enter_text.focus()

button = tk.Button(root, text="Check", font=("arial", 20, "bold"), fg="white", bg="#0db9f0", command=check_spelling)
button.pack(pady=20)

status_label = tk.Label(root, text="", font=("poppins", 14), bg="#1e1e1e")
status_label.pack(pady=(10, 0))

root.mainloop()
