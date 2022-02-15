import bgpstuff
import argparse
import re

def main(asn_name):

    c = bgpstuff.Client()
    c.get_as_names()
    all_names = c.all_as_names
    string = '.*' + asn_name + '.*'
    apple = re.compile(string, re.IGNORECASE)

    for i in sorted(all_names):
        name = all_names[i]
        try:
            m = apple.match(name)
            if m != None:
                result = str(m.group())
                print(f"{i} = {result}")
        except:
            pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Lookup ASN Number by ASN Name Contains.')
    parser.add_argument('asn_name', metavar='ASN_NAME', type=str, help='The string you want contained in the ASN Name.')
    args = parser.parse_args()
    asn_name = args.asn_name
    main(asn_name)
