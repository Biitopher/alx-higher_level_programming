#!/usr/bin/python3
"""Defines script that reads stdin line by line and computes metrics"""


import sys
import signal

total_file_size = 0
status_code_counts = {}

line_count = 0

def print_statistics():
    print("Total file size: File size:", total_file_size)
    for status_code in sorted(status_code_counts.keys()):
        count = status_code_counts[status_code]
        print(status_code, ":", count)

def handle_interrupt(signal, frame):
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        line = line.strip()
        if line:
            line_count += 1
            _, _, _, _, _, status_code, file_size = line.split()
            total_file_size += int(file_size)
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            else:
                status_code_counts[status_code] = 1
            if line_count % 10 == 0:
                print_statistics()

except KeyboardInterrupt:
    pass
print_statistics()
