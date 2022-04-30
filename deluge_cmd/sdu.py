#!dc_manifest
"""
list deluge_card contents of folder(s) specified
"""
import argparse
from deluge_card import DelugeCardFS
from deluge_card.deluge_card import InvalidDelugeCard, list_deluge_fs

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

if __name__ == '__main__':
	#print('dc_manifest')
	parser = argparse.ArgumentParser(description='list deluge_card contents')
	parser.add_argument('folder', type=str, nargs='+',
	                    help='one or more folder to check')
	parser.add_argument('-l', '--list',
	                    help='one of of s=songs, a=samples, S=song_samples (future: K=Kit, I=instrument)')
	parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")	
	parser.add_argument("-s", "--summary", help="summarise output",
                    action="store_true")	

	args = parser.parse_args()
	
	for fname in args.folder:
		card_imgs = list_deluge_fs(fname)
		if len(card_imgs):
			for c in card_imgs:
				print(f'Deluge filesystem at {c.card_root()} mounted: {c.is_mounted()}')
				if args.list == 's':
					list_songs(c, args)
				if args.list ==  'a':
					list_samples(c, args)
				if args.list == 'S':
					list_song_samples(c, args)
