🛰️ SatRecon: Satellite Risk Mapping via OSINT

A Python tool that uses the Shodan API to identify exposed satellite infrastructure (like VSATs, modems, uplinks) and generate a professional report in PDF and CSV format.

---

## 🔧 Features

- Searches Shodan for 10+ satellite-related keywords
- Extracts IP, country, organization, port, protocol, and banner info
- Exports data to:
  - 📁 `satellite_report.csv`
  - 📄 `satellite_osint_report.pdf`

---

## 🚀 How to Use

1. Clone This Repo
   git clone https://github.com/Forensonaut/SatRecon
   cd SatRecon

3. Install Dependencies
   
   pip install -r requirements.txt

4. Add Your API Key

   Open scanner.py and replace your Shodan Key:

   API_KEY = "YOUR_API_KEY"

5. Run the Tool

   python scanner.py
