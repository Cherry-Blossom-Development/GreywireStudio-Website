# Greywire Studio website

The website for Greywire Studio and its Linework series of guitar pedals, planned for **greywirestudio.com** (the domain isn't bought yet). The pedal designs themselves are in the [GreywireStudio](https://github.com/Cherry-Blossom-Development/GreywireStudio) repository.

It's a plain static site: HTML and CSS, no build step and no JavaScript. Any static host can serve it as is.

## Pages

| File | Page |
| --- | --- |
| `index.html` | Home: what Linework is, the pedals, the network to come |
| `linework.html` | How the system works: audio path, control loop, setlist to stage |
| `flashover.html` | Flashover distortion / overdrive |
| `switchyard.html` | Switchyard control pedal |
| `ideas.html` | What's next: the four named pedals in planning, then further ideas by effect type |
| `opinion.html` | Your Opinion: how the surveys work, the privacy promise, what a new product costs, and the list of surveys |
| `survey-musician.html`, `survey-gear.html`, `survey-sounds.html` | One page per survey; "coming soon" placeholders for now |
| `about.html` | The brand, where each product stands, link to the design files |
| `404.html` | Page-not-found (uses root-relative links, so it works at any path) |

Shared styles are in `css/site.css`. The logo and pedal illustrations are SVGs in `img/`; the pedal drawings are illustrations, not final designs. The four planned pedals (Tap Changer, Three Phase, Rolling Blackout, Double Circuit) are drawn by `tools/make_pedal_svgs.py`, and their controls are placeholders until each pedal is designed: edit the script and rerun it rather than editing those SVGs by hand.

The header and footer are repeated in every page. When adding a page, copy an existing one and set `aria-current="page"` on its menu link.

## Viewing it locally

Open `index.html` in a browser, or serve the folder so the 404 page's links work too:

```
python -m http.server 8000
```

then go to http://localhost:8000.

## Content rules

- Only describe features that are decided in the design documents. Mark anything else as planned.
- Nothing is for sale yet: no prices or buy buttons until there's a product.
- Product names are working names until the trademark filings are done.
- Don't promise recording or paid effect downloads; both need a patent check first (see `IP_RESEARCH.md` in the GreywireStudio repo).

## Hosting

The site runs on the same EC2 server as the other Cherry Blossom Development sites (Amazon Linux, 44.225.148.34), served by the host nginx.

| What | Where |
| --- | --- |
| Domain | greywirestudio.com, registered at Porkbun. DNS: `A` records for `greywirestudio.com` and `www` pointing to 44.225.148.34 |
| Files on the server | `/var/www/greywirestudio.com` (owned by `ec2-user`) |
| nginx config | `/etc/nginx/conf.d/greywirestudio.com.conf`. The starting version is `nginx/greywirestudio.com.conf` here; certbot adds the HTTPS parts on the server |
| Certificate | Let's Encrypt via `certbot --nginx`, renewed automatically by the server's `certbot-renew` timer |

### Publishing changes

Commit the change, then from Git Bash in this folder:

```
./deploy.sh
```

It copies the HTML, `css/` and `img/` to the server, replacing the old files. It needs the SSH key at `~/.ssh/Hostgator-Key-1.pem`, the same one the Breakroom deploy uses.

### Getting the certificate (one time, done Oct 19, 2026)

This was run on the server once the Porkbun DNS pointed there. Only rerun it if the site is ever moved to a new server:

```
sudo certbot --nginx -d greywirestudio.com -d www.greywirestudio.com
```

Certbot adds the HTTPS server block and the redirect from HTTP to HTTPS.

Fonts come from Google Fonts (Space Grotesk and IBM Plex Mono).
