from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import requests

def main():
    N = 25

    r = Rectangle("синего", N, N)
    c = Circle("зеленого", N)
    s = Square("красного", N)
    print(r)
    print(c)
    print(s)

    #проверка внешнего пакета requests
    try:
        resp = requests.get("https://httpbin.org/ip", timeout=4)
        print(f"\nВнешний пакет работает. Ваш IP: {resp.json()['origin']}") #преобразует json в словарь, извлекает значение по ключу
    except Exception as e:
        print(f"\nНе удалось проверить requests: {e}")

if __name__ == "__main__":
    main()