"""
CyberSuite Pro v4.0
Cybersecurity Suite - Ultimate Professional Security Toolkit
Created by: Sandaru
"""

import os
import sys
import subprocess
import requests
import hashlib
import socket
import platform
import random
import string
import uuid
import re
from datetime import datetime

# ============================================
# PROFESSIONAL COLORS
# ============================================
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    
    # Standard
    BLACK = '\033[30m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    
    # Custom Neon
    NEON = '\033[38;2;0;255;136m'
    NEON_BLUE = '\033[38;2;0;200;255m'
    NEON_PINK = '\033[38;2;255;0;150m'
    GOLD = '\033[38;2;255;215;0m'
    ORANGE = '\033[38;2;255;165;0m'
    SILVER = '\033[38;2;192;192;192m'
    DARK_GRAY = '\033[38;2;50;50;50m'

# ============================================
# CONFIGURATION
# ============================================
AUTHOR = "Sandaru"
YEAR = datetime.now().year

# ============================================
# UI FUNCTIONS
# ============================================
def clear():
    os.system('clear')

def header():
    print(f"""
{Colors.NEON}╔══════════════════════════════════════════════════════════════════════════╗
║                                                                                  ║
║   {Colors.BOLD}{Colors.WHITE} ██████╗██╗   ██╗██████╗ ███████╗██████╗ ███████╗{Colors.RESET}{Colors.NEON}        ║
║   {Colors.BOLD}{Colors.WHITE}██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██╔════╝{Colors.RESET}{Colors.NEON}        ║
║   {Colors.BOLD}{Colors.WHITE}███████╗ ╚████╔╝ ██████╔╝█████╗  ██████╔╝███████╗{Colors.RESET}{Colors.NEON}        ║
║   {Colors.BOLD}{Colors.WHITE}╚════██║  ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗╚════██║{Colors.RESET}{Colors.NEON}        ║
║   {Colors.BOLD}{Colors.WHITE}███████║   ██║   ██████╔╝███████╗██║  ██║███████║{Colors.RESET}{Colors.NEON}        ║
║   {Colors.BOLD}{Colors.WHITE}╚══════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝{Colors.RESET}{Colors.NEON}        ║
║                                                                                  ║
║   {Colors.BOLD}{Colors.WHITE}🔒  CYBERSECURITY SUITE{Colors.RESET}{Colors.NEON}                           {Colors.DIM}v4.0{Colors.NEON}   ║
║   {Colors.DIM}Professional Security Toolkit{Colors.NEON}                                        ║
║                                                                                  ║
║   {Colors.DIM}Created by: {Colors.WHITE}{AUTHOR}{Colors.NEON}  |  {Colors.DIM}{YEAR}{Colors.NEON}                                       ║
║                                                                                  ║
╚══════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
""")

def menu():
    print(f"""
{Colors.BLUE}╔══════════════════════════════════════════════════════════════════════════╗
║  {Colors.BOLD}{Colors.WHITE}📋  CYBERSECURITY SUITE  •  TOOLS MENU{Colors.RESET}{Colors.BLUE}  {Colors.DIM}(20 Tools){Colors.RESET}{Colors.BLUE}           ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                                  ║
║  {Colors.GREEN}┌─ 1.{Colors.RESET}  🔐 Linux Hardening     {Colors.GREEN}┌─ 2.{Colors.RESET}  📦 System Update          ║
║  {Colors.GREEN}├─ 3.{Colors.RESET}  🔍 Breach Check       {Colors.GREEN}├─ 4.{Colors.RESET}  🧪 File Analysis          ║
║  {Colors.GREEN}├─ 5.{Colors.RESET}  🌐 Network Scanner   {Colors.GREEN}├─ 6.{Colors.RESET}  🔑 Password Generator     ║
║  {Colors.GREEN}├─ 7.{Colors.RESET}  🔍 Whois Lookup      {Colors.GREEN}├─ 8.{Colors.RESET}  🌐 DNS Lookup            ║
║  {Colors.GREEN}├─ 9.{Colors.RESET}  📦 Install Tools     {Colors.GREEN}├─10.{Colors.RESET}  🔌 Port Scanner          ║
║  {Colors.GREEN}├─11.{Colors.RESET}  🔐 Hash Generator    {Colors.GREEN}├─12.{Colors.RESET}  📝 Base64 Tool           ║
║  {Colors.GREEN}├─13.{Colors.RESET}  📊 System Resources  {Colors.GREEN}├─14.{Colors.RESET}  📊 Security Report       ║
║  {Colors.GREEN}├─15.{Colors.RESET}  🌐 IP Info          {Colors.GREEN}├─16.{Colors.RESET}  🌐 HTTP Headers          ║
║  {Colors.GREEN}├─17.{Colors.RESET}  🎲 Random Generator  {Colors.GREEN}├─18.{Colors.RESET}  🎨 Color Demo            ║
║  {Colors.GREEN}└─19.{Colors.RESET}  📊 System Info                                      ║
║                                                                                  ║
╠══════════════════════════════════════════════════════════════════════════╣
║  {Colors.RED}┌─ 20.{Colors.RESET}  🚪  EXIT  {Colors.DIM}—  Close Application{Colors.RESET}{Colors.BLUE}                          ║
╚══════════════════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.DIM}  ⚡  {Colors.WHITE}help{Colors.DIM}  •  Commands List     {Colors.WHITE}clear{Colors.DIM}  •  Clear Screen{Colors.RESET}
""")

