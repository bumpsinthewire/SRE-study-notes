---
title: "archive_backup_compress"
date: "2026-01-14"
type: study_notes
tags: [study, linux]
---

# archive_backup_compress

## Key Concepts

Archiving is packing a bunch of files/directories in a single location
Backup is just moving the file to a place for safe keeping
Compressing makes the file smaller

## Commands & Examples

`tar (options) [name_of_archive] [file_to_be_archived]` is used for archiving (tape archive). sometimes called a tarball
    `-t` used to list (make it make sense)
    `-f` file (should be the last option because `tar` expects the filename right after it)
    `-c` create
    `-r` append (I know right)
    `-x` extract to current directory
        `-C` extract to a target directory
        `tar xf archive.tar -C /tmp/` extract "archive.tar" to the /tmp/ directory
    `tar` can also be used with just the options and no "-"
    `tar` also has flags for each compression utility
        `-z` for `gzip`
        `-j` for `bzip2`
        `-J` for `xz`
        `-a` to let the system automatically pick a compression utility based on the filename extension

Compression utilities:
`gzip/bzip2/xz filename` files end in .gz/.bz2/.xz respectively
    `-k` keep original file
    `-d` to decompress
    `-l` list contents

Backup usually just involves copying
`rsync [from_location] [to_location]` this can be used locally but also between machines
    `-a` for archiving the file as well

## Questions & Notes

`zip` is another utility that is sometimes installed and does both archiving and compression
`dd` is mostly used for disk imaging but has a bit more complicated syntax
    DO NOT run this on a VM as it will overwrite it

### Parent Note

- [Linux Study Journey](./README.md)
