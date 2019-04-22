from random import randint

def process(hold, value):
    try:
        guessed = int(value)
        if guessed > hold:
            print("Aşağı")
        elif guessed < hold:
            print("yukarı")
        else:
            print("!!! T E B R İ K L E R !!!")
            return True
    except:
        print("Lütfen bir sayı giriniz...")
    return False


def play():
    hold = randint(1, 100)
    print(hold)
    print("1 ile 100 arasında bir sayıt tuttum. Tahmin edebilir misin?")
    for _ in range(10):
        value = input("Tahminizi girin:")
        if value in ['q', 'Q']:
            exit(0)
        if process(hold, value):
            return
    print(f"10 defa da bilemediniz. Tuttuğum sayı {hold} idi")


def guess():
    while(True):
        play()
        answer = input("Bir daha oynamak ister misin? [y/n]")
        if answer not in ['y','Y']:
            break


if __name__ == '__main__':
    guess()
