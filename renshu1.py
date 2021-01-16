import time
import threading

def boil_udon():
    print('1組目ランニングメニュー開始')
    for i in range(1,6):
        print(f'1組目{i}km目開始')
        time.sleep(5)
    print('1組目ランニングメニュー終了')

def make_tuyu():
    print('2組目ランニングメニュー開始')
    for i in range(1,6):
        print(f'2組目{i}km目開始')
        time.sleep(3)
    print('2組目ランニングメニュー終了')
    

if __name__ == '__main__':
    thread1 = threading.Thread(target=boil_udon)
    thread2 = threading.Thread(target=make_tuyu)
    thread1.start()
    time.sleep(3)
    thread2.start()
    