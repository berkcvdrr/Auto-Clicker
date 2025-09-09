import pyautogui
import keyboard
import time

def auto_click(x, y, duration, interval):
    end_time= time.time() + duration
    print(f"tıklama başlatılıyor {duration} saniye tıklanacak...")

    while time.time() < end_time:
        pyautogui.click(x,y)#belirtilen konuma tıklama yap
        time.sleep(interval)#bir süre bekle
        if keyboard.is_pressed('q'):
            print("tıklama durduruldu")
            break
if __name__=="__main__":
    print("autoclicker başlatılıyor...")
    print("tıklamak istediğiniz konumu ayarlamak için 5 saniye bekleyin")
    time.sleep(5)

    x , y = pyautogui.position() #fare konumu
    print(f"tıklama konumu {x}, {y}")

    duration=float(input("tıklanacak süreyi girin: "))
    interval=float(input("tıklama aralığını saniye cinsinden girin: "))

    auto_click(x, y, duration, interval)