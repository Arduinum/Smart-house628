#!/usr/bin/python3
import serial  # импорт библиотеки последовательного интерфейса


# скрипт не будет запускаться при импорте
if __name__ == '__main__':
    # инициализация имя, скорость, таймфут чтоб не зависла
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()  # очистка буфера ввода вывода чтоб избежать неполных данных

    while True:
        if ser.in_waiting > 0:  # проверяем доступность данных
            # читаем данные пока не наткнёмся на символ новой строки
            # декодируем данные в нужную кодировку, удаляем символ новой строки
            # и символ возврата коретки
            line = ser.readline().decode('utf-8').rstrip()
            print(line)


# $ chmod +x serial_data_test_arduino.py
# $ ./serial_data_test_arduino.py
