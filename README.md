# Port Scanner

## About

This was my fourth Python cybersecurity project.

I built this project to learn how port scanning works and how Python can be used to check whether common network ports are open or closed. The program uses Python's socket library to attempt a connection to a number of well-known TCP ports before displaying the results in a simple report.

Building this project helped me gain a better understanding of networking, socket programming and some of the services that commonly run on different ports.

## Features

- Scans common TCP ports
- Detects open and closed ports
- Displays common service names
- Counts the total number of open and closed ports
- Measures how long the scan takes
- Handles invalid IP addresses
- Handles keyboard interruption

## Technologies Used

- Python
- Socket library
- Time module

## Example Output

```text
Enter the IP address to scan:

127.0.0.1

========== Port Scan ==========
Scanning: 127.0.0.1
--------------------------------

Port 20 - FTP Data - CLOSED
Port 21 - FTP - CLOSED
Port 22 - SSH - CLOSED
Port 80 - HTTP - OPEN
Port 443 - HTTPS - CLOSED

========== Scan Summary ==========
Open ports: 1
Closed ports: 9
Time taken: 2.15 seconds
Scan complete.
```

## What I Learned

While making this project I learnt:

- How socket programming works in Python
- How port scanning is used in networking
- The purpose of common TCP ports
- How to measure how long a program takes to run
- How to improve my use of exception handling
- How to produce a simple scan summary for the user

## Future Improvements

If I continue working on this project I would like to:

- Allow users to scan custom port ranges
- Scan multiple IP addresses
- Export scan results to a text file
- Display port banners where available
- Create a simple graphical user interface
