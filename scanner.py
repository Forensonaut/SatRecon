import shodan
import csv
from fpdf import FPDF

API_KEY = "YOUR_API_KEY"  

satellite_keywords = [
    "vsat", "norsat", "iDirect", "comtech", "satellite uplink",
    "satellite modem", "ground station", "teleport uplink",
    "LNB", "DVB-S2", "satellite earth station"
]

api = shodan.Shodan(API_KEY)
output_data = []

for keyword in satellite_keywords:
    print(f"\n🔍 Searching: {keyword}")
    try:
        results = api.search(keyword)
        print(f"📊 Total found: {results['total']}")
        for result in results['matches'][:5]:
            ip = result['ip_str']
            country = result.get('location', {}).get('country_name', 'N/A')
            org = result.get('org', 'N/A')
            port = result.get('port', 'N/A')
            protocol = result.get('transport', 'N/A')
            data = result.get('data', '')[:100].replace('\n', ' ').replace('\r', '')

            print(f"🛰️ IP: {ip}, 🌍 Country: {country}, 🏢 Org: {org}")
            output_data.append([keyword, ip, country, org, port, protocol, data])
    except shodan.APIError as e:
        print(f"❌ Error: {e}")


with open("satellite_report.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Keyword", "IP", "Country", "Org", "Port", "Protocol", "Banner Snippet"])
    writer.writerows(output_data)


pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="SatRecon: Satellite Risk Mapping via OSINT", ln=True, align='C')
pdf.ln(10)

for row in output_data:
    keyword, ip, country, org, port, protocol, data = row
    pdf.multi_cell(0, 10, txt=(
        f"🔍 Keyword: {keyword}\n"
        f"🛰️ IP: {ip}\n"
        f"🌍 Country: {country}\n"
        f"🏢 Org: {org}\n"
        f"🔌 Port: {port}\n"
        f"📡 Protocol: {protocol}\n"
        f"🧾 Snippet: {data}\n"
        f"{'-'*40}"
    ))

pdf.output("satellite_osint_report.pdf")
print("\n✅ Reports generated: satellite_report.csv and satellite_osint_report.pdf")
