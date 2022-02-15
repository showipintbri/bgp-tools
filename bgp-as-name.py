import bgpstuff
import argparse


def main(asn):

    c = bgpstuff.Client()

    c.get_as_name(asn)

    if c.status_code == 200 and c.exists:
        print(c.as_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Lookup ASN Name by ASN Number.')
    parser.add_argument('asn_num', metavar='ASN', type=int, help='The ASN Number you want to lookup.')
    args = parser.parse_args()
    asn = args.asn_num
    main(asn)
