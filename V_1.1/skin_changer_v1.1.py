from PIL import Image

lst_presset = ["presset_comrad1.png", "presset_serveur1.png", "presset_serveur2.png", "presset_costar1.png", "presset_costar2.png", "presset_tv_head.png", "blank_skin.png", "blank_skin.png", "presset_technoblade.png", "presset_maid.png", "presset_pain.png", "presset_empereur.png", "presset_vagabon.png", "presset_roi.png"]

for z in range(len(lst_presset)):
    seuil_de_noir = 69
    moins_noir = 150
    skin_original = Image.open("skin/skin_original.png")
    skin_original = skin_original.convert("RGBA")
    data = skin_original.getdata()

    skin_blank = Image.open("preset/blank_skin.png")
    skin_blank = skin_blank.convert("RGB")
    datablank = skin_blank.getdata()

# modification du skin
    new_skin_data = []

    if z == 6 or z == 7:
        for item in range(len(data)):
            if data[item] <= 3*(seuil_de_noir, ):
                if z == 6:
                    new_skin_data.append((255 - data[item][0], 255 - data[item][1], 255 - data[item][2], data[item][3]))
                else:
                    new_skin_data.append((data[item][0] + moins_noir, data[item][1] + moins_noir, data[item][2] + moins_noir, data[item][3]))
            else:
                new_skin_data.append(data[item])

    else:
        skin_preset = Image.open("preset/"+str(lst_presset[z]))
        skin_preset = skin_preset.convert("RGB")
        presetdata = skin_preset.getdata()
        for item in range(len(data)):
            if presetdata[item] != (0, 0, 0) and presetdata[item] != (255, 255, 255):
                new_skin_data.append((presetdata[item][0], presetdata[item][1], presetdata[item][2], 255))
            elif presetdata[item] >= (255, 255, 255):
                new_skin_data.append((0, 0, 0, 0))
            else:
                new_skin_data.append(data[item])

    skin_original.putdata(new_skin_data)
    skin_original.save("skin/skin_modifié_"+str(z)+str(lst_presset[z]))
