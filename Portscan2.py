import socket
import threading
import pyfiglet

# Function to scan a single port
def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

# Function to scan a specified number of ports
def scan_ports(host, num_ports):
    threads = []
    for port in range(1, num_ports + 1):
        thread = threading.Thread(target=scan_port, args=(host, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    # Display the SCAN_HUB banner using pyfiglet
    ascii_banner = pyfiglet.figlet_format("SCAN_HUB")
    print(ascii_banner)

    # Input target host and number of ports to scan
    target_host = input("Enter the target host (IP address or domain): ")
    num_ports = int(input("Enter the number of ports to scan: "))

    print(f"\nScanning the first {num_ports} ports on {target_host}...\n")
    scan_ports(target_host, num_ports)
    print("\nPort scanning completed.")