def status(message, type_="info"):
    icons = {
        "success": f"{Colors.GREEN}✔{Colors.RESET}",
        "error": f"{Colors.RED}✘{Colors.RESET}",
        "warning": f"{Colors.YELLOW}⚠{Colors.RESET}",
        "info": f"{Colors.NEON_BLUE}●{Colors.RESET}",
        "processing": f"{Colors.ORANGE}⟳{Colors.RESET}"
    }
    icon = icons.get(type_, "●")
    colors = {
        "success": Colors.GREEN,
        "error": Colors.RED,
        "warning": Colors.YELLOW,
        "info": Colors.NEON_BLUE,
        "processing": Colors.ORANGE
    }
    color = colors.get(type_, Colors.WHITE)
    print(f"{color}  {icon}  {message}{Colors.RESET}")

def section(title):
    print(f"""
{Colors.PURPLE}╔══════════════════════════════════════════════════════════════════════════╗
║  {Colors.BOLD}{Colors.WHITE}▶  {title}{Colors.RESET}{Colors.PURPLE}                                                 ║
╚══════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
""")

def pause():
    input(f"\n{Colors.DIM}  Press Enter to continue...{Colors.RESET}")

# ============================================
# SYSTEM INFO
# ============================================
def system_info():
    clear()
    header()
    section("📊 SYSTEM INFORMATION")
    
    info = {
        "💻 OS": platform.system(),
        "🔧 Version": platform.version()[:30],
        "🏷️ Hostname": socket.gethostname(),
        "🌐 IP": socket.gethostbyname(socket.gethostname()),
        "📟 Arch": platform.machine()
    }
    
    for key, val in info.items():
        print(f"  {Colors.DIM}{key}:{Colors.RESET}  {Colors.WHITE}{val}{Colors.RESET}")
    
    pause()

# ============================================
# 1. LINUX HARDENING
# ============================================
def linux_harden():
    clear()
    header()
    section("🔐 LINUX HARDENING")
    
    print(f"\n{Colors.ORANGE}  ⟳  Applying security settings...{Colors.RESET}\n")
    
    commands = [
        ("TCP Syncookies", "sudo sysctl -w net.ipv4.tcp_syncookies=1"),
        ("IP Forwarding", "sudo sysctl -w net.ipv4.ip_forward=0"),
        ("RP Filter", "sudo sysctl -w net.ipv4.conf.all.rp_filter=1"),
        ("Firewall", "sudo ufw enable"),
        ("Root Login", "sudo passwd -l root"),
    ]
    
    success = 0
    for name, cmd in commands:
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                status(f"{name} applied", "success")
                success += 1
            else:
                status(f"{name} failed", "error")
        except:
            status(f"{name} error", "error")
    
    print(f"\n{Colors.GREEN}  ✅  {success}/{len(commands)} hardening applied{Colors.RESET}")
    pause()

