from datetime import datetime
from typing import List

from dateparser import parse

from mariinsky.ticket import Ticket


class Spectacle:
    def __init__(self, tickets: List[Ticket], about_url: str, date: str, time: str, name: str, hall: str, idhall: str,
                 id_scheme_place: str, id: str, type: str, stop_sale_time: str, onsale, tarif, stop_sale_time_flag,
                 has_liter_rows, min_tickets_price, max_tickets_price):
        self.id: int = int(id)
        self.date: datetime = parse(date.strip() + ' ' + time.strip())
        self.name: str = name.strip()
        self.hall: str = hall.lstrip('Санкт-Петербург,').strip()
        self.hall_id: int = int(idhall)
        self.place_schema_id: int = int(id_scheme_place)
        self.place_schema_url: str = f'/img/halls/{self.place_schema_id}/hall_ru.png'

        # Балет | Опера
        self.type: str = type.strip()

        self.stop_sale_date: datetime = parse(stop_sale_time)
        self.has_liter_rows: bool = has_liter_rows == '1'
        self.tickets = tickets
        self.about_url = about_url


    def __repr__(self):
        fields = self.__dict__.copy()
        del fields['tickets']

        return f'<{self.__class__.__name__}{str(fields)}>'
