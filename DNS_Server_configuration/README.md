# Configuring a DNS server using Linux

I have configured a Domain Name Server in my Ubuntu Linux and created zone files to resolve hqkim.com (a fake website).

## Prerequisites

* [Bind9](#bind-9-installation) - Open-source DNS software

* [Net-tools](#net-tools-installation) - A suite of network tools that can be useful in Linux

* [UFW](#ufw-installation) - Uncomplicated Firewall

---

## Installation

### Bind-9 Installation
  `sudo apt install bind9 bind9-utils bind9-doc -y`

*Bind 9* is an open source DNS suite that users can download and use for free.

### Net-tools Installation
  `sudo apt install net-tools`

*Net-tools' contains useful tools such as nslookup that can help to test DNS resolution.
  
### UFW Installation
  `sudo apt install ufw`

*UFW* is used to simplify firewall rules in Debian-based Linux.

---

## DNS Records

### DNS Forwarder
First of all, I need to configure forwarders. This allows the DNS server to forward queries that it can't resolve to the assigned DNS server(s).

Forwarders : [name.conf.option](https://github.com/Hyunkyu-Kim-Q/projects/blob/main/DNS_Server_configuration/named.conf.options)

```
options {
    directory "/var/cache/bind";

    // Uncomment the forwarders block if you want to use external DNS servers
    forwarders {
        8.8.8.8;
        1.1.1.1;
    };

    dnssec-validation auto;

    listen-on-v6 { any; };
};
```

### Domain Zone file
Then, I created a zone file that contains A record, NS record, MX record and CNAME record.

Zone file : [db.hqkim.com](https://github.com/Hyunkyu-Kim-Q/projects/blob/main/DNS_Server_configuration/db.hqkim.com)

```
; base zone file for hqkim.com
$TTL 86400 ; default TTL for zone (1 day)
$ORIGIN hqkim.com. ; base domain-name

; Start of Authority RR defining the key characteristics of the zone (domain)
@         IN      SOA   ns1.hqkim.com. admin.hqkim.com. (
                                 2025032300 ; serial number (yyyymmddnn, best practice)
                                 43200      ; refresh (12 hours)
                                 900        ; retry (15 minutes)
                                 345600     ; expiry (4 days)
                                 7200       ; minimum TTL (2 hours)
                                 )

; Name server RR for the domain
@         IN      NS      ns1.hqkim.com.

; Mail server RRs for the zone (domain)
@         IN      MX  10  mail.hqkim.com.

; Domain hosts include NS and MX records defined above
ns1       IN      A       172.18.68.64
mail      IN      A       172.18.68.64
admin     IN      A       172.18.68.64
www       IN      A       172.18.68.64

; Aliases (CNAME) for the domain
ftp       IN      CNAME   ftp.hqkim.net.
```

### Reverse Data File
I also wanted to enable reverse DNS lookup, so I created a reverse data file.

Reverse data file : [db.172.18.68](https://github.com/Hyunkyu-Kim-Q/projects/blob/main/DNS_Server_configuration/db.172.18.68)

```
;
; BIND reverse data file for hqkim.com
;
$TTL 1D
@        IN        SOA  ns1.hqkim.com. admin.hqkim.com. (
                        2025032301 ; serial
                        30800      ; refresh
                        7200       ; retry
                        604800     ; expire
                        300 )      ; minimum
;
@        IN        NS    ns1.hqkim.com.
64       IN        PTR   ns1.hqkim.com.
```

### Forward/Reverse mapping Zone File
Mapping zone file contains the mappings between Domain name and IP address.

Mapping zone file : [named.conf.local](https://github.com/Hyunkyu-Kim-Q/projects/blob/main/DNS_Server_configuration/named.conf.local)

```
// Provide forward mapping zone for hqkim.com

zone "hqkim.com" {
  type master;
  file "/etc/bind/db.hqkim.com";
};

// Provide reverse mapping zone for the hqkim.com
// address 68.18.172.in-addr.arpa

zone "68.18.172.in-addr.arpa" {
  type master;
  file "/etc/bind/db.172.18.68";
};
```

---

# Testing

Restart BIND9 service and check the status.

```
sudo systemctl restart bind9
sudo systemctl status bind9
```

Using UFW, allow bind 9 to access.
```
sudo ufw status
sudo ufw enable
sudo ufw allow bind9
```

Change the primary DNS server to static IP address 172.18.68.64.

```PS
Get-NetAdapter
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses "172.18.68.64"
```

## Result

```
C:\Users\Username>nslookup www.hqkim.com

Server:  ns1.hqkim.com
Address:  172.18.68.64

Name:    www.hqkim.com
Address:  172.18.68.64
```
