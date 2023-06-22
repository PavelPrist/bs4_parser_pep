from pathlib import Path

BASE_DIR = Path(__file__).parent
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
DT_FORMAT = '%d.%m.%Y %H:%M:%S'
EMPTY_RESPONSE = 'Пустой ответ или 404 Not Found по ссылке {url}'
EXPECTED_STATUS = {
    'A': ('Active', 'Accepted'),
    'D': ('Deferred',),
    'F': ('Final',),
    'P': ('Provisional',),
    'R': ('Rejected',),
    'S': ('Superseded',),
    'W': ('Withdrawn',),
    '': ('Draft', 'Active'),
}
LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'
MAIN_DOC_URL = 'https://docs.python.org/3/'
PEPS_PYTHON_URL = 'https://peps.python.org/'
TR_NOT_FOUND = 'Не найден тег tr'
