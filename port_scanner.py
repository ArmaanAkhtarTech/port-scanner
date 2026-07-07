import socket
import time

# Port Scanner
# This program scans some common TCP ports on a target IP address.
# It reports whether each port is open or closed and displays

# Ask the user for the IP address to scan
target = input("Enter the IP address to scan: ")

# Common ports to check
ports = {
    20: "FTP Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS"
}

# Variables to count results
open_ports = 0
closed_ports = 0

# Start timing the scan
start_time = time.time()

print("\n========== Port Scan ==========")
print("Scanning:", target)
print("--------------------------------")

try:

    # Go through every port in the dictionary
    for port in ports:

        # Create a TCP socket
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Stop the program waiting forever
        scanner.settimeout(1)

        # Try connecting to the port
        result = scanner.connect_ex((target, port))

        # Result of 0 means the port is open
        if result == 0:
            print("Port", port, "-", ports[port], "- OPEN")
            open_ports += 1

        else:
            print("Port", port, "-", ports[port], "- CLOSED")
            closed_ports += 1

        # Close the socket before checking the next port
        scanner.close()

    # Work out how long the scan took
    end_time = time.time()

    print("\n========== Scan Summary ==========")
    print("Open ports:", open_ports)
    print("Closed ports:", closed_ports)
    print("Time taken:", round(end_time - start_time, 2), "seconds")
    print("Scan complete.")

except socket.gaierror:
    print("\nError: Invalid IP address or hostname.")

except KeyboardInterrupt:
    print("\nScan stopped by user.")

except Exception as error:
    print("\nSomething went wrong while scanning.")
    print(error)