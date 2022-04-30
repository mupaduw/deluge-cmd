"""
Main cmd list deluge_card contents of folder(s) specified.
"""
import argparse

from deluge_card import list_deluge_fs

from deluge_cmd.deluge_cmd import list_samples, list_song_samples, list_songs

if __name__ == '__main__':
    # print('dc_manifest')
    parser = argparse.ArgumentParser(description='list deluge_card contents')
    parser.add_argument('folder', type=str, nargs='+', help='one or more folder to check')
    parser.add_argument(
        '-l', '--list', help='one of of s=songs, a=samples, S=song_samples (future: K=Kit, I=instrument)'
    )
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument("-s", "--summary", help="summarise output", action="store_true")

    args = parser.parse_args()

    for fname in args.folder:
        card_imgs = list_deluge_fs(fname)
        if len(card_imgs):
            for c in card_imgs:
                print(f'Deluge filesystem at {c.card_root()} mounted: {c.is_mounted()}')
                if args.list == 's':
                    list_songs(c, args)
                if args.list == 'a':
                    list_samples(c, args)
                if args.list == 'S':
                    list_song_samples(c, args)
