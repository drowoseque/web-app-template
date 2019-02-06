from tornado.web import RequestHandler
from typing import List, Tuple

from {{cookiecutter.package_name}}.web.handlers import PingHandler

ping_url = (r'/ping/', PingHandler)

custom_urls = []


def get_all_urls() -> List[Tuple[str, RequestHandler]]:
    return custom_urls + [ping_url]
