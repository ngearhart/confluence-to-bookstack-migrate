from loaders import ConfluenceLoader
from printers import print, prompt


def main():
    print('Confluence to Bookstack Migrator', style='questionmark')
    url = prompt('Enter the URL of your Confluence site: ')
    pat = prompt('Enter the personal access token: ', is_password=True)

    confluence_loader = ConfluenceLoader(url, pat)
    confluence_loader.load()

if __name__ == '__main__':
    main()
