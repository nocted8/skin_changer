from os import path, listdir, mkdir
from PIL import Image

dir_path = path.dirname(path.abspath(__file__))

if not path.exists(dir_path+'/preset/'):
    mkdir(dir_path+'/preset') 

list_preset = [preset for preset in listdir(dir_path+'/preset/') if preset.endswith('.png')]


def preset_updater(preset_name):
    global dir_path

    preset = Image.open(dir_path+'/preset/'+preset_name)
    preset = preset.convert("RGBA")
    data_preset = preset.get_flattened_data() 

    updated_preset = []
    for item in range(len(data_preset)):
        if (data_preset[item][0], data_preset[item][1], data_preset[item][2]) == (255, 255, 255) or data_preset[item][3] == 0:
            updated_preset.append((255, 255, 255, 0))
        elif (data_preset[item][0], data_preset[item][1], data_preset[item][2]) == (0, 0, 0):
            updated_preset.append((0, 0, 0, 255))
        else:
            updated_preset.append(data_preset[item])

    preset.putdata(updated_preset)
    preset.save(dir_path+"/preset/"+preset_name)


if len(list_preset) == 0:
    print('ERROR no preset detected\n')
else:
    for preset in list_preset:
        preset_updater(preset)
    print("preset updated to v1.2.3 standards\n")
