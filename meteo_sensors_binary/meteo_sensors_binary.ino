// библиотека для работы с аналоговым термометром (Troyka-модуль)
#include <TroykaThermometer.h>
int data[1];

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
    int temp = thermometer.getTemperatureC();
    data[0] = temp;
    Serial.write((byte*) data, sizeof(data));
    Serial.write("\n");
    delay(1000);
}
