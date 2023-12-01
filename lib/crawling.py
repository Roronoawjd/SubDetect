from bs4 import BeautifulSoup
from lib.requester import requester
from lib.post_processor import post_processor
from lib.subdomain_printer import subdomain_printer

def crawling(domain, silent):
    crt_sh_url = f"https://crt.sh/?q={domain}"

    response = requester(crt_sh_url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.select('.outer')
        table_td = table[3].select('table tr td:nth-child(6)')

        subdomain_list = []

        for subdomain in table_td:
            subdomain_list += subdomain.get_text(separator=" ").split()
        
        subdomain_list = post_processor(set(subdomain_list))
        subdomain_printer(subdomain_list, silent)

    else:
        print(f"error: {response.status_code}")
        