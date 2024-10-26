import time
import pyautogui
from PIL import Image
import pytesseract
from sympy import print_glsl

access_attempts=2
def get_position(word):
    up_left = None
    while up_left == None:
        up_left = pyautogui.locateCenterOnScreen('C:/Users/11692/PycharmProjects/AUTO/PRECOUCE/{}.png'.format(word),confidence=0.9)
    return up_left
pyautogui.moveTo(get_position('MHY'))
pyautogui.doubleClick()
time.sleep(2)
p=0
while True:
        try:
            if get_position('srmunu') is not None:
                pyautogui.moveTo(get_position('srmunu'))
                print('找到')
                pyautogui.doubleClick()
                time.sleep(1.5)
                break
        except pyautogui.ImageNotFoundException:
            print('无法找到')
            time.sleep(1)

pyautogui.moveTo(get_position('start'))
pyautogui.doubleClick()
time.sleep(10)
num=0
while num<10:
        try:
            if pyautogui.locateCenterOnScreen('C:/Users/11692/PycharmProjects/AUTO/PRECOUCE/{}.png'.format('using'),confidence=0.9) is not None:
                    pyautogui.moveTo(get_position('using'))
                    pyautogui.click()
                    time.sleep(0.5)
                    pyautogui.moveTo(get_position('password'))
                    pyautogui. click()
                    pyautogui.write('************')
                    time.sleep(0.5)
                    pyautogui.moveTo(get_position('phone'))
                    time.sleep(0.5)
                    pyautogui.doubleClick()
                    pyautogui.write('************')
                    time.sleep(0.2)
                    pyautogui.moveTo(get_position('00'))
                    pyautogui.click()
                    time.sleep(0.5)
                    pyautogui.moveTo(get_position('SRstart'))
                    pyautogui.click()
                    break
            else:
                    print("Image not found on the screen.")


        except pyautogui.ImageNotFoundException:
            time.sleep(2)
            num=num+2
            print("Imag not found ovn the screen. (Caught ImageNotFoundException)")




while True:
    try:
        if get_position('djjr') is not None:
            print('已经找到图片')
            pyautogui.click()

            break
    except pyautogui.ImageNotFoundException:

        print('未找到点击开始')

        time.sleep(0.1)

t=0
while t<5:
    try:
        if get_position('meiyue') is not None:
            pyautogui.moveTo(get_position('meiyue'))
            print('已经找到月卡')
            pyautogui.click()
            pyautogui.moveRel(200, 0, duration=1)
            time.sleep(1)
            pyautogui.click()
            time.sleep(1)
            pyautogui.click()

            break
    except pyautogui.ImageNotFoundException:

        print('未找到月卡')
        t=t+1
        time.sleep(1)


while True:
    try:
        if get_position('rwl') is not None:
            print('已经找到任务栏')


            break
    except pyautogui.ImageNotFoundException:
        pyautogui.press('F4')
        print('未找到任务栏')
        time.sleep(2)




time.sleep(3)
num=0
while True:
   try:
       if get_position('moni') is not None:
        pyautogui.moveTo(get_position('moni'))
        pyautogui.doubleClick()
        time.sleep(2)
        break


   except pyautogui.ImageNotFoundException:

        print('未找到模拟宇宙按键1')

        break



screenshot = pyautogui.screenshot(region=(1472,39, 100,50))  # x, y, width, height

# 将截图保存为临时文件
screenshot_path = 'C:\\Users\\11692\\PycharmProjects\\AUTO\\PRECOUCE\\screenshot.png'
screenshot.save(screenshot_path)
image = Image.open(screenshot_path)
#Construct the full path to the image

# 使用pytesseract识别图像中的数字
text = pytesseract.image_to_string(image, config='--oem 3 --psm 6')
# 注意：'--oem 3' 表示使用LSTM OCR引擎，'--psm 6' 表示假设图像是一个单一的统一块文本。

# 由于text可能包含非数字字符，你可能需要进一步处理它
# 例如，使用正则表达式提取所有数字
import re
numbers = re.findall(r'\b\d+\b', text)

# 打印提取的数字
print(numbers)

int_num=int(numbers[0])
print(int_num)
target_finds = int_num/40
target_finds_int = int(target_finds)
print("{:d}".format(target_finds_int))
The_target_finds=target_finds_int-1
print( The_target_finds)

