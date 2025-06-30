import json
import csv

def write_report(results):
    with open("output/report.json", "w") as jf:
        json.dump(results, jf, indent=4)
    with open("output/report.csv", "w", newline="") as cf:
        writer = csv.DictWriter(cf, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
