#!/usr/bin/env python3
"""
    This is a file that will be added to over the course of the project.
    This project is based around learning data obfuscation
    and encryption through Atlas
    I do not know what I am doing
"""
import re
from typing import List
import logging


PII_FIELDS: tuple = ("name", "email", "ssn", "password", "phone")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """This is should be able to recieve data and feed it into datum"""
        obfuscated_message = super().format(record)
        return filter_datum(
            self.fields, self.REDACTION, obfuscated_message, self.SEPARATOR
        )


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """This is a func to obfuscate data through parameters"""
    for field in fields:
        message = re.sub(field + "=.*?" + separator,
                         field + "=" + redaction + separator, message)
    return message

def main():
    """a func that returns a connector"""
    log = get_logger()
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM users;")

    for row in cursor:
        log.info(row[0])
    cursor.close()
    db.close()

def get_logger() -> logging.Logger:
    """Return a configured logger."""
    log = logging.getLogger("user_data")
    log.setLevel(logging.INFO)
    log.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))

    log.addHandler(handler)

    return log