if  The_target_finds>=0:
    time.sleep(1)

    pyautogui.moveTo(1535, 522)#传送流萤副本
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.moveTo(1033, 822)#支援
    pyautogui.click()
    time.sleep(2.5)
    pyautogui.moveTo(353, 637)#好友人物
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(1535, 978)#开始挑战

    pyautogui.doubleClick()
    time.sleep(5)
    pyautogui.press('e')
    time.sleep(1.5)
    pyautogui.press('2')
    time.sleep(1.2)
    pyautogui.press('e')
    time.sleep(1.2)
    pyautogui.press('4')
    time.sleep(1.3)
    pyautogui.press('e')
    time.sleep(1.2)
    pyautogui.keyDown('w')
    time.sleep(2)
    pyautogui.keyUp('w')
    time.sleep(0.5)
    pyautogui.press('e')
    time.sleep(3)

    time.sleep(2)
    pyautogui.press('v')
    time.sleep(2)
    max_attempts = 1000
    attempts = 0
    center_finds = 0

    # 寻找指定数量的"again"图片
    while center_finds < The_target_finds:
        try:
            center = pyautogui.locateCenterOnScreen('C:/Users/11692/PycharmProjects/AUTO/PRECOUCE/again.png', confidence=0.9)
            if center:
                pyautogui.click(center)
                time.sleep(2)
                print('图片 "again" 已找到并点击')
                center_finds += 1  # 增加找到center的次数
        except pyautogui.ImageNotFoundException:
            # 如果没有找到图片，增加尝试次数并等待
            time.sleep(1)
            print('未找到图片again，正在重试...')
            attempts += 1

    time.sleep(4)

    attempts = 0  # 重置尝试次数，因为我们现在开始寻找新的图片
    while attempts < max_attempts:
        try:
            left = pyautogui.locateCenterOnScreen('C:/Users/11692/PycharmProjects/AUTO/PRECOUCE/tuichu.png', confidence=0.9)
            if left:
                pyautogui.click(left)

                print('图片 "tuichu" 已找到并点击，达到目标次数，退出循环')
                break  # 退出内层循环
        except pyautogui.ImageNotFoundException:
            # 如果没有找到图片，增加尝试次数并等待
            print('未找到图片tuichu，正在重试...')
            time.sleep(1)
            attempts += 1

    # 如果在内层循环中找到了"tuichu"图片，则跳出外层循环（如果需要的话）
      # 这里假设找到"tuichu"图片后就不需要继续执行了

    # 如果因为达到最大尝试次数而退出循环，则打印一条消息
    if attempts == max_attempts and center_finds < target_finds:
        print(f'达到最大尝试次数 {max_attempts}，但未能在找到足够多的 "again" 图片。')

time.sleep(5)
time.sleep(5)
time.sleep(3)
#----------------------------------------------------------好友赠礼--------------------------------------------------------------------#

pyautogui.press('esc')
time.sleep(4)
num1=0
while num1 <4:
    try:
        if get_position('gift') is not None:
            pyautogui.moveTo(get_position('gift'))
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(get_position('manyou'))
            pyautogui.click()
            break
    except pyautogui.ImageNotFoundException:
        print('未找到（。。。）')
        pyautogui.press('esc')
        time.sleep(2.5)
        num1=num1+1
# pyautogui.moveTo(1727, 112)#(...)

time.sleep(2)
pyautogui.moveTo(1680, 279)#（gift）
time.sleep(2)
pyautogui.click()

#-------------------------------------------------------------委托------------------------------------------------------------------------------------#

while 1:
    try:
        if get_position('weituo') is not None:
            pyautogui.moveTo(get_position('weituo'))
            pyautogui.click()
            time.sleep(1)
            break
    except pyautogui.ImageNotFoundException:
        pyautogui.press('esc')
        print('未找到委托。。。')
        time.sleep(2)


time.sleep(1)
pyautogui.moveTo(431, 907)#一键领取1
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(1121, 963)#再次委托
pyautogui.click()
time.sleep(2)
pyautogui.click()

#----------------------------------------------------无名勋章----------------------------------------------------------#

y=0
while y<2:
    try:
        if get_position('wuming') is not None:
            pyautogui.moveTo(get_position('wuming'))
            pyautogui.click()

            break
    except pyautogui.ImageNotFoundException:
        pyautogui.press('esc')
        print("未找到无名。。。。")
        time.sleep(2)
        y=y+1
print(y)
time.sleep(2)
if y<2:
    try:
        if get_position('rwding') is not None:
            pyautogui.moveTo(get_position('rwding'))
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(1673, 924)  # 领取
            pyautogui.click()
            time.sleep(2)
    except pyautogui.ImageNotFoundException:
            pyautogui.moveTo(1673, 924)  # 领取
            pyautogui.click()
            time.sleep(2)

    time.sleep(3)

    try:
        if get_position('rwzhong') is not None:
            pyautogui.moveTo(get_position('rwzhong'))
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(1438, 910)  # 领取
            pyautogui.click()
            time.sleep(2)
    except pyautogui.ImageNotFoundException:
            pyautogui.moveTo(1438, 910)  # 领取
            pyautogui.click()
            time.sleep(2)




# ---------------------------------------------------------------指南--------------------------------------------------------------------
time.sleep(5)
z=0
while z<3:
    try:
        if get_position('zhinan') is not None:
            pyautogui.moveTo(get_position('zhinan'))
            pyautogui.click()
            break
    except pyautogui.ImageNotFoundException:
        pyautogui.press('esc')
        print("未找到指南。。。。")
        time.sleep(2)
        z=z+1

time.sleep(3)
try:
    if get_position('meiri') is not None:
        pyautogui.moveTo(get_position('meiri'))
        pyautogui.click()
        pyautogui.click()
        i=0
        while i<5 :
               try:
                    pyautogui.moveTo(get_position('lingqu'))#点击领奖
                    pyautogui.click()
                    time.sleep(1.5)
               except pyautogui.ImageNotFoundException:
                    print('未发现领取按钮1')
                    time.sleep(1)
                    i=i+2
        pyautogui.moveTo(638, 303)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
except pyautogui.ImageNotFoundException:#未发现每日图像
    z = 0
    while z < 5:
        try:
            pyautogui.moveTo(get_position('lingqu'))  # 点击领奖
            pyautogui.click()
            time.sleep(1.5)
        except pyautogui.ImageNotFoundException:
            print('未发现领取按钮2')
            time.sleep(1)
            z = z + 2
    pyautogui.moveTo(638, 303)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)

pyautogui.press('win')
time.sleep(1.5)

#--------------------------------------------------------------------关闭程序----------------------------------------------------------------------#
pyautogui.moveTo(get_position('SRtubiao'))
time.sleep(0.8)
pyautogui.click(button='right')
time.sleep(0.8)
pyautogui.moveTo(get_position('shut'))
time.sleep(0.8)
pyautogui.click()