# Usage

Installing deluge-cmd will make the following available on your system:

## dls

> **dls** (also **deluge_ls**) lists objects such as Songs Samples, and SongSamples
> found on a Deluge Folder System (DFS).
> It's modelled after **[ls](https://tldr.ostera.io/ls)** (or **dir**).

- Print all the songs on a DFS: 

`dls ~/Music/DELUGE/02 songs`

- List songs where the path contains "002", "003" or "004" :

`dls ~/Music/DELUGE/02 songs -p *00[2-4]*`

- List samples where the path contains folder "/Kick/" :

`dls ~/Music/DELUGE/02 samples -p **/Kick/**`

- List the song samples where the path contains folder "Artists" :

`dls ~/Music/DELUGE/02 song_samples -p **/Artists/**`

## future

### dmkfs

### dcp

### dmv

### drm


# About TLDR

This page uses the [TLDR format](https://tldr.ostera.io/)