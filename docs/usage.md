# Usage (TLDR)

Installing deluge-cmd will make the following available on your system:

## dls - deluge list

> **dls** (aka **deluge_dls.py**) lists objects such as Songs Samples, and SongSamples
> found on a Deluge Folder System (DFS).
> It's modelled after **[ls](https://tldr.ostera.io/ls)**.

- Print some help :

`dls --help`

- Print all the songs on a DFS: 

`dls ~/Music/DELUGE/02 songs`

- List songs where the path contains "002", "003" or "004" :

`dls songs ~/Music/DELUGE/02 songs -p *00[2-4]*`

- List samples where the path contains folder "/Kick/" :

`dls s ~/Music/DELUGE/02 **/Kick/*`

- List the song samples where the path contains folder "Artists" :

`dls song_samples ~/Music/DELUGE/02 **/Artists/*`

- Find the CR78 samples

`dls samples ~/Music/DELUGE/TEST/02 **/CR78*.wav`

```
Deluge filesystem at ~/Music/DELUGE/TEST/02 mounted: False
  Sample(path=PosixPath('~/Music/DELUGE/TEST/02/SAMPLES/DRUMS/Kick/CR78 Kick.wav'), settings=[])
  Sample(path=PosixPath('~/Music/DELUGE/TEST/02/SAMPLES/DRUMS/Rim/CR78 Rim.wav'), settings=[])
  ...
  Sample(path=PosixPath('~/Music/DELUGE/TEST/02/SAMPLES/DRUMS/HatC/CR78 Closed hihat.wav'), settings=[])
  Sample(path=PosixPath('~/Music/DELUGE/TEST/02/SAMPLES/DRUMS/ConH/CR78 Conga high.wav'), settings=[])
Deluge filesystem DelugeCardFS(card_root=PosixPath('~/Music/DELUGE/TEST/02')) has 14 samples 
```

## dmv  - deluge move

> **dmv** (aka **deluge_dmv.py**) moves Song Samples, and updates references in SONG XML files on
> a Deluge Folder System (DFS).
> It's loosely modelled after **[mv](https://tldr.ostera.io/mv)**.
>
> **Important** this is **experimental and possibly destructive!** Please backup your data first. 

- Print some help :

`dmv --help`

- Move your **CR78** samples, and update the songs that reference them : 

```
dmv ~/Music/DELUGE/TEST/02 **/CR78* SAMPLES/ANOTHER_PLACE -vs
```

```
~/Music/DELUGE/TEST/02/SONGS/SONG002A.XML update_song_xml
~/Music/DELUGE/TEST/02/SONGS/SONG002.XML update_song_xml
...
~/Music/DELUGE/TEST/02/SAMPLES/ANOTHER_PLACE/CR78 Closed hihat.wav move_file
~/Music/DELUGE/TEST/02/SAMPLES/ANOTHER_PLACE/CR78 Metal.wav move_file
moved 14 samples, in 9 songs
```

# Future

## dcp - deluge copy

Copy files and their references.

## drm - deluge remove

Remove files, cleaning up references.

# About TLDR

This page uses the [TLDR format](https://tldr.ostera.io/)