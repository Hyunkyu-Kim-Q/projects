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
