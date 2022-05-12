"""Main dsd script."""
# flake8: noqa
import argparse

from deluge_card import list_deluge_fs


def list_songs(card, args):
    songs = list(card.songs(args.pattern))
    if args.summary | args.verbose:
        print(f'Deluge filesystem {card} has {len(songs)} songs')
    if args.summary:
        return
    for s in songs:
        print(f'  {s} key {s.scale()} tempo {s.tempo()}')


def list_samples(card, args):
    samples = list(card.samples(args.pattern))
    if args.summary | args.verbose:
        print(f'Deluge filesystem {card} has {len(samples)} samples')
    if args.summary:
        return
    for sa in samples:
        print(f'  {sa}')


def list_song_samples(card, args):
    songs = list(card.songs())
    for s in songs:
        if args.summary | args.verbose:
            print(f'{s} has {len(list(s.samples(args.pattern)))} samples')
        if args.summary:
            continue
        for sa in s.samples(args.pattern):
            print(f'  {s} {str(sa)}')


def parse_args():
    parser = argparse.ArgumentParser(description='deluge_dls.py (dls)  - list deluge FS contents')
    parser.add_argument('type', help='one of of s=songs, a=samples, ss=song_samples (future: k=kits, i=instruments)')
    parser.add_argument('root', help='root folder to begin ls from')
    parser.add_argument('pattern', help='pattern')
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument("-s", "--summary", help="summarise output", action="store_true")
    parser.add_argument('-D', '--debug', action="store_true", help="print debug statements")
    args = parser.parse_args()
    return args


def handle_args(args):
    if args.debug:
        print(f"Args: {args}")

    card_imgs = list(list_deluge_fs(args.root))
    if len(card_imgs):
        for c in card_imgs:
            print(f'Deluge filesystem at {c.card_root} mounted: {c.is_mounted()}')
            if args.type.lower() in ['s', 'songs']:
                list_songs(c, args)
            if args.type.lower() in ['a', 'samples']:
                list_samples(c, args)
            if args.type.lower() in ['ss', 'song_samples']:
                list_song_samples(c, args)


def main():
    handle_args(parse_args())


if __name__ == '__main__':
    main()  # pragma: no cover
