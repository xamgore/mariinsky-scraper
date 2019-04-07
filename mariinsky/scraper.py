from typing import Dict, Iterable, List, Tuple

from bs4 import BeautifulSoup, Tag

from mariinsky.http import get, is_url, normalize
from mariinsky.spectacle import Spectacle
from mariinsky.ticket import Ticket


def children_to_dict(node: Tag) -> Dict[str, str]:
    return {tag.name: tag.get_text() for tag in node.children if tag.name is not None}


def extract_spectacle_info(xml: str, about_url: str) -> Spectacle:
    soup = BeautifulSoup(xml, 'xml')
    tickets = [Ticket(**children_to_dict(tag)) for tag in (soup.select('ticket'))]
    info = children_to_dict(soup.select_one('spectacle_info'))
    return Spectacle(tickets=tickets, about_url=about_url, **info)


def parse_schedule(html: str) -> Iterable[Tuple[str, str]]:
    soup = BeautifulSoup(html, 'html.parser')
    items: List[Tag] = soup.select('[itemtype]')

    for item in items:
        ticket_anchor = item.select_one('.t_button a')
        ticket_url = '' if ticket_anchor is None else normalize(ticket_anchor.get('href', ''))

        about_anchor = item.select_one('[itemprop=url]')
        about_url = '' if about_anchor is None else about_anchor.get('href', '')

        if is_url(ticket_url) and is_url(about_url):
            yield ticket_url, about_url


def get_events(schedule_url: str, months_ahead=6):
    from datetime import datetime
    from dateutil.relativedelta import relativedelta
    now = datetime.now()

    for i in range(months_ahead):
        future = now + relativedelta(months=i)
        html = get(schedule_url.format(year=future.year, month=future.month))

        for ticket_url, about_url in parse_schedule(html):
            xml = get(ticket_url)
            yield extract_spectacle_info(xml, normalize(about_url, 'https://mariinsky.ru/'))
