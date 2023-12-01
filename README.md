<div align="center">
  <h1>SubDetect</h1>
</div>
<h3 align="center">The SubDetect tool is used for detecting subdomains.</h3>

## Usage

`python subdetect.py -h`</br>

```
usage: subdetect.py [-h] -d DOMAIN [-silent]

subdomain discovery tool

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        input domain ex) naver.com, codeengn.com
  -silent               show only subdomains in output
```

`python subdetect.py -d [domain]`

```
python subdetect.py -d hackerone.com

             _          _        _                _
            | |        | |      | |              | |
 ___  _   _ | |__    __| |  ___ | |_   ___   ___ | |_
/ __|| | | || '_ \  / _` | / _ \| __| / _ \ / __|| __|
\__ \| |_| || |_) || (_| ||  __/| |_ |  __/| (__ | |_
|___/ \__,_||_.__/  \__,_| \___| \__| \___| \___| \__|

                                        by Roronoawjd

[INFO] Detecting subdomains of hackerone.com

gslink.hackerone.com
go.hackerone.com
mta-sts.hackerone.com
links.hackerone.com
info.hackerone.com
mta-sts.forwarding.hackerone.com
api.hackerone.com
docs.hackerone.com
events.hackerone.com
mta-sts.managed.hackerone.com
hackerone.com
support.hackerone.com
design.hackerone.com

[INFO] Found 13 subdomains
[INFO] Total Time: 1.65222 sec
```

`python subdetect.py -d [domain] -silent`

```
python subdetect.py -d hackerone.com -silent
mta-sts.forwarding.hackerone.com
mta-sts.managed.hackerone.com
links.hackerone.com
go.hackerone.com
mta-sts.hackerone.com
docs.hackerone.com
events.hackerone.com
info.hackerone.com
api.hackerone.com
support.hackerone.com
design.hackerone.com
gslink.hackerone.com
hackerone.com
```
