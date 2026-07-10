from collections import Counter
from geo_lookup import lookup_ip


def generate_report(events):
    unique_ips = set()

    usernames = Counter()
    passwords = Counter()
    commands = Counter()

    total_connections = 0
    successful_logins = 0

    for event in events:

        event_type = event.get("eventid")

        if "src_ip" in event:
            unique_ips.add(event["src_ip"])

        if event_type == "cowrie.session.connect":
            total_connections += 1

        elif event_type == "cowrie.login.success":
            successful_logins += 1
            usernames[event.get("username", "Unknown")] += 1
            passwords[event.get("password", "Unknown")] += 1

        elif event_type == "cowrie.command.input":
            commands[event.get("input", "")] += 1

    print("=" * 50)
    print("Cowrie Honeypot Threat Report")
    print("=" * 50)

    print(f"Total Events          : {len(events)}")
    print(f"Connections           : {total_connections}")
    print(f"Successful Logins     : {successful_logins}")
    print(f"Unique Attacker IPs   : {len(unique_ips)}")

    print("\nAttacker IP Details")
    print("-" * 60)

    for ip in sorted(unique_ips):

        info = lookup_ip(ip)

        print(f"\nIP      : {ip}")
        print(f"Country : {info['country']}")
        print(f"City    : {info['city']}")
        print(f"ISP     : {info['isp']}")
        print(f"ASN     : {info['asn']}")

    print("\nTop Usernames")
    print("-" * 25)

    for user, count in usernames.most_common(5):
        print(f"{user:<15} {count}")

    print("\nTop Passwords")
    print("-" * 25)

    for pwd, count in passwords.most_common(5):
        print(f"{pwd:<15} {count}")

    print("\nTop Commands")
    print("-" * 25)

    for cmd, count in commands.most_common(10):
        print(f"{cmd:<20} {count}")