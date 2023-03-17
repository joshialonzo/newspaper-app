# NGINX Server

Install NGINX

```bash
sudo apt-get install nginx
```

Check the NGINX status

```bash
sudo systemctl status nginx
```

Review sites available

```bash
cd /etc/nginx/sites-available
```

Create a site available

```bash
# site.available.tld: Name of the site available file
touch /etc/nginx/sites-available/site.available.tld
```

Review sites enabled

```bash
cd /etc/nginx/sites-enabled
```