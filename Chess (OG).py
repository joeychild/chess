# import requests
import os
import pyautogui
from PIL import Image
from time import sleep
from pynput.mouse import Listener
import chess
import chess.engine
# import screeninfo
# import calib
from random import randint
import traceback

'''
===== PREREQUISITES FOR USE =====
- Must be using Chess.com
- Must be using default skins (if not, please re-run new-images commands) !!FIXED!!
- Must not have webpage covered in any way 
- Make sure not to have similar colors displayed over your timer
- Do not zoom in or fullscreen
- The original resolution for the programmer is 2560x1440 !!FIXED!!
- May have different coordinates if resolution, display, or window size is different !!FIXED!!
- Coordinates must be turned off
- Animations must be turned off (for now)
- Auto-promote to queen is on (for now)
- Assume that the other side cannot promote (for now) !!FIXED(not tested though)!!
'''

'''
===== REMAINING TO-DOS =====
- Write math for piece location !!DONE!!
- Check everything works with UCI !!DONE!!
- Add in Stockfish element !!DONE!!
- Add in random processing and time from previous code !!DONE!!
- Add program abort !!DONE!!
- Make Stockfish make first move if white !!DONE!!

===== OPTIONAL ELEMENTS =====
- Plot out analysis
- Print out all moves and blunders
- Promotions (These are going to be really time-consuming to code in so we're currently going with the prerequisite of automatic queen promotion by both sides)
- Have a method of recovering a board if lost (try-except?) !!DONE!!
- Calibration sequence !!DONE!!
'''

########################## CHESS-IMAGES FOLDER ##########################

#Variables
# color = "wb"
# type = "rnbkqp"
# bglist = [(238,238,210, 255), (118,150,86), (247,247,105),(187,203,43)]
# bgname = ["w", "b", "ws", "bs"]

##=====================Retreiving Images Online========================##
# def images(piece):
#     url = "https://www.chess.com/chess-themes/pieces/neo/150/"+ piece +".png"
#     response = requests.get(url)

#     with open("chess_images/" + piece + '.png', 'wb') as f:
#         f.write(response.content)

# for i in color:
#     for j in type:
#         images(i+j)

##=========Combining Images w/ Respective Background Colors============##

# dir_path = os.getcwd()

# Loop through all the files in the directory
# for file_name in os.listdir(dir_path):
#     # Check if the file is a JPG image
#     if file_name.endswith('.jpg'):
#         # Read the file
#         with open(os.path.join(dir_path, file_name), 'rb') as f:
#             # Do something with the file
#             print(f'Reading file: {file_name}')
#             i = f.read()
#             print(type(i))
#             Image.open(i)
#             # print(i)
#             # print("this is getting run")

# def bg(piece, bgc, bgn):
#     img = Image.open("chess_images/"+ piece + ".png").convert("RGBA")
#     new_img = Image.new('RGBA', img.size, bgc)
#     new_img.paste(img, (0, 0), img)
#     new_img.save("chess_images/new_"+ piece + "_" + bgn + ".png")

# for i in color:
#     for j in type:
#         # images(i+j)
#         for k in range(4):
#         #     print(bglist[k])
#         #     bg(i+j, bglist[k],bgname[k])
#         # os.remove("chess_images/"+ i+j + ".png")

#             location = list(pyautogui.locateAllOnScreen("chess_images/new_" + i+j+ "_" + bgname[k] + ".png"))
#             print("chess_images/new_" + i+j+ "_" + bgname[k] + ".png")
#             if location != []:
#                 for piece in location:
#                     x, y, w, h = piece
#                     pyautogui.click(x+w/2, y+h/2)
#                     print(x,y,w,h)
#             else:
#                 print("fail")

########################### NEW-IMAGES FOLDER ###########################

