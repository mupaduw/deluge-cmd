"""Main dmv script."""

import argparse
import itertools
from pathlib import Path

from deluge_card import list_deluge_fs
from deluge_card.deluge_sample import mv_samples, validate_mv_dest


def main():
    """Main entrypoint."""
    parser = argparse.ArgumentParser(description='deluge_dmv.py (dmv)  - move deluge FS sample contents.')

    parser.add_argument('root', help='root folder, must be a valid Deluge file system.')
    parser.add_argument('pattern', help='glob pattern to match e.g. **/Clap*.wav')
    parser.add_argument('dest', help='target folder or file, which must be in a subfolder of root.')

    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument("-s", "--summary", help="summarise output", action="store_true")
    parser.add_argument('-D', '--debug', action="store_true", help="print debug statements")

    args = parser.parse_args()
    if args.debug:
        print(f"Args: {args}")

    card_imgs = list(list_deluge_fs(args.root))
    if len(card_imgs) == 0:
        print('No card found.')
        return
    if len(card_imgs) > 1:
        print("Oops multiple cards found, only a single card mv is supported.")
        return

    card = card_imgs[0]
    try:
        validate_mv_dest(card.card_root, Path(args.dest))
        song_samples = itertools.chain.from_iterable(map(lambda song: song.samples(), card.songs()))
        new_path = Path(args.dest)
    except ValueError as err:
        print(err)
        return

    counters = dict(move_file=0, update_song_xml=0)
    for modop in mv_samples(card.card_root, song_samples, args.pattern, new_path):
        counters[modop.operation] += 1
        if args.verbose:
            print(f"{str(modop.path)} {modop.operation.replace('_', ' ')}")

    if args.summary | args.verbose:
        print(f'moved {counters["move_file"]} samples, in {counters["update_song_xml"]} songs')


if __name__ == '__main__':
    main()  # pragma: no cover
