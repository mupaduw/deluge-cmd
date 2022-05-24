"""Main dsd script."""
# flake8: noqa
import argparse

from deluge_card import list_deluge_fs


def list_songs(card, args):
    songs = list(card.songs(args.pattern))
    if args.summary | args.verbose:
        print(f'{len(songs)} songs  matched "{args.pattern}" on {card.card_root}')
    if args.summary:
        return
    for s in songs:
        print(f'{s} key {s.scale()} tempo {s.tempo()}')


def list_samples(card, args):
    if args.type in ['a', 'samples']:
        samples = list(card.samples(args.pattern))
    else:
        samples = list(card.used_samples(args.pattern))

    if args.summary | args.verbose:
        print(f'{len(samples)} samples matched "{args.pattern}" on {card.card_root}')
    if args.summary:
        return
    for sa in samples:
        detail = f'{sa.path.relative_to(card.card_root)}'
        if (args.type in ['u', 'used_samples']) & args.verbose:
            detail += f' => {[str(ss.xml_file.path.relative_to(card.card_root)) for ss in sa.settings]}'
        print(detail)


def parse_args():
    parser = argparse.ArgumentParser(description='deluge_dls.py (dls)  - list deluge FS contents')
    parser.add_argument('type', help='one of of s=songs, a=all_samples, u=used_samples(future: k=kits, i=instruments)')
    parser.add_argument('root', help='root folder to begin ls from')
    parser.add_argument('pattern', help='pattern')
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument("-vv", "--more-verbose", help="increase output verbosity even more", action="store_true")
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
            # print(f'Deluge Folder System at {c.card_root} {"is" if c.is_mounted() else "is not"} mounted.')
            if args.type.lower() in ['s', 'songs']:
                list_songs(c, args)
            if args.type.lower() in ['a', 'samples', 'u', 'used_samples']:
                list_samples(c, args)


def main():
    handle_args(parse_args())


if __name__ == '__main__':
    main()  # pragma: no cover
