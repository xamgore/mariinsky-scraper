import re


class Ticket:
    def __init__(self, tid: str, tregion: str, tside: str, tplace: str, tprice1: str, tprice2: str,
                 tprice3: str, x: str, y: str, pid: str, it, xcoord, ycoord, trow: str = '', tsection: str = ''):
        def parse_int(str: str) -> int:
            groups = re.findall(r'\d+', str)
            return int(groups[0]) if groups else 1


        # ticket id
        self.id = int(tid)

        # performance id
        self.pid = int(pid)

        # 1-й ярус | Амфитеатр | Балкон | Бельэтаж | Бенуар | Ложа "Д" | Партер
        self.region: str = tregion.strip()

        # Номер ложи в зале Мариинский-1
        self.section: str = tsection.strip()

        # Левая сторона | Середина | Правая сторона
        self.side: str = tside.strip()

        # Ряд 6
        self.row: str = trow.replace('Ряд', '').strip()
        self.row_num: int = parse_int(trow)

        # Место 34
        self.place: str = tplace.strip()
        self.place_num: int = parse_int(tplace)

        # Полный тариф
        self.full_price: int = int(tprice2) if tprice2.isdigit() else int(tprice1)

        # Специальный тариф
        self.price: int = int(tprice1) if tprice1.isdigit() else int(tprice2)

        # ???
        # self.price_unknown = tprice3

        self.left: int = int(x)
        self.top: int = int(y)


    def __repr__(self):
        return f'<{self.__class__.__name__}{str(self.__dict__)}>'
