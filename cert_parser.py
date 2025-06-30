def extract_cert_info(device):
    cert = device.get('ssl', {}).get('cert', {})
    return cert.get('issuer', {})
