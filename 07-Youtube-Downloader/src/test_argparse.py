import argparse

def main():
    pass


if __name__ == '__main__':

    # we have an object (parser) from argparse
    parser = argparse.ArgumentParser(
        description='YouTube Downloader'
    )

    # Add argument one by one
    parser.add_argument('-u', '--url', help='YouTube video URL')
    parser.add_argument(
        '-q', '--quality', help='Video quality', default='highest'
    )
    parser.add_argument('-d', '--delay', help='Delay between downloads', type=int, default=0)
    parser.add_argument('-ul', '--url_list', help='List of URLs', nargs='+')

    """  +: means at least 1 argument or more
    * : means at least 0 argument or more
    """ 

    args = parser.parse_args()
    print(args)

    # print(args.url)
    # print(args.delay)


                