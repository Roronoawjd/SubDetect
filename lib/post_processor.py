def post_processor(subdomains):

    subdomain_list = set()

    for subdomain in subdomains:
        if "*" in subdomain:                    # asterisk delete
            pass
        elif "@" in subdomain:                  # email delete
            pass
        elif subdomain.startswith("www."):      # www.으로 시작할 시 www.뒤에 subdomain만 출력
            subdomain_list.add(subdomain[4:])
        else:
            subdomain_list.add(subdomain)

    return subdomain_list