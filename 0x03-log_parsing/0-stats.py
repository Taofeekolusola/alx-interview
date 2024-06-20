#!/usr/bin/python3
import sys
import signal

# Initialize variables to store total file size and status code counts
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

# Set the signal handler for CTRL + C
signal.signal(signal.SIGINT, handle_signal)

# Read stdin line by line
for line in sys.stdin:
    line = line.strip()
    
    # Validate and parse the input format
    if len(line.split()) >= 7:
        ip, dash, date, request, protocol, status_code, file_size = line.split()[:7]
        if request.startswith('"GET') and request.endswith('HTTP/1.1"'):
            try:
                status_code = int(status_code)
                file_size = int(file_size)
                
                # Update total file size
                total_size += file_size
                
                # Update status code count
                if status_code in status_codes:
                    status_codes[status_code] += 1
                
                # Increment line count
                line_count += 1
                
                # Print statistics after every 10 lines
                if line_count % 10 == 0:
                    print_statistics()
            
            except ValueError:
                # Skip lines where status code or file size is not an integer
                continue

# Print the final statistics when stdin ends
print_statistics()
