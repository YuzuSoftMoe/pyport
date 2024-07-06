import socket

def port_scan(target, port_range):
    """
    Scans a given range of ports on a target host.
    
    :param target: The target host (IP address or hostname).
    :param port_range: A tuple containing the start and end of the port range to scan.
    """
    open_ports = []
    
    for port in range(port_range[0], port_range[1] + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        result = s.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        
        s.close()
    
    return open_ports

if __name__ == "__main__":
    target_host = input("Enter the target host (IP address or hostname): ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    
    print(f"Scanning {target_host} from port {start_port} to {end_port}...")
    open_ports = port_scan(target_host, (start_port, end_port))
    
    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(port)
    else:
        print("No open ports found.")
