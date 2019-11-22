import os
import matplotlib.pyplot as plt
import cv2
from matplotlib.widgets import RectangleSelector
from generate_xml import write_xml
import matplotlib
from pathlib import Path
# matplotlib.use('TKAgg')
#global constants
img = None
tl_list = []
br_list = []
object_list = []
path = input('Please input your image folder name!\n')
#constants
image_folder = 'images/Part1' + '/' + path
target_folder_gray = 'images/Part1_Gray'
savedir = 'annotations'
obj = 'Player'

def line_select_callback(clk, rls):
    global tl_list
    global br_list
    
    tl_list.append((int(clk.xdata), int(clk.ydata)))
    br_list.append((int(rls.xdata), int(rls.ydata)))
    object_list.append(obj)
    print(f'Recorded: \n{object_list}\n')
    print(f'Top Left: \n{tl_list}\n')
    print(f'Bottom Right: \n{br_list}\n')

def change_object(event):
    global obj
    if event.key == 'w':
        print('[Changed to Player]\n')
        obj = 'Player'

    if event.key == 'e':
        print('[Changed to football]\n')
        obj = 'Football'

    if event.key == 'r':
        print('[Changed to Goalpost]\n')
        obj = 'Goalpost'
    
    if event.key == 'd':
        print('[Changed to Referee]\n')
        obj = 'Referee'
    
    if event.key == 'f':
        print('[Changed to Holding the ball]\n')
        obj = 'Holding the ball'

    if event.key == 'z':
        del tl_list[-1]
        del br_list[-1]
        del object_list[-1]
        print('[Deleted Previous Object]\n')
        print(f'Recorded: \n{object_list}\n')
        print(f'Top Left: \n{tl_list}\n')
        print(f'Bottom Right: \n{br_list}\n')

    # if event.key == 'c':
    #     print('Changed to CF')
    #     obj = 'CF'

    # if event.key == 'v':
    #     print('Changed to CMF')
    #     obj = 'CMF'
    
    # if event.key == 'b':
    #     print('Changed to SB')
    #     obj = 'SB'

    # if event.key == 'n':
    #     print('Changed to GK')
    #     obj = 'GK'

def onkeypress(event):
    global object_list
    global tl_list
    global br_list
    global img
    if event.key == 'q':
        write_xml(target_folder_gray, img, object_list, tl_list, br_list, savedir)
        print(f'[Final] \n{tl_list}\n{br_list}\n{object_list}\n')
        tl_list = []
        br_list = []
        img = None
        object_list = []
        plt.close()

    if event.key == 'a':
        os.remove(img)
        print('[Deleted the image]\n')
        plt.close()



def toggle_selector(event):
    toggle_selector.RS.set_active(True)

if __name__ == '__main__':
    # for n, image_file in enumerate(os.scandir(image_folder)):
    for image_file in sorted(Path(image_folder).glob('*.png')):
        img = image_file
        fig, ax = plt.subplots(1)
        # mngr = plt.get_current_fig_manager()
        # mngr.wind.setGeometry(250, 120, 1280, 1024)
        image = cv2.imread(str(img))
        print(image_file)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        ax.imshow(image)

        toggle_selector.RS = RectangleSelector(
            ax, line_select_callback,
            drawtype = 'box', useblit = True,
            button = [1], minspanx = 3, minspany = 3,
            spancoords = 'pixels', interactive = True
        )
        bbox = plt.connect('key_press_event', toggle_selector)
        obj_changed = plt.connect('key_press_event', change_object)
        key = plt.connect('key_press_event', onkeypress)
        plt.tight_layout()
        plt.show()
