Configuring a DNS server using Linux

/// Prerequisites

// Bind9 (Open-source DNS software)

sudo apt install bind9 bind9-utils bind9-doc -y

// Net-tools (Useful network tools in Linux)

sudo apt install net-tools

// UFW (Uncomplicated Firewall)

sudo apt install ufw

///

First of all, I need to configure forwarders. This allows the DNS server to forward queries that it can't resolve to the assigned DNS server(s).
--- see named.conf.options

Configure a zone file for hqkim.com
--- see db.hqkim.com

Configure a reverse data file for hqkim.com
--- see db.172.18.68.rev

Configure forward/reverse zone file for hqkim.com
--- see named.conf.local

Restart BIND9 service, and check the status.

sudo systemctl restart bind9
sudo systemctl status bind9

Configure Firewall allow setting.

sudo ufw status
sudo ufw enable
sudo ufw allow bind9

Then, go to Windows Command Prompt to check if the IP address of 'www.hqkim.com' can be resolved by the domain server.

First I need to configure DNS server in Network setting to static IP address 172.18.68.64.


//Final Result
C:\Users\Username>nslookup www.hqkim.com
Server:  ns1.hqkim.com
Address:  172.18.68.64

Name:    www.hqkim.com
Address:  172.18.68.64