# ============================================
# 2. SYSTEM UPDATE
# ============================================
def system_update():
    clear()
    header()
    section("📦 SYSTEM UPDATE")
    
    print(f"\n{Colors.ORANGE}  ⟳  Updating system...{Colors.RESET}\n")
    
    cmds = [
        ("Update list", "sudo apt update"),
        ("Upgrade", "sudo apt upgrade -y"),
        ("Clean", "sudo apt autoremove -y"),
    ]
    
    for name, cmd in cmds:
        status(f"{name}...", "processing")
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            status(f"{name} complete", "success")
        else:
            status(f"{name} failed", "error")
    
    pause()

# ============================================
# 3. BREACH CHECK
# ============================================
def breach_check():
    clear()
    header()
    section("🔍 BREACH CHECK")
    
    email = input(f"{Colors.CYAN}  📧  Email: {Colors.RESET}")
    
    if not email:
        status("No email provided", "error")
        pause()
        return
    
    status(f"Checking {email}...", "processing")
    
    try:
        url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            breaches = response.json()
            status(f"{len(breaches)} breaches found!", "error")
            for b in breaches[:5]:
                print(f"    {Colors.DIM}📌  {b['Name']}  ({b['BreachDate']}){Colors.RESET}")
        elif response.status_code == 404:
            status("No breaches found! You're safe.", "success")
        else:
            status(f"Status: {response.status_code}", "warning")
    except:
        status("Connection error", "error")
    
    pause()

# ============================================
# 4. FILE ANALYSIS
# ============================================
def file_analysis():
    clear()
    header()
    section("🧪 FILE ANALYSIS")
    
    path = input(f"{Colors.CYAN}  📁  File path: {Colors.RESET}")
    
    if not os.path.exists(path):
        status("File not found!", "error")
        pause()
        return
    
    with open(path, "rb") as f:
        data = f.read()
        md5 = hashlib.md5(data).hexdigest()
        sha256 = hashlib.sha256(data).hexdigest()
    
    susp = any(x in data for x in [b'<script', b'eval(', b'base64'])
    
    print(f"""
  {Colors.DIM}📁 Name:{Colors.RESET}  {Colors.WHITE}{os.path.basename(path)}{Colors.RESET}
  {Colors.DIM}📊 Size:{Colors.RESET}  {Colors.WHITE}{len(data):,} bytes{Colors.RESET}
  {Colors.DIM}🔑 MD5:{Colors.RESET}   {Colors.WHITE}{md5}{Colors.RESET}
  {Colors.DIM}🔒 SHA256:{Colors.RESET} {Colors.WHITE}{sha256[:32]}...{Colors.RESET}
  {Colors.DIM}⚠️ Suspicious:{Colors.RESET}  {Colors.WHITE}{'Yes' if susp else 'No'}{Colors.RESET}
    """)
    
    if susp:
        status("Suspicious patterns detected!", "warning")
    
    pause()

# ============================================
# 5. NETWORK SCANNER
# ============================================
def network_scan():
    clear()
    header()
    section("🌐 NETWORK SCANNER")
    
    target = input(f"{Colors.CYAN}  🎯  Target: {Colors.RESET}")
    
    if not target:
        status("No target", "error")
        pause()
        return
    
    status(f"Scanning {target}...", "processing")
    
    try:
        ip = socket.gethostbyname(target)
        status(f"IP: {ip}", "success")
        
        result = subprocess.run(f"ping -c 2 {target}", shell=True, capture_output=True, text=True)
        for line in result.stdout.split('\n'):
            if "time=" in line:
                print(f"    {Colors.DIM}{line.strip()}{Colors.RESET}")
        
        ports = [22, 80, 443, 8080, 3306]
        open_ports = []
        for p in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            if s.connect_ex((ip, p)) == 0:
                open_ports.append(p)
            s.close()
        
        if open_ports:
            status(f"Open ports: {open_ports}", "warning")
        else:
            status("No common ports open", "info")
    except:
        status("Scan failed", "error")
    
    pause()

