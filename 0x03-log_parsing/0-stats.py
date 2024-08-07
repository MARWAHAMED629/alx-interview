#!/usr/bin/python3
"""
Log stats module
"""
import sys
from operator import itemgetter


def log_parser(log):
    """
    Parses a log entry into its status code and file size.

    Args:
        log (str): A single log entry.

    Returns:
        tuple: A tuple containing the status code (str) and file size (int).
    """
    log_fields = log.split()
    file_size = int(log_fields[-1])
    status_code = log_fields[-2]
    return status_code, file_size


def validate_format(log):
    """
    Validates the format of a log entry.

    Args:
        log (str): A single log entry.

    Returns:
        bool: True if the log format is valid, False otherwise.
    """
    return len(log.split()) >= 7


def validate_status_code(status_code):
    """
    Checks if the status code is valid.

    Args:
        status_code (str): The status code to validate.

    Returns:
        bool: True if the status code is valid, False otherwise.
    """
    valid_status_codes = ["200", "301", "400", "401",
                          "403", "404", "405", "500"]
    return status_code in valid_status_codes


def print_log(file_size, status_codes) -> None:
    """
    Prints the log statistics including total file size and status code counts.

    Args:
        file_size (int): The total file size.
        status_codes (dict): A dictionary with status codes and their counts.
    """
    sorted_status_codes = sorted(status_codes.items(), key=itemgetter(0))
    print('File size: {}'.format(file_size))
    for code_count in sorted_status_codes:
        key = code_count[0]
        value = code_count[1]
        print("{}: {}".format(key, value))


def main():
    """
    Reads logs from stdin and prints statistics on status codes and file size.
    """
    status_codes_count = {}
    total_size = 0
    log_count = 0
    try:
        for log in sys.stdin:
            log_count += 1
            if not validate_format(log):
                continue
            status_code, file_size = log_parser(log)
            total_size += file_size
            if validate_status_code(status_code):
                entry = {status_code:
                         status_codes_count.get(status_code, 0) + 1}
                status_codes_count.update(entry)
            if log_count % 10 == 0:
                print_log(total_size, status_codes_count)
    except KeyboardInterrupt:
        print_log(total_size, status_codes_count)
        raise
    print_log(total_size, status_codes_count)


if __name__ == '__main__':
    main()
