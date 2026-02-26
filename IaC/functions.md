---
title: "functions"
date: "2026-02-26"
type: study_notes
tags: [study, IaC]
---

# functions

## Key Concepts

Terraform has a lot of built-in functions that are available for use

## Commands & Examples

`policy = file("admin-policy.json")` read from a specific file
`count = length(var.filename)` use the length of a list/set/map as a variable
`for_each = toset(var.region)` convert list of variables to a set

`terraform console` gives you an interactive console where you can test functions

*numeric functions*
`max` returns the max element from a variable
`min` returns the min element from a variable
when using a variable, you must expand it with ... `max(var.num...)`

*string functions*
`split("<delimeter>", var.ami)` splits a string at the delimiter into a list
`lower(var.ami)` make the values all lowercase
`upper(var.ami)` make the values all uppercase
`title(var.ami)` capitalizes the first element of each word
`substring(var.ami, 0, 7)` returns a substring starting at the 0th value and goes for 7 characters
`join("<delimeter>", var.ami)` opposite of `split`

*collection functions*
`length(var.ami)` returns number of elements
`index(var.ami, "<value>")` returns the index of a value
`element(var.ami, 2)` returns the value at the index
`contains(var.ami, "<value>")` returns "true/false" if the value is present

*map functions*
`keys(var.ami)` turns the keys from a map into a list
`values(var.ami)` turns the values from a map into a list
`lookup(var.ami, "<key>")` returns the value of a key

## Questions & Notes

Think of variable expansion with `...` as similar to using `*` in python

### Parent Note

- [IaC Study Journey](./README.md)
