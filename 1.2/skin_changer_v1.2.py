from os import path, listdir, mkdir
from PIL import Image

dir_path = path.dirname(path.abspath(__file__))

if not path.exists(dir_path+'/skin/'):
    mkdir(dir_path+'/skin') 
if not path.exists(dir_path+'/preset/'):
    mkdir(dir_path+'/preset') 

list_skin = [skin for skin in listdir(dir_path) if (skin.endswith('.png'))]
list_preset = [preset for preset in listdir(dir_path+'/preset/') if preset.endswith('.png')]


def apply_preset(name_skin, name_preset):
    global dir_path
    global nb

    skin = Image.open(dir_path+'/'+name_skin)
    skin = skin.convert("RGBA")
    data_skin = skin.getdata()

    preset = Image.open(dir_path+'/preset/'+name_preset)
    preset = preset.convert("RGB")
    data_preset = preset.getdata()

    new_skin_data = []
    for item in range(len(data_skin)):
        if data_preset[item] != (0, 0, 0) and data_preset[item] != (255, 255, 255):
            new_skin_data.append((data_preset[item][0], data_preset[item][1], data_preset[item][2], 255))
        elif data_preset[item] == (255, 255, 255):
            new_skin_data.append((0, 0, 0, 0))
        else:
            new_skin_data.append(data_skin[item])

    skin.putdata(new_skin_data)
    skin.save(dir_path+"/skin/"+name_skin[:-4]+"_"+name_preset)


if len(list_skin) == 0:
    print('ERROR no skin detected')
    print()

if len(list_preset) == 0:
    print('ERROR no preset detected')
    print()

if len(list_skin) != 0 and len(list_preset) != 0:
    for skin in list_skin:
        for preset in list_preset:
            apply_preset(skin, preset)
