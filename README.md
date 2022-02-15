# bgp-tools
BGP scripts &amp; tools to interact with API's.

## bgp-name-search.py
This script pulls down all the current AS Numbers and Names from ![bgpstuff.net](https://www.bgpstuff.net). It takes a single, case insensitive, argument and builds a regex expression and tries to match against the AS Name.

```
Usage:

python3 bgp-name-search.py [as_name]

```

