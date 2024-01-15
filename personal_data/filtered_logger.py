#!/usr/bin/env python3
"""
    This is a file that will be added to over the course of the project.
    This project is based around learning data obfuscation
    and encryption through Atlas
    I do not know what I am doing
"""
import re
import typing


def filter_datum(fields: typing.List[str], redaction: str,
                 message: str, separator: str) -> str:
    """This is a func to obfuscate data through parameters"""
    pattern = '|'.join(f'(?<={separator}{field})(.*?)(?={separator}|$)'
                        for field in fields)
    obfuscated_message = re.sub(pattern, f'{separator}{redaction}', message)
    return obfuscated_message
