// библиотека для работы с аналоговым термометром (Troyka-модуль)
#include <TroykaThermometer.h>

// создаём объект для работы с аналоговым термометром
// и передаём ему номер пина выходного сигнала
TroykaThermometer thermometer(A0);

void setup()
{
    // открываем последовательный порт
    Serial.begin(9600);
}

void loop()
{
    // считываем данные с аналогового термометра
    thermometer.read();
    // вывод показателей аналогового термометра в градусах Цельсия
    int data = thermometer.getTemperatureC();
    Serial.println(char(data));
    delay(1000);
}
