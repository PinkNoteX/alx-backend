#!/usr/bin/env python3
""" index_range """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index_range"""
    s, e = 0, 0
    for i in range(page):
        s = e
        e += page_size

    return (s, e)