# ============================================
# 6. PASSWORD GENERATOR
# ============================================
def password_gen():
    clear()
    header()
    section("🔑 PASSWORD GENERATOR")
    
    print(f"""
  {Colors.DIM}1.  Weak  (8 chars){Colors.RESET}
  {Colors.DIM}2.  Medium  (16 chars){Colors.RESET}
  {Colors.DIM}3.  Strong  (24 chars){Colors.RESET}
  {Colors.DIM}4.  Very Strong  (32 chars){Colors.RESET}
    """)
    
    choice = input(f"{Colors.CYAN}  Option: {Colors.RESET}")
    length = {"1": 8, "2": 16, "3": 24, "4": 32}.get(choice, 16)
    
    chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-="
    password = ''.join(random.choice(chars) for _ in range(length))
    
    print(f"""
  {Colors.GREEN}🔐  {password}{Colors.RESET}
  {Colors.DIM}📏  Length:  {length}{Colors.RESET}
    """)
    
    pause()

# ============================================
# 7. WHOIS LOOKUP
# ============================================
def whois_lookup():
    clear()
    header()
    section("🔍 WHOIS LOOKUP")
    
    domain = input(f"{Colors.CYAN}  🌐  Domain: {Colors.RESET}")
    
    if not domain:
        status("No domain", "error")
        pause()
        return
    
    status(f"Looking up {domain}...", "processing")
    
    try:
        result = subprocess.run(f"whois {domain}", shell=True, capture_output=True, text=True)
        lines = result.stdout.split('\n')[:15]
        for line in lines:
            if any(x in line.lower() for x in ['domain', 'registrar', 'creation', 'expiry']):
                print(f"    {Colors.DIM}{line.strip()}{Colors.RESET}")
    except:
        status("Lookup failed", "error")
    
    pause()

# ============================================
# 8. DNS LOOKUP
# ============================================
def dns_lookup():
    clear()
    header()
    section("🌐 DNS LOOKUP")
    
    domain = input(f"{Colors.CYAN}  🌐  Domain: {Colors.RESET}")
    
    if not domain:
        status("No domain", "error")
        pause()
        return
    
    status(f"Resolving {domain}...", "processing")
    
    records = {"A": "nslookup -type=A", "MX": "nslookup -type=MX", "NS": "nslookup -type=NS"}
    
    for rtype, cmd in records.items():
        result = subprocess.run(f"{cmd} {domain}", shell=True, capture_output=True, text=True)
        if result.stdout.strip():
            print(f"  {Colors.BOLD}{Colors.WHITE}{rtype}{Colors.RESET}")
            for line in result.stdout.split('\n'):
                if line.strip() and not line.startswith('Server'):
                    print(f"    {Colors.DIM}{line.strip()}{Colors.RESET}")
    
    pause()

