script made by nocted
wallpapers made by Brique_de_lait


please use the latest version its way easier to use


if you run the source code
i used the pillow library so make sure it is installed

if you run the executable
windows may not authorize it at first if "smart application control" is enabled


if you want to compile the source code yourself use this command in the source code directory using the nuitka python compiler

python -m nuitka .\SkinChanger_V1.4.py --enable-plugin=tk-inter --windows-console-mode=disable


i am not a ui designer, i am sorry if the ui makes you cry, i tried my best

the window is 599 by 300

you can add a "wallpaper" by putting any png in the /wallpaper/ folder (recomended 600x300)
if there is multiple it will take a random one
the wallpaper_guide.png is here to help making "wallpapers" , it show where stuff is and transparent where you should put the interesting parts
the informative_wallpaper.png shows and 'describe' what stuff do

you can change the program icon by changing the app_icon.png file

the prset updater file is here so that if you have an older standard preset it can be refreshed to actual standards, here is the command

python -m nuitka .\preset_updater.py  --windows-console-mode=disable


#################
#               #
#   changelog   #
#               #
#################

v1.0
this script aim to modify a minecraft skin in order to add "clothes"

v1.1
added more "clothes" and updated the script

v1.2
updated the script so that "clothes" names are not fix and skin are just put with the script
it can modify multiples skins in the same run
v1.2.1 - changed getdata() to get_flattened_data() to follow up with the PIL labrary updates

v1.3
added alpha variing preset
changed how preset are put on the skin
added preset_updater.py in order to update presets to v1.3 standards
renamed presets
v1.3.1 - added a sort of ui

v1.4
updated the ui to a more user friendly and overhaul better 
added more option like "use as input", wallpapers etc


##################
#                #
#   how to use   #
#                #
##################

you put your skins in the same folder than the .py or .exe
you put your presets in the /preset/ folder
and run it

if you forgot something the app will start showing you the error and buttons that open the repo or the app folder
if you really need help contact me on discord at ' nocted ' my pfp should be the same as on github

to add preset you have to take a skin and moddify it so that
the pixels whos going to be replaced by your skin are "True black" : any color thet is rgb = 0, 0, 0 no matter the alpha value

