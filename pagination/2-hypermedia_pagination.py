#!/usr/bin/env python3
"""This is supposed to be a simple helper function"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Why do you have to document this init"""
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

    def get_hyper(page=1, page_size=10):
        data = get_page(page, page_size)
        total_entries = len(data)
        total_pages = math.ceil(total_entries / page_size)
        next_page = None if page == total_pages else page + 1
        prev_page = None if page == 1 else page - 1
        return {'page_size': page_size, 'page': page,
                'data': data, 'next_page': next_page,
                'prev_time': prev_time, 'total_pages': total_pages}
