import socket  # Import socket module for network operations

def resolve_domain(domain_name):
    """Resolve a domain name to its corresponding IP address."""
    try:
        ip_address = socket.gethostbyname(domain_name)  # Get IP from domain
        print(f"Domain: {domain_name} -> IP: {ip_address}")
    except socket.gaierror:  # Handle invalid domain
        print(f"Error: Could not resolve domain '{domain_name}'.")

def resolve_ip(ip_address):
    """Resolve an IP address to its corresponding domain name."""
    try:
        domain_name = socket.gethostbyaddr(ip_address)[0]  # Get domain from IP
        print(f"IP: {ip_address} -> Domain: {domain_name}")
    except socket.herror:  # Handle invalid IP
        print(f"Error: Could not resolve IP '{ip_address}'.")

# ---------------- MAIN ---------------- #

print("=== DOMAIN/IP RESOLVER ===")
print("Choose an option:")
print("1 - Domain to IP")
print("2 - IP to Domain")

choice = input("Enter your choice (1 or 2): ").strip()

if choice == '1':
    domain_input = input("Enter domain name (e.g., example.com): ").strip()
    resolve_domain(domain_input)

elif choice == '2':
    ip_input = input("Enter IP address (e.g., 8.8.8.8): ").strip()
    resolve_ip(ip_input)

else:
    print("Invalid choice. Please enter 1 or 2.")
