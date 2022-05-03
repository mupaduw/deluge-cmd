"""Main dsd script."""

import argparse

from deluge_card import list_deluge_fs
from helpers import list_samples, list_song_samples, list_songs


def main():
    """Main entrypoint."""
    parser = argparse.ArgumentParser(description='deluge_dls.py (dls)  - list deluge FS contents')

    parser.add_argument('root', help='root folder to begin ls from')
    parser.add_argument('type', help='one of of s=songs, a=samples, ss=song_samples (future: k=kits, i=instruments)')
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument("-s", "--summary", help="summarise output", action="store_true")
    parser.add_argument('-p', '--pattern', help='pattern')
    parser.add_argument('-D', '--debug', action="store_true", help="print debug statements")

    args = parser.parse_args()

    if args.debug:
        print(f"Args: {args}")

    card_imgs = list_deluge_fs(args.root)
    if len(card_imgs):
        for c in card_imgs:
            print(f'Deluge filesystem at {c.card_root()} mounted: {c.is_mounted()}')
            if args.type.lower() in ['s', 'songs']:
                list_songs(c, args)
            if args.type.lower() in ['a', 'samples']:
                list_samples(c, args)
            if args.type.lower() in ['ss', 'song_samples']:
                list_song_samples(c, args)


if __name__ == '__main__':
    main()  # pragma: no cover
