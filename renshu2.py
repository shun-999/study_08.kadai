import time
import threading

def first_ranning():
    print('1組目ランニングメニュー開始')
    for i in range(1,6):
        print(f'1組目{i}km目開始')
        time.sleep(5)
    print('1組目ランニングメニュー終了')

def second_ranning():
    print('2組目ランニングメニュー開始')
    for i in range(1,6):
        print(f'2組目{i}km目開始')
        time.sleep(3)
    print('2組目ランニングメニュー終了')

def muscle_training():
    print("筋トレメニュー開始")
    time.sleep(3)
    print("筋トレメニュー終了")

if __name__ == '__main__':
    thread1 = threading.Thread(target=first_ranning)
    thread2 = threading.Thread(target=second_ranning)
    thread3 = threading.Thread(target=muscle_training)
    thread1.start()
    time.sleep(3)
    thread2.start()
    thread1.join()
    thread2.join()
    time.sleep(1)
    thread3.start()
    thread3.join()
    print('トレーニング終了')
    

    