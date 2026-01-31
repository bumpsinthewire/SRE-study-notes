---
title: "environment_profiles_and_templates"
date: "2026-01-26"
type: study_notes
tags: [study, linux]
---

# environment_profiles_and_templates

## Key Concepts

Environment variables store system settings

## Commands & Examples

`printenv` outputs all of the assigned system variables  
`echo $[variable]` will give you the output of a specific system variable

## Questions & Notes

edit the `.bashrc` file to change system settings for a user  
edit the `/etc/environment` file to change system settings for *ALL* users  
you must log out and back in to make changes to these settings take effect  
create custom commands to be run by creating files in the `/etc/profile.d/` directory  
use a custom file in `/etc/skel/` when you want to run something for every user

### Parent Note

- [Linux Study Journey](./README.md)
