"""Helper functions module."""
# flake8: noqa


def list_songs(card, args):
    songs = list(card.songs())
    if args.summary | args.verbose:
        print(f'Deluge filesystem {card} has {len(songs)} songs')
    if args.summary:
        return
    for s in songs:
        print(f'  {s} key {s.scale()} tempo {s.tempo()}')


def list_samples(card, args):
    all_samples = list(card.samples())
    if args.summary | args.verbose:
        print(f'Deluge filesystem {card} has {len(all_samples)} samples')
    if args.summary:
        return
    for sa in all_samples:
        print(f'  {sa}')


def list_song_samples(card, args):
    song_samples = list(card.songs())
    for s in song_samples:
        if args.summary | args.verbose:
            print(f'{s} has {len(list(s.samples()))} samples')
        if args.summary:
            continue
        for sa in s.samples():
            print(f'  {str(sa)} => {sa.settings()}')
