from loaders import ConfluenceLoader
from printers import print, prompt
from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--no-verify', action='store_true')
    return parser.parse_args()


def main():
    args = parse_args()

    if args.no_verify:
        print('WARNING: SSL certificate verification is turned off.', style='warn')
        import urllib3
        urllib3.disable_warnings()

    print('Confluence to Bookstack Migrator', style='questionmark')
    url = prompt('Enter the URL of your Confluence site: ')
    pat = prompt('Enter the personal access token: ', is_password=True)

    confluence_loader = ConfluenceLoader(url, pat, verify=not args.no_verify)
    confluence_loader.load()

if __name__ == '__main__':
    main()
