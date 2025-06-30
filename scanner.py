import shodan
from geo_mapper import generate_map
from cve_checker import check_vulns
from cert_parser import extract_cert_info
from passive_dns import get_passive_dns
from risk_score import assign_risk_score
from report_writer import write_report

API_KEY = "YOUR_SHODAN_API_KEY"  # Replace this with your actual key
KEYWORDS = ["vsat", "satellite uplink", "iDirect", "norsat", "comtech"]

api = shodan.Shodan(API_KEY)
all_results = []

for keyword in KEYWORDS:
    try:
        print(f"🔍 Scanning for: {keyword}")
        results = api.search(keyword)
        for device in results['matches']:
            ip = device['ip_str']
            org = device.get('org', 'N/A')
            location = device.get('location', {}).get('country_name', 'Unknown')
            ports = device.get('port', [])
            vulns = check_vulns(device)
            cert = extract_cert_info(device)
            dns = get_passive_dns(ip)
            score = assign_risk_score(device)
            
            device_info = {
                'IP': ip,
                'Org': org,
                'Location': location,
                'Vulnerabilities': vulns,
                'CertInfo': cert,
                'PassiveDNS': dns,
                'RiskScore': score
            }
            all_results.append(device_info)
    except Exception as e:
        print(f"❌ Error scanning {keyword}: {e}")

write_report(all_results)
generate_map(all_results)
