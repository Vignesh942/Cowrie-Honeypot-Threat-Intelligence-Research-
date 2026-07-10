import requests

BASE_URL = "http://ip-api.com/json/"


def lookup_ip(ip):
    """
    Returns country, city, ISP and ASN for an IP address.
    """

    try:
        response = requests.get(
            f"{BASE_URL}{ip}",
            timeout=5,
            params={"fields": "status,country,city,isp,as"}
        )

        data = response.json()

        if data.get("status") == "success":
            return {
                "country": data.get("country", "Unknown"),
                "city": data.get("city", "Unknown"),
                "isp": data.get("isp", "Unknown"),
                "asn": data.get("as", "Unknown")
            }

    except Exception:
        pass

    return {
        "country": "Unknown",
        "city": "Unknown",
        "isp": "Unknown",
        "asn": "Unknown"
    }