from PIL import Image
seuil_de_noir=69
skin_original = Image.open("skin/skin_original.png")
skin_original = skin_original.convert("RGBA")
data = skin_original.getdata()

skin_blank=Image.open("skin/skin_original.png")
skin_blank = skin_blank.convert("RGBA")
datablank = skin_blank.getdata()

#choix du presset
lst_presset=[("comrad","presset_comrad1.png"),("serveur 1","presset_serveur1.png"),("serveur 2","presset_serveur2.png"),("costar 1","presset_costar1.png"),("costar 2","presset_costar2.png"),("tv head","presset_tv_head.png"),("plus de noir","blank_skin.png")]

sure=False
sure=True
while sure==False:
    for i in range(len(lst_presset)):
        print(str(i)+":",lst_presset[i][0])
    choix=int(input("quel preset choisissez vous?"))
#    Image.open("preset/"+str(lst_presset[choix][1])).show()
    ok=input("etes vous sur? (o/n)")
    if ok.lower() =="o":
        sure=True
        
for z in range(len(lst_presset)):
    seuil_de_noir=69
    skin_original = Image.open("skin/skin_original.png")
    skin_original = skin_original.convert("RGBA")
    data = skin_original.getdata()
    
    skin_blank=Image.open("skin/skin_original.png")
    skin_blank = skin_blank.convert("RGBA")
    datablank = skin_blank.getdata()
    
    choix=z
#modification du skin
    new_skin_data = []
    if choix==6:
        for item in data:
                if item <= (seuil_de_noir,seuil_de_noir,seuil_de_noir) and item != (0,0,0):
                    new_skin_data.append((255-item[0],255-item[1],255-item[2]))
                else:
                    new_skin_data.append(item)
    else:
        skin_preset = Image.open("preset/"+str(lst_presset[choix][1]))
        skin_preset = skin_preset.convert("RGB")
        presetdata = skin_preset.getdata()
        for item in range(len(data)):
            if presetdata[item]!=(0,0,0):
                new_skin_data.append((presetdata[item][0],presetdata[item][1],presetdata[item][2],255))
            else:
                new_skin_data.append(data[item])
    skin_original.putdata(new_skin_data)
#    skin_original.show()
    skin_original.save("skin/skin_modifié_"+str(lst_presset[choix][0])+".png")