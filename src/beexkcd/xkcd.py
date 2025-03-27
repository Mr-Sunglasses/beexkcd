import json
import urllib.request
from random import randint


class XKCD:

    number = 1

    def __init__(self):
        self.link = f"https://xkcd.com/{self.number}/info.0.json"

    def _make_request(self):
        data = None
        with urllib.request.urlopen(self.link) as d:
            data = d.read().decode("utf-8")
        return json.loads(data)

    @property
    def get_title(self) -> str:
        return self._make_request()["safe_title"]

    @property
    def get_image_data(self) -> str:
        img_data = None
        with urllib.request.urlopen(self._make_request()["img"]) as i:
            img_data = i.read()
        return img_data

    @property
    def next(self) -> None:
        self.number += 1
        self.link = f"https://xkcd.com/{self.number}/info.0.json"

    @property
    def previous(self) -> None:
        if self.number == 1:
            pass
        else:
            self.number -= 1
            self.link = f"https://xkcd.com/{self.number}/info.0.json"

    @property
    def random(self) -> None:
        self.number = randint(1, 3001)
        self.link = f"https://xkcd.com/{self.number}/info.0.json"
