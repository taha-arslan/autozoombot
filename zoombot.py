import pyautogui
import subprocess
import time
import os
import datetime
from datetime import datetime

def join(id, password):
    subprocess.call(APPDATA + '\\Zoom\\bin\\Zoom.exe')
    while True:
        time.sleep(6)
        giriş = pyautogui.locateOnScreen('joinbuton.png')
        if giriş != None:
            pyautogui.click(giriş)
            break

    while True:
        giriş = pyautogui.locateOnScreen('enterid.png')
        pyautogui.typewrite(meeting)
        pyautogui.press('enter')
        break
        if giriş != None:
            pyautogui.click(giriş)
            break

    while True:
        giriş = pyautogui.locateOnScreen('passcode.png')
        pyautogui.typewrite(password)
        pyautogui.press('enter')
        break
        if giriş != None:
            pyautogui.click(giriş)
            os.system('color 7')
            break


APPDATA = os.getenv('APPDATA')

print("")
print("  zzzzzzzzzzzzzzzzz   ooooooooooo      ooooooooooo      mmmmmmm    mmmmmmm ")
print("  z:::::::::::::::z oo:::::::::::oo  oo:::::::::::oo  mm:::::::m  m:::::::mm")
print("  z::::::::::::::z o:::::::::::::::oo:::::::::::::::om::::::::::mm::::::::::m")
print("  zzzzzzzz::::::z  o:::::ooooo:::::oo:::::ooooo:::::om::::::::::::::::::::::m")
print("        z::::::z   o::::o     o::::oo::::o     o::::om:::::mmm::::::mmm:::::m")
print("       z::::::z    o::::o     o::::oo::::o     o::::om::::m   m::::m   m::::m")
print("      z::::::z     o::::o     o::::oo::::o     o::::om::::m   m::::m   m::::m")
print("     z::::::z      o::::o     o::::oo::::o     o::::om::::m   m::::m   m::::m")
print("    z::::::zzzzzzzzo:::::ooooo:::::oo:::::ooooo:::::om::::m   m::::m   m::::m")
print("   z::::::::::::::zo:::::::::::::::oo:::::::::::::::om::::m   m::::m   m::::m")
print("  z:::::::::::::::z oo:::::::::::oo  oo:::::::::::oo m::::m   m::::m   m::::m")
print("  zzzzzzzzzzzzzzzzz   ooooooooooo      ooooooooooo   mmmmmm   mmmmmm   mmmmmm")
print("")
print("                                                                                          Coded By Taha Arslan             ")
print("                                                                                |-----------------------------------------|")                                                                       
print("                                                                                | Discord: janiS#0115                     |")
print("                                                                                |                                         |")
print("                                                                                | GitHub : https://github.com/taha-arslan |")
print("                                                                                |-----------------------------------------|")
print("")
print(" 1. English")
print(" 2. Türkçe")
print("")
dil = input(" Choose A Language: ").strip()




