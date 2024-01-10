#!/usr/env/bin python3
"""This is supposed to be a simple helper function"""



def index_range(page, page_size) {
    """Honestly the instructions on this task made no sense"""
    start_index = (page - 1) * page_size

    end_index = start_index + page_size

    return (start_index, end_index)
}

