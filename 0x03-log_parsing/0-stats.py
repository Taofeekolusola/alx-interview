#!/usr/bin/python3
import sys
import signal

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_statistics():
    """Prints the current statistics of total file size and status code counts."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def handle_signal(signal, frame):
    """Handles the signal interruption (CTRL + C) to print statistics and exit."""
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_signal)

for line in sys.stdin:
    line = line.strip()
    
    if len(line.split()) >= 7:
        ip, dash, date, request, protocol, status_code, file_size = line.split()[:7]
        if request.startswith('"GET') and request.endswith('HTTP/1.1"'):
            try:
                status_code = int(status_code)
                file_size = int(file_size)
                
                total_size += file_size
                
                if status_code in status_codes:
                    status_codes[status_code] += 1
                
                line_count += 1
                
                if line_count % 10 == 0:
                    print_statistics()
            
            except ValueError:
                continue

print_statistics()