if dil == "1":
    time.sleep(0.5)
    while True:
        os.system('cls')    
        print("")
        print("  zzzzzzzzzzzzzzzzz   ooooooooooo      ooooooooooo      mmmmmmm    mmmmmmm ")
        print("  z:::::::::::::::z oo:::::::::::oo  oo:::::::::::oo  mm:::::::m  m:::::::mm")
        print("  z::::::::::::::z o:::::::::::::::oo:::::::::::::::om::::::::::mm::::::::::m")
        print("  zzzzzzzz::::::z  o:::::ooooo:::::oo:::::ooooo:::::om::::::::::::::::::::::m")
        print("        z::::::z   o::::o     o::::oo::::o     o::::om:::::mmm::::::mmm:::::m")
        print("       z::::::z    o::::o     o::::oo::::o     o::::om::::m   m::::m   m::::m")
        print("      z::::::z     o::::o     o::::oo::::o     o::::om::::m   m::::m   m::::m")
        print("     z::::::z      o::::o     o::::oo::::o     o::::om::::m   m::::m   m::::m")
        print("    z::::::zzzzzzzzo:::::ooooo:::::oo:::::ooooo:::::om::::m   m::::m   m::::m")
        print("   z::::::::::::::zo:::::::::::::::oo:::::::::::::::om::::m   m::::m   m::::m")
        print("  z:::::::::::::::z oo:::::::::::oo  oo:::::::::::oo m::::m   m::::m   m::::m")
        print("  zzzzzzzzzzzzzzzzz   ooooooooooo      ooooooooooo   mmmmmm   mmmmmm   mmmmmm")
        print("")
        print("                                                                                          Coded By Taha Arslan             ")
        print("                                                                                |-----------------------------------------|")                                                                       
        print("                                                                                | Discord: janiS#0115                     |")
        print("                                                                                |                                         |")
        print("                                                                                | GitHub : https://github.com/taha-arslan |")
        print("                                                                                |-----------------------------------------|")
        print("")
        meeting = input(" Enter Your Meeting ID: ").strip()
        time.sleep(0.5)
        if len(meeting) == 10:
            os.system('color 3')
            break
        else:
            os.system('color 4')
            print(" You Entered Wrong ID, Try Again")
            time.sleep(2)
            os.system('cls')
            os.system('color 3')
            print("")
            print("  zzzzzzzzzzzzzzzzz   ooooooooooo      ooooooooooo      mmmmmmm    mmmmmmm ")
            print("  z:::::::::::::::z oo:::::::::::oo  oo:::::::::::oo  mm:::::::m  m:::::::mm")
            print("  z::::::::::::::z o:::::::::::::::oo:::::::::::::::om::::::::::mm::::::::::m")
            print("  zzzzzzzz::::::z  o:::::ooooo:::::oo:::::ooooo:::::om::::::::::::::::::::::m")
            print("        z::::::z   o::::o     o::::oo::::o     o::::om:::::mmm::::::mmm:::::m")
            print("       z::::::z    o::::o     o::::oo::::o     o::::om::::m   m::::m   m::::m")
            print("      z::::::z     o::::o     o::::oo::::o     o::::om::::m   m::::m   m::::m")
            print("     z::::::z      o::::o     o::::oo::::o     o::::om::::m   m::::m   m::::m")
            print("    z::::::zzzzzzzzo:::::ooooo:::::oo:::::ooooo:::::om::::m   m::::m   m::::m")
            print("   z::::::::::::::zo:::::::::::::::oo:::::::::::::::om::::m   m::::m   m::::m")
            print("  z:::::::::::::::z oo:::::::::::oo  oo:::::::::::oo m::::m   m::::m   m::::m")  
            print("  zzzzzzzzzzzzzzzzz   ooooooooooo      ooooooooooo   mmmmmm   mmmmmm   mmmmmm")
            print("")
            print("                                                                                          Coded By Taha Arslan             ")
        print("                                                                                |-----------------------------------------|")                                                                       
        print("                                                                                | Discord: janiS#0115                     |")
        print("                                                                                |                                         |")
        print("                                                                                | GitHub : https://github.com/taha-arslan |")
        print("                                                                                |-----------------------------------------|")
        continue
    print("")

    password = input(" Enter Your Meeting Password: ").strip()
    time.sleep(0.5)

    print("")

    a = input(" Enter Time (i.e. 08:35:00): ")

    print("")
    time.sleep(0.5)
    print(" Waiting...")

    while True:
        d = time.strftime("%X")
        time.sleep(1)
        if d == a:
            break
    print("")
    print(" Redirecting To Zoom.")
    time.sleep(0.5)

    join(meeting, password)