# ============================================
# 9. INSTALL TOOLS
# ============================================
def install_tools():
    clear()
    header()
    section("📦 INSTALL TOOLS")
    
    tools = [
        ("nmap", "Network scanner"),
        ("gobuster", "Directory busting"),
        ("ffuf", "Web fuzzing"),
        ("sqlmap", "SQL injection"),
        ("hydra", "Password cracking"),
        ("john", "Password cracking"),
        ("metasploit-framework", "Exploitation"),
    ]
    
    for i, (tool, desc) in enumerate(tools, 1):
        print(f"  {Colors.DIM}{Colors.GREEN}{i:2}.{Colors.RESET}{Colors.DIM}  {tool}  —  {desc}{Colors.RESET}")
    
    print(f"\n  {Colors.DIM}{Colors.GREEN}a.{Colors.RESET}{Colors.DIM}  Install all{Colors.RESET}")
    print(f"  {Colors.DIM}{Colors.RED}b.{Colors.RESET}{Colors.DIM}  Cancel{Colors.RESET}")
    
    choice = input(f"\n{Colors.CYAN}  Select: {Colors.RESET}")
    
    if choice == 'b':
        return
    
    if choice == 'a':
        selected = tools
    else:
        try:
            selected = [tools[int(choice)-1]]
        except:
            status("Invalid", "error")
            pause()
            return
    
    status("Installing...", "processing")
    for tool, desc in selected:
        result = subprocess.run(f"sudo apt install {tool} -y", shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            status(f"{tool} installed", "success")
        else:
            status(f"{tool} failed", "error")
    
    pause()

# ============================================
# 10. PORT SCANNER
# ============================================
def port_scanner():
    clear()
    header()
    section("🔌 PORT SCANNER")
    
    target = input(f"{Colors.CYAN}  🎯  IP Address: {Colors.RESET}")
    
    if not target:
        status("No target provided", "error")
        pause()
        return
    
    # Validate IP
    try:
        socket.gethostbyname(target)
    except:
        status("Invalid IP address", "error")
        pause()
        return
    
    print(f"\n{Colors.ORANGE}  ⟳  Scanning {target}...{Colors.RESET}\n")
    
    # Common ports with service names
    common_ports = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        993: "IMAPS",
        995: "POP3S",
        3306: "MySQL",
        3389: "RDP",
        5432: "PostgreSQL",
        8080: "HTTP-Alt",
        8443: "HTTPS-Alt",
        27017: "MongoDB"
    }
    
    open_ports = []
    closed_ports = 0
    total_scanned = len(common_ports)
    
    print(f"  {Colors.DIM}Scanning {total_scanned} common ports...{Colors.RESET}\n")
    
    for port, service in common_ports.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        sock.close()
        
        if result == 0:
            open_ports.append((port, service))
            print(f"  {Colors.GREEN}✅  Port {port}  ({service})  —  OPEN{Colors.RESET}")
        else:
            closed_ports += 1
            # Optionally show closed ports (uncomment if needed)
            # print(f"  {Colors.DIM}❌  Port {port}  ({service})  —  CLOSED{Colors.RESET}")
    
    # Show summary
    print(f"""
{Colors.PURPLE}╔══════════════════════════════════════════════════════════════════════════╗
║  {Colors.BOLD}{Colors.WHITE}📊  SCAN RESULTS{Colors.RESET}{Colors.PURPLE}                                                ║
╚══════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
""")
    
    if open_ports:
        print(f"  {Colors.GREEN}✅  Open Ports Found:  {len(open_ports)}{Colors.RESET}\n")
        for port, service in open_ports:
            print(f"    {Colors.GREEN}▶  Port {port}  ({Colors.WHITE}{service}{Colors.GREEN}){Colors.RESET}")
    else:
        print(f"  {Colors.YELLOW}⚠️  No open ports found on common ports{Colors.RESET}")
    
    print(f"""
  {Colors.DIM}📊  Summary:{Colors.RESET}
  {Colors.DIM}   •  Ports Scanned:  {total_scanned}{Colors.RESET}
  {Colors.DIM}   •  Open Ports:     {Colors.GREEN}{len(open_ports)}{Colors.RESET}
  {Colors.DIM}   •  Closed Ports:   {Colors.RED}{closed_ports}{Colors.RESET}
  {Colors.DIM}   •  Target:         {Colors.WHITE}{target}{Colors.RESET}
    """)
    
    # Save results option
    if open_ports:
        if input(f"\n{Colors.CYAN}  Save results to file? (y/n): {Colors.RESET}").lower() == 'y':
            with open("port_scan_results.txt", "w") as f:
                f.write(f"Port Scan Results - {target}\n")
                f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 40 + "\n")
                for port, service in open_ports:
                    f.write(f"Port {port} ({service}) - OPEN\n")
                f.write(f"\nTotal open ports: {len(open_ports)}")
            status("Results saved to port_scan_results.txt", "success")
    
    pause()
    
# ============================================
# 11. HASH GENERATOR
# ============================================
def hash_gen():
    clear()
    header()
    section("🔐 HASH GENERATOR")
    
    text = input(f"{Colors.CYAN}  📝  Text: {Colors.RESET}")
    
    if not text:
        status("No text", "error")
        pause()
        return
    
    data = text.encode('utf-8')
    
    print(f"""
  {Colors.DIM}MD5:{Colors.RESET}     {Colors.WHITE}{hashlib.md5(data).hexdigest()}{Colors.RESET}
  {Colors.DIM}SHA1:{Colors.RESET}    {Colors.WHITE}{hashlib.sha1(data).hexdigest()}{Colors.RESET}
  {Colors.DIM}SHA256:{Colors.RESET}  {Colors.WHITE}{hashlib.sha256(data).hexdigest()}{Colors.RESET}
  {Colors.DIM}SHA512:{Colors.RESET}  {Colors.WHITE}{hashlib.sha512(data).hexdigest()}{Colors.RESET}
    """)
    
    pause()

