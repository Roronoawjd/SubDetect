def subdomain_printer(subdomains, silent):
    for subdomain in subdomains:
        print(subdomain)
    
    if not silent:
        print(f"\n[INFO] Found {len(subdomains)} subdomains")