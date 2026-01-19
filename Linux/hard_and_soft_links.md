---
title: "hard_and_soft_links"
date: "2026-01-13"
type: study_notes
tags: [study, linux]
---

# hard_and_soft_links

## Key Concepts

Hard links are essentially a filename that links to a specific inode (location in memory)
Soft links (also called sym links or symbolic links) allow you to point to another file (kind of like a shortcut)

## Commands & Examples

`ln [path_to_target_file] [path_to_link_file]`
    `-s` is used for sym/soft links

## Questions & Notes

Hard links allow you to store a file one time, but have multiple pointers to that inode
    If someone deletes their hard link, the rest of the links still have access to the data
    If all links to an inode are deleted, the data will be deleted as well
    Hard links can only be used for files, not folders and can only be linked to files on the same filesystem
Soft links can be used to point to other filesystems and to directories

### Parent Note

- [Linux Study Journey](./README.md)
