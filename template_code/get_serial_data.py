#!/usr/bin/python3
import serial  # импорт библиотеки последовательного интерфейса


def get_data_binary_serial(port: str, speed: int, timeout: int):
    """Принимает данные в виде байт и возвращает обычную строку"""
    
    # инициализация имя, скорость, таймфут чтоб не зависла
    ser = serial.Serial(port=port, baudrate=speed, timeout=timeout)
    # очистка буфера ввода вывода чтоб избежать неполных данных
    ser.flush()
        
    while True:
        if ser.in_waiting > 0:
            # для hex данных
            line = ser.readline().decode('utf-8').rstrip()
            return line


if __name__ == '__main__':
    from template_code.config import PORT, SPEED, TIMEOUT
    
    
    while True:
        data_serial_temp = get_data_binary_serial(
            port=PORT, 
            speed=SPEED, 
            timeout=TIMEOUT
        )
        print(data_serial_temp)