# location = list(pyautogui.locateAllOnScreen("chess_images/test_bp.png"))
# if location != []:
#     for piece in location:
#         x, y, w, h = piece
#         pyautogui.click(x+w/2, y+h/2)
#         print(x,y,w,h)
# else:
#     print("fail")
# location = list(pyautogui.locateAllOnScreen("chess_images/test_bp2.png"))
# if location != []:
#     for piece in location:
#         x, y, w, h = piece
#         pyautogui.click(x+w/2, y+h/2)
#         print(x,y,w,h)
# else:
#     print("fail")

# color = "bw"
# type2 = "rqkpbn"
# pyautogui.click(535, 210)
# pyautogui.click(535+135+17, 210+135+17)
# sleep(1)
# pyautogui.click(535+135+135-17, 210+135+130)
# print((((1+2)*(1+5)) //2) % 6)
# for i in range(4):
#     for j in range(6):
#         pyautogui.click(687+j*135, 362 + i*135)
#         img = pyautogui.screenshot(region = (687+j*135,362+i*135, 101, 101))
#         pyautogui.click(687+j*135, 362 + i*135)
#         # img.show()
#         print(i + j //2)
#         img.save("new_images/"+ color[i//2] + type2[(((1+i)*6+(1+j) - 1) //2) % 6] + "_" + bgname[(i + j) % 2 + 2] + ".png")

########################### TIMER AND COLOR ###########################

#Variables
color = "w"
files = "hgfedcba"
ucolor = "b"
start = ""
end = ""
words = ["B", "Second b", "Third b", "Fourth b", "Fifth b"]