# ============================================
# 12. BASE64 TOOL
# ============================================
def base64_tool():
    clear()
    header()
    section("📝 BASE64 TOOL")
    
    print(f"  {Colors.DIM}1.  Encode{Colors.RESET}")
    print(f"  {Colors.DIM}2.  Decode{Colors.RESET}")
    
    choice = input(f"{Colors.CYAN}  Option: {Colors.RESET}")
    
    import base64
    
    if choice == "1":
        text = input(f"{Colors.CYAN}  Text: {Colors.RESET}")
        result = base64.b64encode(text.encode()).decode()
        print(f"\n  {Colors.GREEN}{result}{Colors.RESET}")
    elif choice == "2":
        text = input(f"{Colors.CYAN}  Base64: {Colors.RESET}")
        try:
            result = base64.b64decode(text).decode()
            print(f"\n  {Colors.GREEN}{result}{Colors.RESET}")
        except:
            status("Invalid base64", "error")
    else:
        status("Invalid", "error")
    
    pause()

# ============================================
# 13. SYSTEM RESOURCES
# ============================================
def system_resources():
    clear()
    header()
    section("📊 SYSTEM RESOURCES")
    
    status("Fetching...", "processing")
    
    cpu = subprocess.run("top -bn1 | grep 'Cpu(s)'", shell=True, capture_output=True, text=True).stdout.strip()
    mem = subprocess.run("free -h", shell=True, capture_output=True, text=True).stdout
    disk = subprocess.run("df -h /", shell=True, capture_output=True, text=True).stdout
    uptime = subprocess.run("uptime -p", shell=True, capture_output=True, text=True).stdout.strip()
    
    print(f"""
  {Colors.DIM}CPU:{Colors.RESET}     {Colors.WHITE}{cpu[:50]}{Colors.RESET}
  {Colors.DIM}Memory:{Colors.RESET}
  {Colors.DIM}  {mem.split('\\n')[1] if '\\n' in mem else mem}{Colors.RESET}
  {Colors.DIM}Disk:{Colors.RESET}
  {Colors.DIM}  {disk.split('\\n')[1] if '\\n' in disk else disk}{Colors.RESET}
  {Colors.DIM}Uptime:{Colors.RESET}  {Colors.WHITE}{uptime}{Colors.RESET}
    """)
    
    pause()

# ============================================
# 14. SECURITY REPORT
# ============================================
def security_report():
    clear()
    header()
    section("📊 SECURITY REPORT")
    
    status("Generating...", "processing")
    
    fw = subprocess.run("sudo ufw status", shell=True, capture_output=True, text=True).stdout
    fw_status = "Active" if "active" in fw.lower() else "Inactive"
    
    ssh = subprocess.run("systemctl status sshd", shell=True, capture_output=True, text=True).stdout
    ssh_status = "Running" if "active" in ssh.lower() else "Stopped"
    
    updates = subprocess.run("apt list --upgradable 2>/dev/null | wc -l", shell=True, capture_output=True, text=True)
    update_count = int(updates.stdout.strip()) - 1 if updates.stdout.strip().isdigit() else 0
    
    print(f"""
  {Colors.DIM}🛡️  Firewall:{Colors.RESET}   {Colors.WHITE}{fw_status}{Colors.RESET}
  {Colors.DIM}🔐  SSH:{Colors.RESET}        {Colors.WHITE}{ssh_status}{Colors.RESET}
  {Colors.DIM}📦  Updates:{Colors.RESET}    {Colors.WHITE}{update_count}{Colors.RESET}
  {Colors.DIM}🕐  Generated:{Colors.RESET}  {Colors.WHITE}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.RESET}
  {Colors.DIM}💻  Host:{Colors.RESET}       {Colors.WHITE}{socket.gethostname()}{Colors.RESET}
    """)
    
    pause()

