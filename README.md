# bgp-tools
BGP scripts &amp; tools to interact with API's.

## bgp-name-search.py
This script pulls down all the current AS Numbers and Names from ![bgpstuff.net](https://www.bgpstuff.net). It takes a single, case insensitive, argument and builds a regex expression and tries to match against the AS Name.

**REQUIRED:** `python3 -m pip install bgpstuff`
```
Usage:

python3 bgp-name-search.py [as_name]


user@host:~$ python3 bgp-name-search.py apple
714 = APPLE-ENGINEERING
6185 = APPLE-AUSTIN
11046 = LITTLE-APPLE
14009 = APPLESEEDS
54506 = STAYPINEAPPLE
63707 = APPLE-CN Apple Computer Trading Shanghai Co. Ltd.
135855 = APPLESTL-AS-IN Applesoft Technologies
136581 = APPLEWEA-CSLOX-AS-AP Apple Wealth Securities
136716 = APPLEBB-AS APPLE BROADBAND SERVICES PVT. LTD
138575 = APPLE2-AS-AP APPLE NET
139901 = APPLE1-AS-AP Apple Communication Ltd.
142567 = MYISPPTYLTD-AS-AP ISP Pineapple Net
208629 = GOLDAPPLE
396918 = APPLE-BANK-FOR-SAVINGS
396959 = APPLE-BANK-FOR-SAVINGS
```

