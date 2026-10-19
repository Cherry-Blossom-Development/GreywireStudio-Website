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
| `about.html` | The brand, where each product stands, link to the design files |
| `404.html` | Page-not-found (uses root-relative links, so it works at any path) |

Shared styles are in `css/site.css`. The logo and pedal illustrations are hand-written SVGs in `img/`; the pedal drawings are illustrations, not final designs.

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

## Hosting (not set up yet)

Once the domain is bought, the simplest options are:

- **GitHub Pages:** turn on Pages for this repository, add a `CNAME` file containing `greywirestudio.com`, and point the domain's DNS at GitHub.
- **The existing EC2 server:** add an nginx site serving this folder, with a certificate from Let's Encrypt.

Fonts come from Google Fonts (Space Grotesk and IBM Plex Mono).
