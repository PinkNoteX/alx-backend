#!/usr/bin/env python3
""" server """
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index_range"""
    s, e = 0, 0
    for i in range(page):
        s = e
        e += page_size

    return (s, e)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def assert_int(value: int) -> None:
        """ assert_int """
        assert type(value) is int and value > 0

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get_page """
        self.assert_int(page)
        self.assert_int(page_size)
        dataset = self.dataset()
        s, e = index_range(page, page_size)
        try:
            ind = index_range(page, page_size)
            x = dataset[s:e]
        except IndexError:
            x = []
        return x

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ get_hyper """
        total_pages = len(self.dataset()) // page_size + 1
        data = self.get_page(page, page_size)
        info = {
            "page": page,
            "page_size": page_size if page_size <= len(data) else len(data),
            "total_pages": total_pages,
            "data": data,
            "prev_page": page - 1 if page > 1 else None,
            "next_page": page + 1 if page + 1 <= total_pages else None
        }
        return info
