"""Re-create site/img photo files from originals/ with light enhancement.

Run from the project folder:  python tools/process_photos.py
"""
import os

from PIL import Image, ImageEnhance, ImageFilter, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIG = os.path.join(ROOT, "originals")
OUT = os.path.join(ROOT, "site", "img")

PHOTOS = {
    "untitled-design-48.png": "retail-plaza-jimmy-johns-pizza-hut-smoothie-king",
    "7.png": "pump-station-tank-installation",
    "photo-1.png": "storm-sewer-pipe-installation-crew",
    "photo-16.png": "manhole-water-valve-installation",
    "photo-18.png": "underground-utility-trench-excavation",
    "photo-3.png": "pump-room-piping-installation",
    "photo-5.png": "large-water-valve-installation",
    "photo-6.png": "industrial-pump-room-upgrade",
    "photo-9.png": "precast-structure-crane-set",
    "rbf-1.jpg": "commercial-site-excavation-grading",
    "rbf-6-concrete.jpg": "concrete-road-curb-gutter-construction",
    "rbf-8.jpg": "steel-frame-commercial-building",
    "rbf18.jpg": "foundation-walls-excavation",
}
# Homepage slideshow, in display order
SLIDES = ["retail-plaza-jimmy-johns-pizza-hut-smoothie-king", "commercial-renovation-after",
          "commercial-site-excavation-grading", "precast-structure-crane-set",
          "underground-utility-trench-excavation", "industrial-pump-room-upgrade"]


def load(name):
    im = Image.open(os.path.join(ORIG, name)).convert("RGBA")
    im = im.crop(im.split()[3].getbbox())
    flat = Image.new("RGB", im.size, (255, 255, 255))
    flat.paste(im, mask=im.split()[3])
    return flat


def enhance(im):
    im = ImageOps.autocontrast(im, cutoff=0.5, preserve_tone=True)  # no color cast
    im = ImageEnhance.Color(im).enhance(1.08)
    im = ImageEnhance.Contrast(im).enhance(1.05)
    return im.filter(ImageFilter.UnsharpMask(radius=1.3, percent=60, threshold=3))


def save(im, name, width=None, quality=80):
    if width and im.width != width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
        if width > 1000:
            im = im.filter(ImageFilter.UnsharpMask(radius=1.6, percent=40, threshold=2))
    im.save(os.path.join(OUT, name + ".webp"), "WEBP", quality=quality, method=6)


def main():
    done = {}
    for src, name in PHOTOS.items():
        im = enhance(load(src))
        done[name] = im
        save(im, name, min(im.width, 1600))
        if name.startswith("retail-plaza"):
            save(im, name + "-800", 800)
    # Before/after: split the original banner and crop off its baked-in labels
    full = Image.open(os.path.join(ORIG, "banner.png")).convert("RGBA")
    bg = Image.new("RGB", full.size, (255, 255, 255))
    bg.paste(full, mask=full.split()[3])
    top, bot = 512, 1012
    halves = {"commercial-renovation-before": bg.crop((58, top, 1715, bot)),
              "commercial-renovation-after": bg.crop((1721, top, 3472, bot))}
    w = min(h.width for h in halves.values())
    for name, im in halves.items():
        im = enhance(im.crop(((im.width - w) // 2, 0, (im.width - w) // 2 + w, bot - top)))
        done[name] = im
        save(im, name)
        save(im, name + "-800", 800)
    for name in SLIDES:
        im = done[name]
        if im.width / im.height < 1.6:  # crop taller photos to a wide frame
            h = int(im.width / 1.6)
            t = int((im.height - h) * 0.55)
            im = im.crop((0, t, im.width, t + h))
        save(im, name + "-hero", 1920, quality=78)
        save(im, name + "-hero-960", 960, quality=76)
    print("Processed", len(done), "photos and", len(SLIDES), "slides")


if __name__ == "__main__":
    main()
