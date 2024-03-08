from tkinter import *
import random
from tkinter.messagebox import showinfo


def timing(a, n):
    return (a * 999 + n) // 60,  (a * 999 + n) % 60


offsets = (
    (0, 0, 1, 0),  # top
    (1, 0, 1, 1),  # upper right
    (1, 1, 1, 2),  # lower right
    (0, 2, 1, 2),  # bottom
    (0, 1, 0, 2),  # lower left
    (0, 0, 0, 1),  # upper left
    (0, 1, 1, 1),  # middle
)
# Segments used for each digit; 0, 1 = off, on.
digits = (
    (1, 1, 1, 1, 1, 1, 0),  # 0
    (0, 1, 1, 0, 0, 0, 0),  # 1
    (1, 1, 0, 1, 1, 0, 1),  # 2
    (1, 1, 1, 1, 0, 0, 1),  # 3
    (0, 1, 1, 0, 0, 1, 1),  # 4
    (1, 0, 1, 1, 0, 1, 1),  # 5
    (1, 0, 1, 1, 1, 1, 1),  # 6
    (1, 1, 1, 0, 0, 0, 0),  # 7
    (1, 1, 1, 1, 1, 1, 1),  # 8
    (1, 1, 1, 1, 0, 1, 1),  # 9
)

n = 0
a = 0


class Digit:
    def __init__(self, canvas, x=10, y=10, length=20, width=4):
        self.canvas = canvas
        l = length
        self.segs = []
        for x0, y0, x1, y1 in offsets:
            self.segs.append(canvas.create_line(
                x + x0*l, y + y0*l, x + x1*l, y + y1*l,
                width=width, state='hidden'))

    def show(self, num):
        for iid, on in zip(self.segs, digits[num]):
            self.canvas.itemconfigure(iid, state = 'normal' if on else 'hidden')


