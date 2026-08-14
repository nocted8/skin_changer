#######################################
#                                     #
#            dev by nocted            #
#     wallpapers by Brique_de_lait    #
#                                     #
#######################################
from os import path, listdir, mkdir, sys, remove
import webbrowser
from tkinter import*
import tkinter as tk
from PIL import Image
from random import randint
import subprocess


abs_pth = path.abspath(sys.argv[0])
dir_path = path.dirname(abs_pth)


def goto_repo():
    webbrowser.open("https://github.com/nocted8/skin_changer")

def goto_preset():
    webbrowser.open("https://github.com/nocted8/skin_changer/tree/main/latest_presets")

def open_skin_dir():
    subprocess.Popen(r'explorer /select,'+dir_path)

if not path.exists(dir_path+'\\skin'):
    mkdir(dir_path+'\\skin') 
if not path.exists(dir_path+'\\preset'):
    mkdir(dir_path+'\\preset')
if not path.exists(dir_path+'\\ui_image'):
    mkdir(dir_path+'\\ui_image') 
if not path.exists(dir_path+'\\ui_image\\wallpaper'):
    mkdir(dir_path+'\\ui_image\\wallpaper') 

list_skin = [skin for skin in listdir(dir_path) if (skin.endswith('.png'))]
list_preset = [preset for preset in listdir(dir_path+'\\preset\\') if preset.endswith('.png')]

if path.exists(dir_path+'\\ui_image\\wallpaper\\'):
    list_wallpaper = [wallpaper for wallpaper in listdir(dir_path+'\\ui_image\\wallpaper\\')]


root = tk.Tk()
root.title("SkinChanger_V1.4")

root.resizable(False, False)
root.attributes('-topmost', 1)

text_color = '#000000'
widget_color = '#404040'
background_color = '#303030'


def set_window_size( window_width, window_height):

    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    root.geometry(str(window_width)+"x"+str(window_height)+"+"+str(center_x)+"+"+str(center_y))


if len(list_skin)==0 or len(list_preset)==0:

    preset_label_text = StringVar()
    skin_label_text = StringVar()

    if len(list_preset)==0:
        preset_label_text.set("missing preset ERROR")
        preset_label_color = 'red'
    else:
        preset_label_text.set("preset OK")
        preset_label_color = 'green'
    if len(list_skin)==0:
        skin_label_text.set("missing skin ERROR")
        skin_label_color = 'red'
    else:
        skin_label_text.set("skin OK")
        skin_label_color = 'green'

    preset_label = Label( root, textvariable=preset_label_text, bg=widget_color, fg=preset_label_color)
    preset_label.grid(column=0, row=0, sticky="nsew")
    skin_label = Label( root, textvariable=skin_label_text, bg=widget_color, fg=skin_label_color)
    skin_label.grid(column=1, row=0, sticky="nsew")
    preset_button = Button(root, text="click here to open the repo's presets", bg=widget_color, fg=text_color, command=goto_preset)
    preset_button.grid(column=0, row=1)
    skin_button = Button(root, text="click here to open where to put your skin", bg=widget_color, fg=text_color, command=open_skin_dir)
    skin_button.grid(column=1, row=1)
    repo_button = Button(root, text="click here to open the SkinChanger repo", bg=widget_color, fg=text_color, command=goto_repo)
    repo_button.grid(column=0, columnspan=2, row=3, sticky="nsew")



