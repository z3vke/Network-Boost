import os
import subprocess
import sys
import webbrowser
import ctypes

try:
    from colorama import Fore, Style, init
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])
    from colorama import Fore, Style, init

init(autoreset=True)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    script = sys.argv[0]
    params = ' '.join([f'"{param}"' for param in sys.argv[1:]])
    command = f'powershell Start-Process -FilePath "python" -ArgumentList \'"{script}" {params}\' -Verb RunAs'
    subprocess.run(command, shell=True)

# Network tweaks functions
def disable_nagles_algorithm():
    subprocess.run('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces\\{GUID}" /v "TCPNoDelay" /t REG_DWORD /d 1 /f', shell=True)
    subprocess.run('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces\\{GUID}" /v "TcpAckFrequency" /t REG_DWORD /d 1 /f', shell=True)
    print("Nagle's Algorithm disabled.")

def optimize_dns():
    subprocess.run('netsh interface ip set dns "Ethernet" static 1.1.1.1', shell=True)
    subprocess.run('netsh interface ip add dns "Ethernet" 8.8.8.8 index=2', shell=True)
    print("DNS optimized.")

def flush_dns_cache():
    subprocess.run('ipconfig /flushdns', shell=True)
    print("DNS cache flushed.")

def disable_ipv6():
    subprocess.run('netsh interface ipv6 set global state=disabled', shell=True)
    print("IPv6 disabled.")

def increase_network_performance():
    subprocess.run('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile" /v "NetworkThrottlingIndex" /t REG_DWORD /d 4294967295 /f', shell=True)
    print("Network performance increased.")

def reset_network_adapter():
    subprocess.run('netsh int ip reset', shell=True)
    subprocess.run('netsh winsock reset', shell=True)
    print("Network adapter reset.")

def disable_qos():
    subprocess.run('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Psched" /v "Start" /t REG_DWORD /d 1 /f', shell=True)
    print("QoS Packet Scheduler disabled.")

def disable_eee():
    subprocess.run('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces\\{GUID}" /v "EEE" /t REG_DWORD /d 0 /f', shell=True)
    print("Energy Efficient Ethernet (EEE) disabled.")

def optimize_nic_settings():
    subprocess.run('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces\\{GUID}" /v "ReceiveBuffers" /t REG_DWORD /d 1024 /f', shell=True)
    subprocess.run('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces\\{GUID}" /v "TransmitBuffers" /t REG_DWORD /d 512 /f', shell=True)
    subprocess.run('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces\\{GUID}" /v "InterruptModeration" /t REG_DWORD /d 0 /f', shell=True)
    print("NIC settings optimized.")

def disable_jumbo_frames():
    subprocess.run('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces\\{GUID}" /v "JumboPacket" /t REG_DWORD /d 1514 /f', shell=True)
    print("Jumbo Frames disabled.")

def enable_tcp_fast_open():
    subprocess.run('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" /v "TcpFastOpen" /t REG_DWORD /d 1 /f', shell=True)
    print("TCP Fast Open enabled.")

def disable_auto_tuning():
    subprocess.run('netsh int tcp set global autotuninglevel=disabled', shell=True)
    print("TCP auto-tuning disabled.")

def optimize_tcp_ip():
    subprocess.run('netsh int tcp set global rss=enabled', shell=True)
    subprocess.run('netsh int tcp set global chimney=enabled', shell=True)
    subprocess.run('netsh int tcp set global dca=enabled', shell=True)
    subprocess.run('netsh int tcp set global ecncapability=disabled', shell=True)
    print("TCP/IP settings optimized.")

def disable_large_send_offload():
    subprocess.run('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces\\{GUID}" /v "LsoV2IPv4" /t REG_DWORD /d 0 /f', shell=True)
    subprocess.run('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces\\{GUID}" /v "LsoV2IPv6" /t REG_DWORD /d 0 /f', shell=True)
    print("Large Send Offload (LSO) disabled.")

def optimize_packet_coalescing():
    subprocess.run('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces\\{GUID}" /v "EnablePacketCoalescing" /t REG_DWORD /d 1 /f', shell=True)
    print("Packet Coalescing optimized.")

def disable_flow_control():
    subprocess.run('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces\\{GUID}" /v "FlowControl" /t REG_DWORD /d 0 /f', shell=True)
    print("Flow Control disabled.")

def increase_rss_queues():
    subprocess.run('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces\\{GUID}" /v "NumRssQueues" /t REG_DWORD /d 4 /f', shell=True)
    print("Increased RSS Queues to 4.")

def enable_tcp_sack():
    subprocess.run('netsh int tcp set global sack=enabled', shell=True)
    print("TCP Selective Acknowledgment (SACK) enabled.")

def disable_power_saving_features():
    subprocess.run('powercfg -change -standby-timeout-ac 0', shell=True)
    subprocess.run('powercfg -change -hibernate-timeout-ac 0', shell=True)
    print("Disabled power-saving features for better network performance.")



