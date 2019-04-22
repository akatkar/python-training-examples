

def main():
    try:
        a,b =5,0
        c = a // b
        print(f'{a} / {b} = {c}')
    except ZeroDivisionError as e:
        print("hata oldu: ",e)
    finally:
        print("bu kod her zaman çalışacak")


if __name__ == '__main__':
    main()