else:
    set_window_size(599, 300)
    if path.exists(dir_path+"\\ui_image\\app_icon.ico"):
        app_icon = PhotoImage(file = dir_path+"\\ui_image\\app_icon.ico")
        root.iconphoto(False, app_icon)
    elif path.exists(dir_path+"\\ui_image\\app_icon.png"):
        app_icon = PhotoImage(file = dir_path+"\\ui_image\\app_icon.png")
        root.iconphoto(False, app_icon)

    if len(list_wallpaper) > 0:
        wallpaper_path = dir_path+'\\ui_image\\wallpaper\\'+list_wallpaper[randint(0, len(list_wallpaper)-1)]
        wallpaper_image = PhotoImage(file = wallpaper_path)
        wallpaper = Label( root, image = wallpaper_image)
        wallpaper.place(x = -2, y = -2)
    else:
        root.configure(bg=background_color)


    #lists
    preset_listbox_list = StringVar()
    preset_listbox_list.set(list_preset)
    preset_listbox = Listbox(root, listvariable=preset_listbox_list , bg=widget_color, fg=text_color)
    skin_listbox_list = StringVar()
    skin_listbox_list.set(list_skin)
    skin_listbox = Listbox(root, listvariable=skin_listbox_list , bg=widget_color, fg=text_color)

    preset_listbox.grid(column=0, row=0, rowspan=5) 
    skin_listbox.grid(column=4, row=0, rowspan=5)

    #log label
    log_label_text = StringVar()
    log_labell_color = StringVar()
    log_labell_color.set("green")

    def load_log():
        log_label = Label( root, textvariable=log_label_text, bg=widget_color, fg=log_labell_color.get())
        log_label.grid(column=1, columnspan=3, row=0, sticky="news") 
    load_log()

    def supah_secreh_function():
        webbrowser.open("https://youtu.be/Aq5WXmQQooo?si=uzVpMUq5fk1uszXM")
    
    if randint(1, 100) == 1:
        root.attributes('-alpha',0.5)
        log_label_text.set("oooh phantom ahh window oooh")
        log_labell_color.set("white")
        load_log()

    #images preview
    preview_preset_path = StringVar()
    preview_preset_path.set(dir_path+'\\preset\\'+list_preset[0])
    preset_name = StringVar()
    preset_name.set(preview_preset_path.get().rsplit('\\')[-1])
    preview_skin_path = StringVar()
    preview_skin_path.set(dir_path+'\\'+list_skin[0])
    skin_name = StringVar()
    skin_name.set(preview_skin_path.get().rsplit('\\')[-1])

    def apply_preset(skin_path, preset_path, is_preview=False):
        global dir_path

        skin = Image.open(skin_path)
        skin = skin.convert("RGBA")
        data_skin = skin.get_flattened_data()
        
        if preset_path != "":
            preset = Image.open(preset_path)
            preset = preset.convert("RGBA")
            data_preset = preset.get_flattened_data()

            new_skin_data = []
            for item in range(len(data_skin)):
                if data_preset[item] != (0, 0, 0, 255):
                    new_skin_data.append((data_preset[item]))
                else:
                    new_skin_data.append(data_skin[item])
        else:
            new_skin_data = data_skin

        skin.putdata(new_skin_data)
        if is_preview == False:
            skin.save(dir_path+'\\skin\\'+skin_path.rsplit('\\')[-1][:-4]+"_"+preset_path.rsplit('\\')[-1])
        else:
            skin.save(dir_path+'\\ui_image\\preseted_skin_preview.png')

    if path.exists(dir_path+'\\ui_image\\preseted_skin_preview.png'):
        remove(dir_path+'\\ui_image\\preseted_skin_preview.png')
    apply_preset(dir_path+'\\'+list_skin[0], dir_path+'\\preset\\'+list_preset[0], True)
    preview_preseted_skin_path = StringVar()
    preview_preseted_skin_path.set(dir_path+'\\ui_image\\preseted_skin_preview.png')
    preview_preseted_skin_order = []


    def load_preset_preview():
        global dir_path, list_preset
        preset_preview_image = PhotoImage(file = preview_preset_path.get())
        preset_preview_label = Label( root, image = preset_preview_image, bg=widget_color)
        preset_preview_label.image = preset_preview_image
        preset_preview_label.config(image=preset_preview_image)
        preset_preview_label.grid(column=1, row=1)
    
    def load_skin_preview():
        global dir_path, list_skin
        skin_preview_image = PhotoImage(file = preview_skin_path.get())
        skin_preview_label = Label( root, image = skin_preview_image, bg=widget_color)
        skin_preview_label.image = skin_preview_image
        skin_preview_label.config(image=skin_preview_image)
        skin_preview_label.grid(column=3, row=1)
    
    def load_preseted_skin_preview(order):
        global dir_path
        apply_preset(preview_skin_path.get(), "", True)
        for preset in order:
            apply_preset(preview_preseted_skin_path.get(), dir_path+'\\preset\\'+preset, True)
        preseted_skin_preview_image = PhotoImage(file = preview_preseted_skin_path.get())
        preseted_skin_preview_label = Label( root, image = preseted_skin_preview_image, bg=widget_color)
        preseted_skin_preview_label.image = preseted_skin_preview_image
        preseted_skin_preview_label.config(image=preseted_skin_preview_image)
        preseted_skin_preview_label.grid(column=2, row=1)

    load_preset_preview()
    load_preseted_skin_preview(preview_preseted_skin_order)
    load_skin_preview()


    # buttons funstions
    def apply_this_one():
        apply_preset(preview_skin_path.get(), preview_preset_path.get())
        log_label_text.set("succes")
        log_labell_color.set("green")
        load_log()

    def apply_on_all_skins():
        previous_preview_skin_path = preview_skin_path.get()
        for skin in list_skin:
            preview_skin_path.set(dir_path+'\\'+skin)
            apply_this_one()
        preview_skin_path.set(previous_preview_skin_path)

    def use_as_input():
        already = 0
        for i in range(len(preview_preseted_skin_order)):
            if preview_preseted_skin_order[i] == preview_preset_path.get().rsplit('\\')[-1]:
                already += 1
                preview_preseted_skin_order.pop(i)
        preview_skin_path.set(preview_preseted_skin_path.get())
        load_skin_preview()
        if already == 1:
            skin_name.set(skin_name.get()[:-4]+"_"+preset_name.get())
            preview_preseted_skin_order.append(preset_name.get())
        load_preseted_skin_preview(preview_preseted_skin_order)
        log_label_text.set("succes")
        log_labell_color.set("green")
        load_log()

    def apply_everything():
        previous_preview_skin_path = preview_skin_path.get()
        previous_preview_preset_path = preview_preset_path.get()
        for preset in list_preset:
            preview_preset_path.set(dir_path+'\\preset\\'+preset)
            for skin in list_skin:
                preview_skin_path.set(dir_path+'\\'+skin)
                apply_this_one()
        preview_skin_path.set(previous_preview_skin_path)
        preview_preset_path.set(previous_preview_preset_path)

    def apply_with_all_presets():
        previous_preview_preset_path = preview_preset_path.get()
        for preset in list_preset:
            preview_preset_path.set(dir_path+'\\preset\\'+preset)
            apply_this_one()
        preview_preset_path.set(previous_preview_preset_path)
    
    def confirm_selected_preset():
        if len(preset_listbox.curselection()) > 0:
            selected_preset = list_preset[preset_listbox.curselection()[0]]
            preview_preset_path.set(dir_path+'\\preset\\'+selected_preset)
            load_preset_preview()
            preset_name.set(preview_preset_path.get().rsplit('\\')[-1])
            preview_list = [x for x in preview_preseted_skin_order]
            preview_list.append(preset_name.get())
            load_preseted_skin_preview(preview_list)
            log_label_text.set("succes")
            log_labell_color.set("green")
            load_log()
        else:
            log_label_text.set("select a preset first")
            log_labell_color.set("red")
            load_log()

    def confirm_selected_skin():
        if len(skin_listbox.curselection()) > 0:
            selected_skin = list_skin[skin_listbox.curselection()[0]]
            preview_skin_path.set(dir_path+'\\'+selected_skin)
            load_skin_preview()
            skin_name.set(preview_skin_path.get().rsplit('\\')[-1])
            preview_preseted_skin_order = [preset_name.get()]
            load_preseted_skin_preview(preview_preseted_skin_order)
            log_label_text.set("succes")
            log_labell_color.set("green")
            load_log()
        else:
            log_label_text.set("select a skin first")
            log_labell_color.set("red")
            load_log()


    #buttons
    button_goto_repo = Button(              root, text="  open project's repo ", bg=widget_color, fg=text_color, command=goto_repo)
    button_confirm_preset = Button(         root, text="    confirm preset    ", bg=widget_color, fg=text_color, command=confirm_selected_preset)
    button_apply_on_all_skins = Button(     root, text="  apply on all skins  ", bg=widget_color, fg=text_color, command=apply_on_all_skins)
    button_apply_this_one = Button(         root, text="    apply this one    ", bg=widget_color, fg=text_color, command=apply_this_one)
    button_use_as_input = Button(           root, text="     use as input     ", bg=widget_color, fg=text_color, command=use_as_input)
    button_apply_everything = Button(       root, text="   apply everything   ", bg=widget_color, fg=text_color, command=apply_everything)
    button_apply_with_all_presets = Button( root, text="apply with all presets", bg=widget_color, fg=text_color, command=apply_with_all_presets)
    button_confirm_skin = Button(           root, text="     confirm skin     ", bg=widget_color, fg=text_color, command=confirm_selected_skin)
    button_goto_preset = Button(            root, text="     open presets     ", bg=widget_color, fg=text_color, command=goto_preset)

    button_goto_repo.grid(              column=0, row=6, sticky="news")
    button_confirm_preset.grid(         column=0, row=5, sticky="news")
    button_apply_on_all_skins.grid(     column=1, row=2, sticky="news")
    button_apply_this_one.grid(         column=2, row=2, sticky="news")
    button_use_as_input.grid(           column=2, row=3, sticky="news")
    button_apply_everything.grid(       column=2, row=4, sticky="news")
    button_apply_with_all_presets.grid( column=3, row=2, sticky="news")
    button_confirm_skin.grid(           column=4, row=5, sticky="news")
    button_goto_preset.grid(            column=4, row=6, sticky="news")

    if randint(1,100) == 1:
        button_supah_secreh = Button(root, text="da supah secreh button", bg='#AAAAAA', fg=text_color, command=supah_secreh_function)
        button_supah_secreh.place(x = 400, y = 200)

root.mainloop()
