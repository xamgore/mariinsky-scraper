#!/usr/bin/env -S pipenv run python
import os

from mariinsky.scraper import get_events

if __name__ == '__main__':
    os.makedirs('saved', exist_ok=True)
    os.chdir('saved')

    SCHEDULE_URL = 'https://mariinsky.ru/ru/playbill/playbill/?year={year}&month={month}'
    for spectacle in get_events(SCHEDULE_URL):
        print(spectacle)


    # print(get(URL))
