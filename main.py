from tkinter import *

morse_code_dict = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',
    'E': '.',      'F': '..-.',   'G': '--.',    'H': '....',
    'I': '..',     'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',    'P': '.--.',
    'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
    'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    '0': '-----',  '1': '.----',  '2': '..---',  '3': '...--',
    '4': '....-',  '5': '.....',  '6': '-....',  '7': '--...',
    '8': '---..',  '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..',  "'": '.----.',
    '!': '-.-.--', '/': '-..-.',  '(': '-.--.',   ')': '-.--.-',
    '&': '.-...',  ':': '---...', ';': '-.-.-.',  '=': '-...-',
    '+': '.-.-.',  '-': '-....-', '_': '..--.-',  '"': '.-..-.',
    '$': '...-..-','@': '.--.-.', '¿': '..-.-',   '¡': '--...-',
    ' ': '/'
}

def generateMorse() :
    fetching_text = input_text.get().upper()
    morse_text_list = [morse_code_dict[character] for character in fetching_text]
    morse_text = "  ".join(morse_text_list)
    morse_output.config(text=morse_text)




window = Tk()
window.title("Morse Code Translation")
window.geometry("900x500")
text = Label(window, text="Enter Your text : ", font=("Consola", 14, "bold"))
text.place(x=10, y=200)
input_text = Entry(window, font=("Consola", 16), width=50)
input_text.place(x=180, y=199)
morse_text_label = Label(window, text="Morse Code : ", font=("Consola", 14, "bold"))
morse_text_label.place(x=10, y=300)
morse_output = Label(window, text="", font=("Consola", 24, "bold"), wraplength=700, state="disabled")
morse_output.place(x=190, y=300)
submit_button = Button(window, text="Generate a Morse code", bg="green", fg="black", activebackground="green", font=("Consola", 14, "bold"), command=generateMorse)
submit_button.place(x=150, y=420)


window.mainloop()



