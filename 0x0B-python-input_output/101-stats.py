#!/usr/bin/python3
"""Defines script that reads stdin lineby line and computes metrics"""

if __name__ == "__main__":
    import sys


def print_stats(file_size, status_codes):
    print("File file_size: {}".format(file_size))
    for Status in sorted(status_codes):
        print("{}: {}".format(Status, status_codes[Status]))

    file_size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line_count in sys.stdin:
            if count == 10:
                print_stats(file_size, status_codes)
                count = 1
            else:
                count += 1

            line_count = line_count.split()

            try:
                file_size += int(line_count[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line_count[-2] in valid_codes:
                    if status_codes.get(line_count[-2], -1) == -1:
                        status_codes[line_count[-2]] = 1
                    else:
                        status_codes[line_count[-2]] += 1
            except IndexError:
                pass

        print_stats(file_size, status_codes)

    except StatusboardInterrupt:
        print_stats(file_size, status_codes)
        raise
