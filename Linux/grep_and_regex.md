---
title: "grep_and_regex"
date: "2026-01-14"
type: study_notes
tags: [study, linux]
---

# grep_and_regex

## Key Concepts

Grep lets you search within a file for specific patterns  
Regex is like reciting magical incantations that let you search for more specific and unique patterns

## Commands & Examples

`grep 'password' [directory/filename]` searches for lines containing the pattern "password" in a certain location  
`-i` to ignore case  
`-r` to search recursively  
`-v` matches lines that do not contain the pattern  
`-w` matches the exact word (the results here can be a bit unexpected because it will only match certain ways of containing the word in a line)  
it will mostly just match the word exactly with no leading or trailing letters, but some punctiation will also match (like -)

Regex spells (put them in your pattern):  
`^` the line begins with (put at the beginning of the pattern)  
`grep '^test' [directory/filename]` matches any line beginning with "test"

`$` the line ends with (put at the end of the pattern)  
`grep 'test$' [directory/filename]` matches any line ending in "test"

`.` match any ONE character (can use this like a wildcard so put it where you want it to match)  
`grep 't.st' [directory/filename]` matches "t[a-z]st"

`\` for escaping special characters so you can search for them  
`grep '\.' [directory/filename]` matches anything with a period

`*` match the previous element 0 or more times  
`grep 'ok*' [directory/filename]` matches "ok" (with any number of k's, including none at all and returning just "o")

`+` match the previous element 1 or more times  
`grep 'ok+' [directory/filename]` matches "ok" (starting with at least "ok" followed by zero or more "k's")

Extended regex allows you to bypass having to use the escape character (\) for regex symbols  
you simply add the `-E` option to `grep` or use the `egrep` command

`{min,max}` previous element can exist "this many" times  
`egrep '0{3,}' [directory/filename]` matches a minimum of "000" or any number of zeroes more than 3  
leaving either min or max blank means any number  
if you just use ONE number in {} then it only matches exactly that number of occurences

`?` match the previous element optionally  
`egrep 'disabled?' [directory/filename]` matches all occurences of "disable" or "disabled"

`|` match one thing or another  
`egrep 'enabled|disabled' [directory/filename]` matches all occurences of both "enabled" and "disabled"

`[]` use for ranges or sets  
`egrep 'c[au]t' [directory/filename]` matches all occurences of either "cut" or "cat" (this is a set)  
`egrep '/dev/[a-z]*' [directory/filename]` match any occurences of "/dev/" followed by anything within "a-z" (this is a range)  
`egrep '/dev/[a-z]*[0-9]?' [directory/filename]` same as above but also optionally matches anything ending in 0-9  
these are case sensitive so if you use [a-z] that is different than [A-Z]  
you can also use a "^" to negate the set  
`egrep 'https[^:]' [directory/filename]` matches "https" that does not have a ":" after it

`()` use for subexpressions  
`egrep '/dev/([a-z]*[0-9]?)*' [directory/filename]` same as above but lets the pattern repeat as many times as needed

## Questions & Notes

It is useful to wrap your patter in single quotes ('') to prevent bash from interpreting special characters  
Grep highlights with color to help you understand the output (unless you use sudo and then you must add the --color option)  
You can use pretty much any combination of `grep` options as well as regex symbols together

## Resources

[RegExr: Learn, Build, & Test RegEx](https://regexr.com/)

### Parent Note

- [Linux Study Journey](./README.md)
