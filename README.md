#  Сапер
_Это игра не нуждаеется в представлении_
## Описание 
Главная цель игрока (сапера) это поставить флажки на бомбы, для этого пользователь может открывать клетки. На каждой клетки показан номер, который означает кол-во бомб рядом с ним. Также номера может и не быть - пустые клетки. Рядом с ним нет бомб.
## Цели проекта
* Изучить _tkinter_
* Тренировка навыка программирования
* Сборка приложения с _pyinstaller_
* Просто pet - проект
## Возможности
* Реализован интерфейс игры
  - Ставить флажки
  - Убирать флажки
  - Открывть клетку
  - Таймер
  - Кол - во флажков
  - поле ввода для имен
* Кнопка разработчика
* Кнопка - статистика
  - имя пользователя
  - время
  - формат
## Установка
Скачиваем zip файли и заразархивировуем файл или (если есть _git_) пишем
```
git clone https://github.com/tantoni228/saper.git
```
## Запуск
Запускаем main.py файл или можно командой (находясь в нужной дерикторией)
```
python main.py
```
Также можно сразу запустить main.exe (как приложение)
## Сборка приложения
Приложение собрано, но можно собрать самостоятельно при помощи _pyinstaller_
Скачиваем библиотеку
```
pip install pyinstaller
```
Теперь пишем команду 
```
pyinstaller --onefile --noconsole --add-data "<путь, где хранится сама папка>\saper\db\my_database.db;db" --add-data "<путь, где хранится сама папка>\saper\img\*.png;img" <путь, где хранится сама папка>\saper\main.py --icon="<путь, где хранится сама папка>n\saper\unnamed.ico"
```
также можно поишрать с параметрами, также можно поменять иконку приложения
# _Спасибо за внимание!!!_