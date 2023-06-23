import logging

from bs4 import BeautifulSoup
from http import HTTPStatus
from requests import RequestException

from constants import EMPTY_RESPONSE
from exceptions import ParserFindTagException


def get_response(session, url):
    try:
        response = session.get(url)
        response.encoding = 'utf-8'
        return response
    except RequestException:
        logging.exception(
            f'Возникла ошибка при загрузке страницы {url}',
            stack_info=True
        )


def find_tag(soup, tag, attrs=None):
    searched_tag = soup.find(tag, attrs=(attrs or {}))
    if searched_tag is None:
        error_msg = f'Не найден тег {tag} {attrs}'
        logging.error(error_msg, stack_info=True)
        raise ParserFindTagException(error_msg)
    return searched_tag


def make_soup(session, url):
    response = get_response(session, url)
    if response is None or response.status_code == HTTPStatus.NOT_FOUND:
        logging.error(EMPTY_RESPONSE.format(url=url))
        raise ParserFindTagException(EMPTY_RESPONSE.format(url=url))
    soup = BeautifulSoup(response.text, features='lxml')
    return soup