class Saper:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.map_status = [[0 for _ in range(self.x)] for _ in range(self.y)]
        self.count_bomb = 0
        self.count_flags = 0
        self.cash_map = []
        self.data = []
        self.map = [[0 for _ in range(self.x)] for _ in range(self.y)]

    def create_map(self):
        self.count_bomb = random.randint(10, 18)

        x = [random.randrange(0, self.x - 1) for _ in range(self.count_bomb)]
        y = [random.randrange(0, self.x - 1) for _ in range(self.count_bomb)]
        for i in range(self.count_bomb):
            self.map[y[i]][x[i]] = 1
        self.count_bomb = 0
        for i in self.map:
            for j in i:
                if j == 1:
                    self.count_bomb += 1

        self.count_flags = self.count_bomb
        # просмотр
        # for i in self.map:
            # print(i)

    def create_cash(self):
        for i in range(self.y):
            self.cash_map.append([])
            for j in range(self.x):
                self.cash_map[i].append(self.find_neighbour(j, i))
        for i in self.cash_map:
            print(*i)

    def find(self, btn):
        for i, val in enumerate(self.data):
            for j, val2 in enumerate(val):
                if btn == val2:
                    return j, i
        return -1, -1

    def find_neighbour(self, x, y):
        count = 0
        data = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        if self.map[y][x] == 1:
            return "B"
        for i in data:
            try:
                if self.map[y + i[1]][x + i[0]] == 1 and y + i[1] >= 0 and x + i[0] >= 0:
                    count += 1
            except IndexError:
                a = 0
        return count

    def algoritm(self, x, y):
        count = [(x, y)]
        i = 0
        while i < len(count):
            for j in self.find_free_cells2(count[i][0], count[i][1]):
                if j not in count:
                    count.append(j)
            i += 1
        return count

    def find_free_cells2(self, x, y):
        count = [(x, y)]
        data = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        for i in data:
            try:
                if self.cash_map[y + i[1]][x + i[0]] == 0 and y + i[1] >= 0 and x + i[0] >= 0:
                    count.append((x + i[0], y + i[1]))
            except IndexError:
                a = 0
        return count

    def find_free_cells(self, x, y):
        count = {}
        data = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        for i in data:
            try:
                if self.cash_map[y + i[1]][x + i[0]] == 0:
                    count.add((x, y))

            except IndexError:
                a = 0
        return count

    def click_button(self, btn):
        x, y = self.find(btn)
        if self.map_status[y][x] == 1:
            return
        # print(x, y)
        self.map_status[y][x] = 1
        match self.cash_map[y][x]:
            case 0:
                image = PhotoImage(file="img/cell_2.png")
                for i, value in enumerate(self.algoritm(x, y)):
                    if i != 0:
                        self.data[value[1]][value[0]].configure(image=image)
            case 1:
                image = PhotoImage(file="img/m1.png")
            case 2:
                image = PhotoImage(file="img/m2.png")
            case 3:
                image = PhotoImage(file="img/m3.png")
            case 4:
                image = PhotoImage(file="img/m4.png")
            case 5:
                image = PhotoImage(file="img/m5.png")
            case 6:
                image = PhotoImage(file="img/m6.png")
            case 7:
                image = PhotoImage(file="img/m7.png")
            case 8:
                image = PhotoImage(file="img/m8.png")
            case 'B':
                image = PhotoImage(file="img/bomd_2.png")
            case _:
                image = PhotoImage(file="img/bomd_2.png")
        btn.configure(image=image)
        btn.image = image  # Сохраняем изображение в атрибуте кнопки

    def flag(self, btn):
        x, y = self.find(btn)
        if self.map_status[y][x] == 1:
            return
        if self.map_status[y][x] == 0 and self.count_flags != 0:
            image = PhotoImage(file="img/flag.png")
            self.map_status[y][x] = 2
            self.count_flags -= 1
        elif self.map_status[y][x] == 2:
            image = PhotoImage(file="img/cell.png")
            self.map_status[y][x] = 0
            self.count_flags += 1
        else:
            return

        btn.configure(image=image)
        btn.image = image  # Сохраняем изображение в атрибуте кнопки

    def win(self):
        count = []
        for i, val in enumerate(self.map_status):
            for j, val2 in enumerate(val):
                if val2 == 2:
                    count.append((j, i))
        count2 = []
        for i, val in enumerate(self.map):
            for j, val2 in enumerate(val):
                if val2 == 1:
                    count2.append((j, i))
        if set(count) == set(count2):
            return True
        return False


    def run(self):
        self.window = Tk()
        self.window.title("Сапер скачать бесплатно, без регистрации.")
        self.window.geometry('600x450')
        self.window.resizable(width=False, height=False)
        screen = Canvas(self.window, width=200, height=50)
        screen.create_text(32, 10,
                           text="Time: ", font="Verdana 14")
        screen.grid(row=0, column=10)
        screen2 = Canvas(self.window, width=200, height=50)
        screen2.create_text(34, 10,
                           text="Flags: ", font="Verdana 14")
        screen2.grid(row=1, column=10)

        developer = Button(self.window, text="DEVELOPER", height=2, width=12)
        developer.grid(row=2, column=10)

        statistics = Button(self.window, text="STATISTICS", height=2, width=12)
        statistics.grid(row=3, column=10)

        image = PhotoImage(file="img/cell.png")  # задать размер
        for i in range(self.y):
            self.data.append([])
            for j in range(self.x):
                btn = Button(self.window, image=image, width=50, height=50)
                btn.config(command=lambda b=btn: self.click_button(b))  # передаем кнопку как аргумент
                btn.bind("<ButtonPress-3>", lambda event, b=btn: self.flag(b))
                self.data[i].append(btn)
                btn.grid(column=j, row=i)
        dig = Digit(screen, 60, 10)
        dig1 = Digit(screen, 90, 10)
        dig2 = Digit(screen, 120, 10)

        dig2_1 = Digit(screen2, 60, 10)
        dig2_2 = Digit(screen2, 90, 10)

        def update():
            global n, a
            dig2.show(n % 10)
            dig1.show(n % 100 // 10)  # Control what you want to show here , eg (n+1)%10
            dig.show(n // 100)

            dig2_1.show(self.count_flags // 10)
            dig2_2.show(self.count_flags % 10)

            n += 1
            a += n // 999
            n %= 999
            self.window.after(1000, update)

            if self.count_flags == 0:
                if self.win():
                    showinfo(title="Information", message="Hello, winner!!! Your time: {:02d}:{:02d}".format(*timing(a, n)))
                    self.create_map()
                    self.create_cash()
                    self.run()
                    return
        self.window.after(1000, update)
        self.window.mainloop()


if __name__ == "__main__":
    saper = Saper(8, 8)
    saper.create_map()
    saper.create_cash()
    saper.run()