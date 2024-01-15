#!/usr/bin/env python3
"""
    This is a file that will be added to over the course of the project.
    This project is based around learning data obfuscation and encryption through Atlas
    I do not know what I am doing
"""
import re
import list


def filter_datum(fields: list[str], redaction: str, message: str, separator: str) -> str:
    pattern = '|'.join(fields)
    obfuscated_message = re.sub(pattern, redaction, message)
    return obfuscated_message