# ============================================
# 15. IP INFO
# ============================================
def ip_info():
    clear()
    header()
    section("🌐 IP INFO")
    
    ip = input(f"{Colors.CYAN}  IP (or 'me'): {Colors.RESET}")
    
    if ip.lower() == 'me':
        try:
            ip = requests.get('https://api.ipify.org').text
        except:
            status("Failed", "error")
            pause()
            return
    
    try:
        resp = requests.get(f"http://ip-api.com/json/{ip}")
        data = resp.json()
        print(f"""
  {Colors.DIM}🌐  IP:{Colors.RESET}        {Colors.WHITE}{data.get('query', 'N/A')}{Colors.RESET}
  {Colors.DIM}📍  Country:{Colors.RESET}   {Colors.WHITE}{data.get('country', 'N/A')}{Colors.RESET}
  {Colors.DIM}🏙️  City:{Colors.RESET}      {Colors.WHITE}{data.get('city', 'N/A')}{Colors.RESET}
  {Colors.DIM}📟  ISP:{Colors.RESET}       {Colors.WHITE}{data.get('isp', 'N/A')}{Colors.RESET}
        """)
    except:
        status("Failed", "error")
    
    pause()

# ============================================
# 16. HTTP HEADERS
# ============================================
def http_headers():
    clear()
    header()
    section("🌐 HTTP HEADERS")
    
    url = input(f"{Colors.CYAN}  URL: {Colors.RESET}")
    
    if not url.startswith('http'):
        url = 'https://' + url
    
    try:
        resp = requests.get(url, timeout=10)
        print(f"\n  {Colors.DIM}Status:{Colors.RESET}  {Colors.WHITE}{resp.status_code}{Colors.RESET}")
        print(f"  {Colors.DIM}Size:{Colors.RESET}    {Colors.WHITE}{len(resp.content)} bytes{Colors.RESET}\n")
        for key, val in list(resp.headers.items())[:8]:
            print(f"  {Colors.DIM}{key}:{Colors.RESET}  {Colors.WHITE}{val[:50]}{Colors.RESET}")
    except:
        status("Failed", "error")
    
    pause()

# ============================================
# 17. RANDOM GENERATOR
# ============================================
def random_gen():
    clear()
    header()
    section("🎲 RANDOM GENERATOR")
    
    print(f"  {Colors.DIM}1.  Number{Colors.RESET}")
    print(f"  {Colors.DIM}2.  String{Colors.RESET}")
    print(f"  {Colors.DIM}3.  UUID{Colors.RESET}")
    print(f"  {Colors.DIM}4.  MAC{Colors.RESET}")
    
    choice = input(f"{Colors.CYAN}  Option: {Colors.RESET}")
    
    if choice == "1":
        mn = int(input(f"{Colors.CYAN}  Min: {Colors.RESET}"))
        mx = int(input(f"{Colors.CYAN}  Max: {Colors.RESET}"))
        print(f"\n  {Colors.GREEN}{random.randint(mn, mx)}{Colors.RESET}")
    elif choice == "2":
        n = int(input(f"{Colors.CYAN}  Length: {Colors.RESET}"))
        chars = string.ascii_letters + string.digits
        print(f"\n  {Colors.GREEN}{''.join(random.choice(chars) for _ in range(n))}{Colors.RESET}")
    elif choice == "3":
        print(f"\n  {Colors.GREEN}{uuid.uuid4()}{Colors.RESET}")
    elif choice == "4":
        mac = [0x00, 0x16, 0x3e, random.randint(0x00, 0x7f), random.randint(0x00, 0xff), random.randint(0x00, 0xff)]
        print(f"\n  {Colors.GREEN}{':'.join(f'{x:02x}' for x in mac)}{Colors.RESET}")
    else:
        status("Invalid", "error")
    
    pause()

# ============================================
# 18. COLOR DEMO
# ============================================
def color_demo():
    clear()
    header()
    section("🎨 COLOR DEMO")
    
    print(f"""
  {Colors.RED}RED{Colors.RESET}
  {Colors.GREEN}GREEN{Colors.RESET}
  {Colors.YELLOW}YELLOW{Colors.RESET}
  {Colors.BLUE}BLUE{Colors.RESET}
  {Colors.PURPLE}PURPLE{Colors.RESET}
  {Colors.CYAN}CYAN{Colors.RESET}
  {Colors.NEON}NEON{Colors.RESET}
  {Colors.GOLD}GOLD{Colors.RESET}
  {Colors.ORANGE}ORANGE{Colors.RESET}
  {Colors.NEON_PINK}PINK{Colors.RESET}
  {Colors.BOLD}BOLD{Colors.RESET}
  {Colors.DIM}DIM{Colors.RESET}
    """)
    
    pause()

