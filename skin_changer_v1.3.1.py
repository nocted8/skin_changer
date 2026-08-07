from os import path, listdir, mkdir, sys
import webbrowser
from tkinter import*
import tkinter as tk
from PIL import Image


abs_pth = path.abspath(sys.argv[0])
dir_path = path.dirname(abs_pth)

if not path.exists(dir_path+'/skin/'):
    mkdir(dir_path+'/skin') 
if not path.exists(dir_path+'/preset/'):
    mkdir(dir_path+'/preset') 


root = tk.Tk()
root.title("SkinChangerV1.3.1")

window_width = 300
window_height = 100

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(str(window_width)+"x"+str(window_height)+"+"+str(center_x)+"+"+str(center_y))
root.resizable(False, False)
root.attributes('-topmost', 1)


def open_repo():
    webbrowser.open("https://github.com/nocted8/skin_changer")


def open_preset_repo():
    webbrowser.open("https://github.com/nocted8/skin_changer/tree/main/latest_presets")


def apply_preset(name_skin, name_preset):
    global dir_path

    skin = Image.open(dir_path+'/'+name_skin)
    skin = skin.convert("RGBA")
    data_skin = skin.get_flattened_data()

    preset = Image.open(dir_path+'/preset/'+name_preset)
    preset = preset.convert("RGBA")
    data_preset = preset.get_flattened_data()

    new_skin_data = []
    for item in range(len(data_skin)):
        if data_preset[item] != (0, 0, 0, 255):
            new_skin_data.append((data_preset[item]))
        else:
            new_skin_data.append(data_skin[item])

    skin.putdata(new_skin_data)
    skin.save(dir_path+"/skin/"+name_skin[:-4]+"_"+name_preset)


def main():
    global dir_path

    list_skin = [skin for skin in listdir(dir_path) if (skin.endswith('.png'))]
    list_preset = [preset for preset in listdir(dir_path+'/preset/') if preset.endswith('.png')]

    end_result = ""

    if len(list_skin) == 0:
        end_result += 'ERROR no skin detected\n'
        end_text_color = 'red'

    if len(list_preset) == 0:
        end_result += 'ERROR no preset detected\n'
        end_text_color = 'red'

    if len(list_skin) != 0 and len(list_preset) != 0:
        for skin in list_skin:
            for preset in list_preset:
                apply_preset(skin, preset)
        end_result += "program executed with succes\n"
        end_text_color = 'green'

    end_text = StringVar()
    texte = Label(root, textvariable=end_text, fg=end_text_color)
    texte.pack()

    end_text.set(end_result[:-1])
    tk.Button(root, text="check for update", command=open_repo, bg="yellow").pack()
    tk.Button(root, text="download more presets", command=open_preset_repo, bg="yellow").pack()
    root.mainloop()


if __name__ == "__main__":
    main()