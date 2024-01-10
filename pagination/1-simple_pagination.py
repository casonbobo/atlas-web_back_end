#!/usr/bin/env python3
import csv
import math
from typing import List
"""This is supposed to be a simple helper function"""


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page, page_size):
        """Honestly the instructions on this task made no sense"""
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """This should get the page of said data"""
        assert isinstance(page, int), "page needs to be an int"
        assert isinstance(page_size, int), "page_size needs to be an int"
        assert page > 0, "page needs to be greater than 0"
        assert page_size > 0, "page_size needs to be greater than 0"

        start_index, end_index = self.index_range(page, page_size)
        data = self.dataset()


        if start_index >= len(data):
            return []

        return data[start_index:end_index]
