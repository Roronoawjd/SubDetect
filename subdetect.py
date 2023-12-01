import time
import argparse
from lib.crawling import crawling

# 인자 값 추가
parser = argparse.ArgumentParser(description='subdomain discovery tool')
parser.add_argument('-d', '--domain', required=True, help='input domain ex) naver.com, codeengn.com', dest='domain')
parser.add_argument('-silent', action='store_true', help='show only subdomains in output', dest='silent')

args = parser.parse_args()

domain = args.domain
silent = args.silent

logo = """
             _          _        _                _   
            | |        | |      | |              | |  
 ___  _   _ | |__    __| |  ___ | |_   ___   ___ | |_ 
/ __|| | | || '_ \  / _` | / _ \| __| / _ \ / __|| __|
\__ \| |_| || |_) || (_| ||  __/| |_ |  __/| (__ | |_ 
|___/ \__,_||_.__/  \__,_| \___| \__| \___| \___| \__|

                                        by Roronoawjd
"""
if not silent:
    print(logo)
    print(f"[INFO] Detecting subdomains of {domain}\n")


start = time.time()
crawling(domain, silent)
end = time.time()

if not silent:
    print(f"[INFO] Total Time: {end - start:.5f} sec")
