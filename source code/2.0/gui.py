import customtkinter
from config import*
import json
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

def save_settings():
    with open("settings.txt", "w") as f:
        settings = {
            "slider_value": slider_1.get(),
            "entry_text": entry_1.get(),
            "text": text_1.get("1.0", "end-1c")
        }
        json.dump(settings, f)

def load_settings():
    try:
        with open("settings.txt", "r") as f:
            settings = json.load(f)
            slider_1.set(settings["slider_value"])
            entry_1.set(settings["entry_text"])
            text_1.delete("1.0", "end")
            text_1.insert("1.0", settings["text"])
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        pass

app = customtkinter.CTk()
app.geometry("400x700")
app.title("gibel client 2.0")
'''
autoholdtk = StringVar()
autoholdtk.set(autohold)
hotKeyclikertk = StringVar()
hotKeyclikertk.set(hotKeycliker)
hotKeyTrigertk = StringVar()
hotKeyTrigertk.set(hotKeyTriger)
bind1tk = StringVar()
bind1tk.set(bind1tk)
'''
def slider_callback(value):
    progressbar_1.set(value)

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT)
label_1.pack(pady=10, padx=10)

progressbar_1 = customtkinter.CTkProgressBar(master=frame_1)
progressbar_1.pack(pady=10, padx=10)

slider_1 = customtkinter.CTkSlider(master=frame_1, command=slider_callback, from_=0, to=1)
slider_1.pack(pady=10, padx=10)
slider_1.set(0.5)
"""
entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="your bind1:",textvariable=autoholdtk)
entry_1.pack(pady=10, padx=10)

entry_2 = customtkinter.CTkEntry(master=frame_1, placeholder_text="clicker bind:",textvariable=hotKeyclikertk)
entry_2.pack(pady=10, padx=10)

entry_3 = customtkinter.CTkEntry(master=frame_1, placeholder_text="triger bind:",textvariable=hotKeyTrigertk)
entry_3.pack(pady=10, padx=10)

entry_4 = customtkinter.CTkEntry(master=frame_1, placeholder_text="your bind1:",textvariable=bind1tk)
entry_4.pack(pady=10, padx=10)

entry_5 = customtkinter.CTkEntry(master=frame_1, placeholder_text="your hotkey for bind1:",textvariable=hotKeyBind1)
entry_5.pack(pady=10, padx=10)
"""
entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="your bind1:")
entry_1.pack(pady=10, padx=10)

entry_2 = customtkinter.CTkEntry(master=frame_1, placeholder_text="clicker bind:")
entry_2.pack(pady=10, padx=10)

entry_3 = customtkinter.CTkEntry(master=frame_1, placeholder_text="triger bind:")
entry_3.pack(pady=10, padx=10)

entry_4 = customtkinter.CTkEntry(master=frame_1, placeholder_text="your bind1:")
entry_4.pack(pady=10, padx=10)

entry_5 = customtkinter.CTkEntry(master=frame_1, placeholder_text="your hotkey for bind1:")
entry_5.pack(pady=10, padx=10)
button_1 = customtkinter.CTkButton(master=frame_1,text="TriggreBot")
button_1.pack(pady=10, padx=10)


button_2 = customtkinter.CTkButton(master=frame_1,text="clicker")
button_2.pack(pady=10, padx=10)

text_1 = customtkinter.CTkTextbox(master=frame_1, width=200, height=70)
text_1.pack(pady=10, padx=10)
text_1.insert("0.0", "hello we developers are ready to present you version 2.0 it includes 1 GUI 2 autoclicker 3 hold auto clicker 4 trigger bot 5 and 1 bind most likely you hear about our client for the first time and we want to list it as a possibility and the first thing is that it will never be found everything is recorded from the monitor screen and cannot be found by checking for cheats simple file-config txt files are installed everywhere and everyone can fix their own there save takecheat is written in simple python language which allows it to be easy to write")

button_save = customtkinter.CTkButton(master=frame_1,text="Сохранить", command=save_settings)
button_save.pack(pady=10, padx=10)

button_load = customtkinter.CTkButton(master=frame_1,text="Загрузить", command=load_settings)
button_load.pack(pady=10, padx=10)

app.mainloop()
