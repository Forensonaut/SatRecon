def assign_risk_score(device):
    base = 50
    if "vulns" in device:
        base += 20
    if "ssl" in device:
        base += 10
    if device.get("port") == 22:
        base += 5
    return min(base, 100)
