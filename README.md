🛰️ SatReconX — Satellite OSINT Recon Scanner

SatReconX is an advanced Open Source Intelligence (OSINT) tool designed to scan, assess, and report vulnerabilities in publicly exposed satellite communication infrastructure.

---

## 🔍 Features

- Shodan-based scanning for satellite-related devices
- CVE vulnerability extraction
- SSL certificate analysis
- Risk scoring of targets
- Passive DNS linking
- Interactive map visualization (using Folium)
- JSON + CSV reports

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
