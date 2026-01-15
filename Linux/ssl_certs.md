---
title: "SSL_certs"
date: "2026-01-14"
type: study_notes
tags: [study, linux]
---

# SSL_certs

## Key Concepts

Managing security certificates is a very common task for an SRE
OpenSSL is the most commonly used utility for creating these certificates but it has a crazy amount of things it can do in addition

## Commands & Examples

`openssl help` gives you a list of all of the capabilities
`man openssl` use tab to see all of the options

`req` and `x509` are the focus of most `openssl` work
    `req` is used to generate both a private key and a CSR (but can also use the `x509` flag to self-sign)
    `x509` command is used to generate a self-signed certificate but can also let you read certificate information

`openssl req -new -newkey rsa:2048 -keyout key.pem -out req.csr` creates new key with RSA2048 encryption, saves it to "key.pem", and generates and saves a CSR to "req.csr"
`openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.crt` same as above but self signs the certificate for use immediately

`openssl x509 -in mycertificate.crt -text` outputs the text of the mycertificate.crt certificate

## Questions & Notes

Even though everyone talks about them as "SSL certificates", these day's SSL has been replaced with TLS (Transport Layer Security)
Creating a new key and CSR and then getting it validated by a CA is the "professional" way to work with certificates
Creating a self-signed certificate is usually reserved for lab environments
