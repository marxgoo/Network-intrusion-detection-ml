from scapy.all import sniff, IP, TCP, UDP
from flow_manager import process_packet

def handle_packet(packet):
    # On ne traite que les paquets IP
    if IP in packet:
        process_packet(packet)

def start_sniffing(interface=None):
    print("Démarrage du sniffing...")
    if interface:
        sniff(iface=interface, prn=handle_packet, store=False)
    else:
        sniff(prn=handle_packet, store=False)

if __name__ == "__main__":
    # Tu peux préciser une interface start_sniffing(interface="Wi-Fi")
    start_sniffing()




