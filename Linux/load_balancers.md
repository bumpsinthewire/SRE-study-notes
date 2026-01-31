---
title: "load_balancers"
date: "2026-01-28"
type: study_notes
tags: [study, linux]
---

# load_balancers

## Key Concepts

Reverse proxies and load balancers are similar but different  
A reverse proxy essentially takes a request and forwards it to a server on your behalf  
A load balancer adds intelligence (load balancing) to this process and chooses a server from a pool of servers  
`nginx` is one of the most well known proxies in the world and can be used for both a reverse proxy and a load balancer

## Commands & Examples

`sudo apt install nginx` to install `nginx`  
add a file to `/etc/nginx/sites-available/` to create the config you desire (eg. reverse proxy or load balancer)

reverse proxy:
```nginx
server {
  listen 80;
  location / {
    proxy_pass http://1.1.1.1;
  }
}
```
this `nginx` snippet tells the server to listen for traffic coming in on port 80, destined for any directory starting with "/", and then sending it to 1.1.1.1

load balancer:
```nginx
upstream mywebservers {
  server 1.2.3.4;
  server 5.6.7.8;
}

  server {
    listen 80;
    location / {
      proxy_pass http://mywebservers;
    }
}
```
for a load balancer, you do the same config as reverse proxy, but you must define the pool of webservers first

`nginx -t` tests your `nginx` configuration files  
use `systemctl reload nginx.service` to reload `nginx` and apply your configuration files

## Questions & Notes

the main `nginx` config is located at `/etc/nginx/nginx.conf` and it points to other locations to find your config files  
it is best practice to *soft* link `/etc/nginx/sites-available/` to `/etc/nginx/sites-enabled/`  
as well as removing `/etc/nginx/sites-enabled/default`

## Resources

[nginx](https://nginx.org/)

### Parent Note

- [Linux Study Journey](./README.md)
