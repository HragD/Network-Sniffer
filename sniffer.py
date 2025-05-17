from scapy.all import sniff, IP
from colorama import Fore, Style

def process_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        print(Fore.CYAN + f"[+] {ip_layer.src} -> {ip_layer.dst} | Proto: {ip_layer.proto}" + Style.RESET_ALL)

def main():
    print(Fore.GREEN + "[*] Starting packet capture (Press Ctrl+C to stop)..." + Style.RESET_ALL)
    sniff(filter="ip", prn=process_packet, store=False)

if __name__ == "__main__":
    main()