# ============================================
# 19. HELP
# ============================================
def show_help():
    clear()
    header()
    section("📖 HELP — COMMAND REFERENCE")
    
    print(f"""
  {Colors.DIM}1.  Linux Hardening     —  Secure your Linux system{Colors.RESET}
  {Colors.DIM}2.  System Update       —  Update system packages{Colors.RESET}
  {Colors.DIM}3.  Breach Check        —  Check email in data breaches{Colors.RESET}
  {Colors.DIM}4.  File Analysis       —  Analyze suspicious files{Colors.RESET}
  {Colors.DIM}5.  Network Scanner     —  Scan network targets{Colors.RESET}
  {Colors.DIM}6.  Password Generator  —  Generate strong passwords{Colors.RESET}
  {Colors.DIM}7.  Whois Lookup        —  Get domain information{Colors.RESET}
  {Colors.DIM}8.  DNS Lookup          —  Lookup DNS records{Colors.RESET}
  {Colors.DIM}9.  Install Tools       —  Install security tools{Colors.RESET}
  {Colors.DIM}10. Port Scanner        —  Scan open ports{Colors.RESET}
  {Colors.DIM}11. Hash Generator      —  Generate file hashes{Colors.RESET}
  {Colors.DIM}12. Base64 Tool         —  Encode/Decode base64{Colors.RESET}
  {Colors.DIM}13. System Resources    —  Show system usage{Colors.RESET}
  {Colors.DIM}14. Security Report     —  Generate security report{Colors.RESET}
  {Colors.DIM}15. IP Info             —  Get IP information{Colors.RESET}
  {Colors.DIM}16. HTTP Headers        —  Check HTTP headers{Colors.RESET}
  {Colors.DIM}17. Random Generator    —  Generate random data{Colors.RESET}
  {Colors.DIM}18. Color Demo          —  Show available colors{Colors.RESET}
  {Colors.DIM}19. System Info         —  Show system details{Colors.RESET}
  {Colors.DIM}20. Exit                —  Close application{Colors.RESET}
    """)
    
    pause()

# ============================================
# EXIT
# ============================================
def exit_app():
    clear()
    print(f"""
{Colors.NEON}╔══════════════════════════════════════════════════════════════════════════╗
║                                                                                  ║
║   {Colors.BOLD}{Colors.WHITE}👋  Thank you for using Cybersecurity Suite!{Colors.RESET}{Colors.NEON}              ║
║   {Colors.YELLOW}🔒  Stay safe!  Stay secure!{Colors.RESET}{Colors.NEON}                                ║
║                                                                                  ║
║   {Colors.DIM}Created by {Colors.WHITE}{AUTHOR}{Colors.NEON}  |  {Colors.DIM}{YEAR}{Colors.NEON}                                       ║
║                                                                                  ║
╚══════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
    """)
    sys.exit(0)

# ============================================
# MAIN
# ============================================
def main():
    while True:
        clear()
        header()
        menu()
        
        choice = input(f"{Colors.CYAN}  Select option: {Colors.RESET}").strip()
        
        if choice == 'help':
            show_help()
            continue
        elif choice == 'clear':
            continue
        elif choice == '20':
            exit_app()
        
        actions = {
            "1": linux_harden,
            "2": system_update,
            "3": breach_check,
            "4": file_analysis,
            "5": network_scan,
            "6": password_gen,
            "7": whois_lookup,
            "8": dns_lookup,
            "9": install_tools,
            "10": port_scanner,
            "11": hash_gen,
            "12": base64_tool,
            "13": system_resources,
            "14": security_report,
            "15": ip_info,
            "16": http_headers,
            "17": random_gen,
            "18": color_demo,
            "19": system_info,
        }
        
        if choice in actions:
            actions[choice]()
        else:
            status("Invalid option. Type 'help' for commands.", "error")
            pause()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}  👋  Goodbye!{Colors.RESET}")
        sys.exit(0)