#Dimensions (ADD CALIBRATION IN FUTURE)
square = 140
while True:
    onw = pyautogui.locateOnScreen("new_images/wr.png", region = (0, 0, pyautogui.size()[0], pyautogui.size()[1] // 2))
    onb = pyautogui.locateOnScreen("new_images/br.png", region = (0, 0, pyautogui.size()[0], pyautogui.size()[1] // 2))
    if onw != None or onb != None:
        break
# print(pyautogui.size()[0], pyautogui.size()[1])
# print(onw, onb)
if onb != None:
    ucolor = "w"
    color = "b"
print(f"You are playing as {'white' if ucolor == 'w' else 'black'}.")
on = onb if onb is not None else onw
# print(onb)
lx = 5 * round((on[0]-4)/5)
ly = 5 * round((on[1]-4)/5)
tx = int(square * 7 + lx)
ty = int(square * 8.2 + ly)
active = (38, 36, 33) if ucolor == "b" else (255, 255, 255) #Active timer color

# print(lx, ly, tx, ty)

#Compatiability with different colored boards



"""
Key information:

-----Board size-----

left corner is 430, 210
left corner on analysis board is 535, 210
square size is 135 px

1920 x 1080
left corner is 295, 170
square size is 100 px

-----timer color-----

surveying region: 1380, 1320 and 1400, 1340

red turn [low time] (178,51,48)
black turn (38,36,33)
white turn (255, 255, 255)
"""

##### NOT NEEEDED ANYMORE. ROOK FINDING CAN ACT AS COLOR DETECTION AS WELL #####
#Waits until timer is visible to find color
# while True:
#     for i in range(4):
#         if pyautogui.pixelMatchesColor(tx, ty, tcolors[i]):
#             print("You are playing as " + color[i // 2])
#             ucolor = color[i//2] #ucolor is now the color of the player's pieces
#             color = color.replace(ucolor, "") #color is now the opponent's piece color
#             #print(color)
#             active = tcolors[(i//2)*2]
#             passive = tcolors[(i//2)*2 + 1]
#             break
#     if ucolor != "":
#         break
#     sleep(0.1)
#print(ucolor, active, passive)

########################### PLAYING THE GAME ###########################

board = chess.Board()

engine = chess.engine.SimpleEngine.popen_uci(r"stockfish_15.1_win_x64_avx2\stockfish-windows-2022-x86-64-avx2.exe")

#Add FEN in case board is already in different position
fen = input("Add FEN? ")
try:
    board.set_fen(fen)
except:
    print("Continuing on a blank board.")

#Makes first move if applicable
#print(board.fullmove_number)
if ucolor == "w" and board.fullmove_number == 1:
    files = "abcdefgh"
    # pyautogui.click(430+60+4*135, 210 + 60 + 6*135)
    # pyautogui.click(430+60+4*135, 210 + 60 + 4*135)
    # board.push_uci("e2e4")
    #print(board)
    rand = randint(1, 3)
    result = engine.analyse(board, chess.engine.Limit(depth=20), multipv = rand)
    move = str(result[rand-1]["pv"][0])
    eval = result[rand-1]["score"].relative.score()
    # moves = result["pv"] ##### Doesn't allow randomizing moves.
    # print(moves)
    # move = str(moves[randint(1, 7)])


    # print(move)
    pyautogui.click(files.index(move[0]) * square + square//2 + lx, (8 - int(move[1])) * square + square//2 + ly)
    pyautogui.click(files.index(move[2]) * square + square//2 + lx, (8 - int(move[3])) * square + square//2 + ly)
    board.push_uci(move)

    # print(board.fullmove_number)
    print("========== MOVE", str(board.fullmove_number), "==========")
    print(f"{words[rand - 1]}est move")
    print("UCI:", move)
    print("Current evaluation:", str(eval/100))
    print()

piece = "fail"
promote = ""
#sleep(randint(0, 10))
try:
    while True:
        if pyautogui.pixelMatchesColor(tx, ty, active) or pyautogui.pixelMatchesColor(tx, ty, (178, 51, 48)):
            sleep(0.5)
            s = pyautogui.screenshot(region = (lx, ly, square*8, square*8))
            try:
                for x in range(square//2, s.width, square):
                    for y in range(5*square//7, s.height, square):
                        if s.getpixel((x, y)) == Image.open("new_images/bp_bs.png").getpixel((0,0)) or s.getpixel((x, y)) == Image.open("new_images/bp_ws.png").getpixel((0,0)): #bs and ws
                            #pyautogui.click(x+430, y+210)
                            #print(s.getpixel((x,y)))
                            #print(x+430,y+210)
                            #print()
                            if ucolor == "w":
                                start = files[x//square].upper() + str(9 - round(y/square))
                            else:
                                start = files[x//square].upper() + str(round(y/square))
                            # print(start)
                            #print("board.piece_at(chess." + start + ").symbol()")
                            exec("piece = board.piece_at(chess." + start + ").symbol()")
                            #print(piece)
                            raise StopIteration
                        
            except StopIteration:
                pass

            ######## FAULTY PROGRAMMING (decided to keep this because theres so much more thats gone so heres a taste of what ive been dealing with i guess) ########
            # location = pyautogui.locateOnScreen("bs.png", region = (430, 210, 135*8, 135*8), needle=[(187,203,43)], search=True)
            # pyautogui.locateOnScreen()
            # print(location)
            # pyautogui.click(location[0], location[1])
            # if location != None:
            #     print(round((location[0] - 490)/135))
            #     print(8 - round((location[0] - 270)/135))
            #     start = files[round((location[0] - 490)/135)] + str(8 - round((location[1] - 270)/135))
            # else:
            #     location = pyautogui.locateCenterOnScreen("ws.png")
            #     start = files[round((location[0] - 490)/135)] + str(8 - round((location[1] - 270)/135))

            ###### This was removed because it was too inefficient. Instead of scrolling through every image, I will query what piece was originally on the starting position and look for that specific piece.
            ###### By doing so, I can also start removing the issue of not including promotions by checking if the piece changes, and how it changes.

            # for file in os.listdir("new_images"):
            #     location = pyautogui.locateCenterOnScreen("new_images/" + file)
            #     if location != None:
            #         pyautogui.click(location[0], location[1])
            #         print(files[round((location[0] - 490)/135)] + str(8 - round((location[1] - 270)/135)))
            # print(start)
            # break
            # pyautogui.locateCenterOnScreen("new_images/" + file)
            # pyautogui.click(location[0], location[1])
            # print(files[round((location[0] - 490)/135)] + str(8 - round((location[1] - 270)/135)))
            
            # print(color + piece.lower())
            onb = pyautogui.locateCenterOnScreen("new_images/" + color + piece.lower() + "_bs.png")
            onw = pyautogui.locateCenterOnScreen("new_images/" + color + piece.lower() + "_ws.png")

            # print(onb, onw)

            if onb != None or onw != None:
                on = onb if onb is not None else onw
                # pyautogui.click(onb[0], onb[1])
                if ucolor == "w":
                    # print(round((on[0] - square//2 - lx)/square))
                    end = files[round((on[0] - square//2 - lx)/square)] + str(8 - round((on[1] - square//2 - ly)/square))
                else:
                    # print(round((on[0] - square//2 - lx)/square))
                    end = files[round((on[0] - square//2 - lx)/square)] + str(round((on[1] - square//2 - ly)/square) + 1)
                # print(on[0], on[1], "black")
            else:
                if piece.lower() == "p" and int(start[1]) == 7:
                    promotes = "qrbn"
                    for i in promotes:
                        onb = pyautogui.locateCenterOnScreen("new_images/" + color + i.lower() + "_bs.png")
                        onw = pyautogui.locateCenterOnScreen("new_images/" + color + i.lower() + "_ws.png")
                        if onb != None or onw != None:
                            on = onb if onb is not None else onw
                            # pyautogui.click(onb[0], onb[1])
                            if ucolor == "w":
                                end = files[round((on[0] - square//2 - lx)/square)] + str(8 - round((on[1] - square//2 - ly)/square))
                            else:
                                end = files[round((on[0] - square//2 - lx)/square)] + str(round((on[1] - square//2 - ly)/square) + 1)
                            # print(onb[0], onb[1], "black")
                            promote = i
                            break
            # print(end)
            # print(start+end+promote)
            board.push_uci((start+end+promote).lower())
            # print(board)

            ########## Stockfish Shenanigans (and Stats) ##########

            # print(board.fullmove_number)
            rand = randint(1, 4) ##### CHANGE FOR EASIER (OR HARDER) MOVE DIFFICULTY
            result = engine.analyse(board, chess.engine.Limit(depth=20), multipv = rand)
            print("========== MOVE", str(board.fullmove_number), "==========")
            try:
                move = str(result[rand-1]["pv"][0])
                eval = result[rand-1]["score"].relative.score()
                print(f"{words[rand - 1]}est move")
            except:
                move = str(result[0]["pv"][0])
                eval = result[0]["score"].relative.score()
                print("Best move")
            # sleep(randint(0, 10)) ##### DELAY. ADD IN IF NEEDED

            if len(move) > 4:
                move = move[:4] + "q" ##### STOP GAP SOLUTION FOR PROMOTIONS

            board.push_uci(move)
            print("UCI:", move)
            try:
                print("Current evaluation:", str(eval/100))
            except TypeError:
                print("Current evaluation: M1")
            print()
            
            # Moving the piece
            if ucolor == "w":
                pyautogui.click(files.index(move[0]) * square + square//2 + lx, (8 - int(move[1])) * square + square//2 + ly)
                pyautogui.click(files.index(move[2]) * square + square//2 + lx, (8 - int(move[3])) * square + square//2 + ly)
            else:
                pyautogui.click(files.index(move[0]) * square + square//2 + lx, (int(move[1]) - 1) * square + square//2 + ly)
                pyautogui.click(files.index(move[2]) * square + square//2 + lx, (int(move[3]) - 1) * square + square//2 + ly)

        sleep(0.1)
except:
    #Abort if exception actually occurs.
    traceback.print_exc()
    print(board.fen())
    os.abort()
