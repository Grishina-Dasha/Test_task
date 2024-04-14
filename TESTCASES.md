## Задание 2

## ТК№1. Проверка блока счетчика CO2 для неавторизованного пользователя
### Предусловие:
1. Пользователь не авторизован.
### Шаги воспроизведения:
1. Открыть страницу эковклада https://www.avito.ru/avito-care/eco-impact.
2. Проскроллить страницу до блока "Ваш экологический вклад".
3. Обратить внимание на блок счетчика CO2.
### ОР:
В блоке счетчика отображается 3 строки: 1 строка - 0, 2 строка - "кг СО2", 3 строка - "не попало в атмосферу".

## ТК№2. Проверка счетчика сохраненного объема воды для неавторизованного пользователя
### Предусловие:
1. Пользователь не авторизован.
### Шаги воспроизведения:
1. Открыть страницу эковклада.
2. Проскроллить страницу до блока "Ваш экологический вклад".
3. Обратить внимание на блок счетчика сохраненного объема воды.
### ОР: 
В блоке счетчика отображается 3 строки: 1 строка - 0, 2 строка - текст "л воды", 3 строка - "было сохранено".

## ТК№3. Проверка блока счетчика электроэнергии для неавторизованного пользователя
### Предусловие:
1. Пользователь не авторизован.
### Шаги воспроизведения:###
1. Открыть страницу эковклада.
2. Проскроллить страницу до блока "Ваш экологический вклад".
3. Обратить внимание на блок счетчика электроэнергии.
### ОР:
В блоке счетчика отображается 3 строки: 1 строка - 0, 2 строка - текст "кВт/ч энергии", 3 строка - "было сэкономлено".

## ТК№4. Проверка счетчиков для авторизованного пользователя без значений
### Предусловие:
1. Пользователь авторизован в системе Авито.
### Шаги воспроизведения:
1. Открыть страницу эковклада.
2. Проскроллить страницу до блока "Ваш экологический вклад".
3. Обратить внимание на блоки.
### ОР: 
В каждом блоке счетчика отображается нулевое значение и соответствующие ему единицы измерения, в блоке с тегом Эковклад отображается заглушка аватарки пользователя/либо аватрака пользователя.

## ТК№5. Проверка счетчика сохраненного объема воды для авторизованного пользователя со значениями
### Предусловие:
1. Пользователь авторизован в системе Авито.
2. Пользователь совершал сделки на платформе Авито.
### Шаги воспроизведения:
1. Открыть страницу эковклада.
2. Проскроллить страницу до блока "Ваш экологический вклад".
3. Обратить внимание на счетчик сохраненного объема воды.
    - 500 литров
    - 999 литров
    - 1000 литров
### ОР: 
    - отображается три строки 1 строка - 500, 2 - "л воды", 3 - "было сохранено".
    - отображается три строки 1 - 999, 2 - "л воды", 3 - "было сохранено".
    - отображается три строки 1 - 1, 2 - метр кубический (м3) воды, 3 - было сохранено.