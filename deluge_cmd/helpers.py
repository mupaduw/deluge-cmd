"""Helper functions module."""
# flake8: noqa


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