elif dil == "2":
    # Türkçe
    time.sleep(0.5)
    while True:
        os.system('cls')    
        print("")
        print("  zzzzzzzzzzzzzzzzz   ooooooooooo      ooooooooooo      mmmmmmm    mmmmmmm ")
        print("  z:::::::::::::::z oo:::::::::::oo  oo:::::::::::oo  mm:::::::m  m:::::::mm")
        print("  z::::::::::::::z o:::::::::::::::oo:::::::::::::::om::::::::::mm::::::::::m")
        print("  zzzzzzzz::::::z  o:::::ooooo:::::oo:::::ooooo:::::om::::::::::::::::::::::m")
        print("        z::::::z   o::::o     o::::oo::::o     o::::om:::::mmm::::::mmm:::::m")
        print("       z::::::z    o::::o     o::::oo::::o     o::::om::::m   m::::m   m::::m")
        print("      z::::::z     o::::o     o::::oo::::o     o::::om::::m   m::::m   m::::m")
        print("     z::::::z      o::::o     o::::oo::::o     o::::om::::m   m::::m   m::::m")
        print("    z::::::zzzzzzzzo:::::ooooo:::::oo:::::ooooo:::::om::::m   m::::m   m::::m")
        print("   z::::::::::::::zo:::::::::::::::oo:::::::::::::::om::::m   m::::m   m::::m")
        print("  z:::::::::::::::z oo:::::::::::oo  oo:::::::::::oo m::::m   m::::m   m::::m")
        print("  zzzzzzzzzzzzzzzzz   ooooooooooo      ooooooooooo   mmmmmm   mmmmmm   mmmmmm")
        print("")
        print("                                                                                          Coded By Taha Arslan             ")
        print("                                                                                |-----------------------------------------|")                                                                       
        print("                                                                                | Discord: janiS#0115                     |")
        print("                                                                                |                                         |")
        print("                                                                                | GitHub : https://github.com/taha-arslan |")
        print("                                                                                |-----------------------------------------|")
        meeting = input(" Toplantı ID'nizi Giriniz: ").strip()
        time.sleep(0.5)
        if len(meeting) == 10 or 11:
            os.system('color 3')
            break
        else:
            os.system('color 4')
            print(" Yanlış Değer Girdiniz, Tekrar Deneyin.")
            time.sleep(2)
            os.system('cls')
            os.system('color 3')
            print("")
            print("  zzzzzzzzzzzzzzzzz   ooooooooooo      ooooooooooo      mmmmmmm    mmmmmmm ")
            print("  z:::::::::::::::z oo:::::::::::oo  oo:::::::::::oo  mm:::::::m  m:::::::mm")
            print("  z::::::::::::::z o:::::::::::::::oo:::::::::::::::om::::::::::mm::::::::::m")
            print("  zzzzzzzz::::::z  o:::::ooooo:::::oo:::::ooooo:::::om::::::::::::::::::::::m")
            print("        z::::::z   o::::o     o::::oo::::o     o::::om:::::mmm::::::mmm:::::m")
            print("       z::::::z    o::::o     o::::oo::::o     o::::om::::m   m::::m   m::::m")
            print("      z::::::z     o::::o     o::::oo::::o     o::::om::::m   m::::m   m::::m")
            print("     z::::::z      o::::o     o::::oo::::o     o::::om::::m   m::::m   m::::m")
            print("    z::::::zzzzzzzzo:::::ooooo:::::oo:::::ooooo:::::om::::m   m::::m   m::::m")
            print("   z::::::::::::::zo:::::::::::::::oo:::::::::::::::om::::m   m::::m   m::::m")
            print("  z:::::::::::::::z oo:::::::::::oo  oo:::::::::::oo m::::m   m::::m   m::::m")
            print("  zzzzzzzzzzzzzzzzz   ooooooooooo      ooooooooooo   mmmmmm   mmmmmm   mmmmmm")
            print("")
            print("                                                                                          Coded By Taha Arslan             ")
            print("                                                                                |-----------------------------------------|")                                                                       
            print("                                                                                | Discord: janiS#0115                     |")
            print("                                                                                |                                         |")
            print("                                                                                | GitHub : https://github.com/taha-arslan |")
            print("                                                                                |-----------------------------------------|")
            continue
    print("")

    password = input(" Toplantı Şifrenizi Giriniz: ").strip()
    time.sleep(0.5)

    print("")

    a = input(" Saat Giriniz (Örnek: 08:35:00): ")

    print("")
    time.sleep(0.5)
    print(" Bekleniyor...")

    while True:
        d = time.strftime("%X")
        time.sleep(1)
        if d == a:
            break

    print("")
    print(" Zoom'a Yönlendiriliyorsunuz.")
    time.sleep(0.5)

else:
    print("")
    print(" Böyle bir dil desteği yok.")
os.system('exit')

join(meeting, password)
