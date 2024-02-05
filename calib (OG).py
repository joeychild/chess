from pynput.mouse import Listener
import pyautogui
from time import sleep

'''
===== CALIBRATION PRE-REQUISITES =====
- Display this FEN on chess.com/analysis: 2p1p3/1ppbbnn1/1rrqqkk1/1PPBBNN1/1RRQQKK1/8/8/8 w - - 0 1
- Take a CENTERED screenshot of the pawn on c8 and save as "calib_bp.png"
- Replace square value in Chess.py with the one generated in this program
'''
# #PXD - Display coordinates when clicking
# def on_click(x, y, button, pressed):
#     if button == button.left and pressed:
#         print('Mouse clicked at ({0}, {1})'.format(x, y))

# #Activate when actually looking for coordinates

# with Listener(on_click=on_click) as listener:
#     listener.join()

def rnd(x, base=5):
    return base * round(x/base)

location = list(pyautogui.locateAllOnScreen("calib_bp.png"))
x1, y1 = (rnd(i) for i in location[0][:2])
x2, y2 = (rnd(i) for i in location[1][:2])
# print(x1, y1,x2,y2)
square = (x2-x1)//2
lx, ly = x1-2*square, y1
pyautogui.click(lx, ly)
# print(lx, ly)
# sleep(1)
# print(square, lx, ly)

color = "bw"
type2 = "rqkpbn"
bgname = ["w", "b", "ws", "bs"]
# pyautogui.click(535, 210)
# pyautogui.click(535+square+17, 210+square+17)
# sleep(1)
# pyautogui.click(535+square+square-17, 210+square+130)
for i in range(4):
    for j in range(6):
        pyautogui.click(lx + int(1.1 * square) + j * square, ly + int(1.1 * square) + i * square)
        img = pyautogui.screenshot(region = (lx + int(1.1 * square) + j * square, ly + int(1.1 * square) + i * square, int(0.8 * square), int(0.8 * square)))
        pyautogui.click(lx + int(1.1 * square) + j * square, ly + int(1.1 * square) + i * square)
        if i % 2 != 0 and j == 1:
            img2 = pyautogui.screenshot(region = (lx + int(1.1 * square) + j * square, ly + int(1.1 * square) + i * square, int(0.8 * square), int(0.8 * square)))
            img2.save("new_images/"+ color[i//2] + type2[(((1+i)*6+(1+j) - 1) //2) % 6] + ".png")
        # img.show()
        # print(i + j //2)
        img.save("new_images/"+ color[i//2] + type2[(((1+i)*6+(1+j) - 1) //2) % 6] + "_" + bgname[(i + j) % 2 + 2] + ".png")
print("Square size:", square)