# Display the menu
def display_menu():
    os.system('cls' if os.name == 'nt' else 'clear')

    ascii_art = """

 /$$    /$$ /$$     /$$ /$$$$$$$   /$$$$$$        /$$$$$$$$ /$$      /$$ /$$$$$$$$  /$$$$$$  /$$   /$$  /$$$$$$ 
| $$   | $$|  $$   /$$/| $$__  $$ /$$__  $$      |__  $$__/| $$  /$ | $$| $$_____/ /$$__  $$| $$  /$$/ /$$__  $$
| $$   | $$ \  $$ /$$/ | $$  \ $$| $$  \ $$         | $$   | $$ /$$$| $$| $$      | $$  \ $$| $$ /$$/ | $$  \__/
|  $$ / $$/  \  $$$$/  | $$$$$$$/| $$  | $$         | $$   | $$/$$ $$ $$| $$$$$   | $$$$$$$$| $$$$$/  |  $$$$$$ 
 \  $$ $$/    \  $$/   | $$__  $$| $$  | $$         | $$   | $$$$_  $$$$| $$__/   | $$__  $$| $$  $$   \____  $$
  \  $$$/      | $$    | $$  \ $$| $$  | $$         | $$   | $$$/ \  $$$| $$      | $$  | $$| $$\  $$  /$$  \ $$
   \  $/       | $$    | $$  | $$|  $$$$$$/         | $$   | $$/   \  $$| $$$$$$$$| $$  | $$| $$ \  $$|  $$$$$$/
    \_/        |__/    |__/  |__/ \______/          |__/   |__/     \__/|________/|__/  |__/|__/  \__/ \______/ 
                                                                                                                

creator: zevke & zex
development: zevke  
discord: zogp                                                                                                              
                                                                                                                
                                                                                               
"""

    terminal_width = os.get_terminal_size().columns
    centered_ascii_art = "\n".join(line.center(terminal_width) for line in ascii_art.splitlines())
    print(Fore.BLUE + centered_ascii_art)
    print("\n" + "=" * terminal_width)
    print("=" * terminal_width)

    # Menu items structured into two columns
    menu_column_1 = [
        f"                 {Fore.BLUE}[1]{Style.RESET_ALL} Disable Nagle's Algorithm        ",
        f"              {Fore.BLUE}[3]{Style.RESET_ALL} Optimize DNS                   ",
        f"             {Fore.BLUE}[5]{Style.RESET_ALL} Increase Network Performance     ",
        f"                      {Fore.BLUE}[7]{Style.RESET_ALL} Reset Network Adapter           ",
        f"                        {Fore.BLUE}[9]{Style.RESET_ALL} Enable TCP Fast Open            ",
        f"                           {Fore.BLUE}[11]{Style.RESET_ALL} Disable TCP Auto-Tuning       ",
        f"                             {Fore.BLUE}[13]{Style.RESET_ALL} Disable Large Send Offload      ",
        f"                           {Fore.BLUE}[15]{Style.RESET_ALL} Disable Flow Control            ",
        f"                              {Fore.BLUE}[17]{Style.RESET_ALL} Enable TCP Selective Acknowledgment"
    ]

    menu_column_2 = [
        f"{Fore.BLUE}[2]{Style.RESET_ALL} Flush DNS Cache",
        f"  {Fore.BLUE}[4]{Style.RESET_ALL} Disable IPv6",
        f"{Fore.BLUE}[6]{Style.RESET_ALL} Disable QoS",
        f" {Fore.BLUE}[8]{Style.RESET_ALL} Disable Jumbo Frames",
        f" {Fore.BLUE}[10]{Style.RESET_ALL} Optimize NIC Settings",
        f"  {Fore.BLUE}[12]{Style.RESET_ALL} Optimize TCP/IP Settings",
        f"{Fore.BLUE}[14]{Style.RESET_ALL} Optimize Packet Coalescing",
        f"{Fore.BLUE}[16]{Style.RESET_ALL} Increase RSS Queues to 4",
        f"{Fore.BLUE}[18]{Style.RESET_ALL} Disable Power Saving Features"
    ]

    print(f"{Fore.MAGENTA}[A]{Style.RESET_ALL} Apply All Tweaks (1-18)".center(terminal_width))
    print("\n" + "-" * terminal_width)

    # Combine the two columns and print them
    for item1, item2 in zip(menu_column_1, menu_column_2):
        print(f"{item1}  {item2}".center(terminal_width))

    print("\n" + "-" * terminal_width)
    print(f"                    {Fore.BLUE}[E]{Style.RESET_ALL} Exit the Utility)       

def handle_input(choice):
    if choice == '1':
        disable_nagles_algorithm()
    elif choice == '2':
        flush_dns_cache()
    elif choice == '3':
        optimize_dns()
    elif choice == '4':
        disable_ipv6()
    elif choice == '5':
        increase_network_performance()
    elif choice == '6':
        disable_qos()
    elif choice == '7':
        reset_network_adapter()
    elif choice == '8':
        disable_jumbo_frames()
    elif choice == '9':
        enable_tcp_fast_open()
    elif choice == '10':
        optimize_nic_settings()
    elif choice == '11':
        disable_auto_tuning()
    elif choice == '12':
        optimize_tcp_ip()
    elif choice == '13':
        disable_large_send_offload()
    elif choice == '14':
        optimize_packet_coalescing()
    elif choice == '15':
        disable_flow_control()
    elif choice == '16':
        increase_rss_queues()
    elif choice == '17':
        enable_tcp_sack()
    elif choice == '18':
        disable_power_saving_features()
    elif choice.lower() == 'a':
        disable_nagles_algorithm()
        flush_dns_cache()
        optimize_dns()
        disable_ipv6()
        increase_network_performance()
        disable_qos()
        reset_network_adapter()
        disable_jumbo_frames()
        enable_tcp_fast_open()
        optimize_nic_settings()
        disable_auto_tuning()
        optimize_tcp_ip()
        disable_large_send_offload()
        optimize_packet_coalescing()
        disable_flow_control()
        increase_rss_queues()
        enable_tcp_sack()
        disable_power_saving_features()
        open_staroptimizer()
        print("All tasks completed.")
    elif choice.lower() == 'e':
        print("Exiting the utility.")
        exit()
    elif choice.lower() == 'w':
        open_staroptimizer()

def main():
    if not is_admin():
        run_as_admin()
        sys.exit(0)

    while True:
        display_menu()
        choice = input("Select an option: ")
        handle_input(choice)
        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
