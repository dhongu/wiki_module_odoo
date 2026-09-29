"""Anonimizează capturile fișei consultant pentru publicare pe Odoo Apps Store.

Capturile originale (readme/screenshots) sunt făcute pe o instalare reală și conțin
numele clientului, hostname-ul serverului CalDAV și un utilizator de mail. Copiile
publicate în static/description folosesc date generice.
"""

from PIL import Image, ImageDraw, ImageFont

SRC = "/Users/dhongu/Odoo/odoo19/odoo-addons/bitshop/deltatech_calendar_caldav/readme/screenshots/"
DST = "/Users/dhongu/Odoo/odoo19/odoo-addons/bitshop/deltatech_calendar_caldav/static/description/"
ARIAL = "/System/Library/Fonts/Supplemental/Arial.ttf"


def font(size):
    return ImageFont.truetype(ARIAL, size)


def patch(draw, box, bg, text=None, xy=None, size=13, fg=(55, 65, 81)):
    """Acoperă `box` cu fundalul dat și rescrie textul pe aceeași linie de bază."""
    draw.rectangle(box, fill=bg)
    if text:
        draw.text(xy, text, font=font(size), fill=fg, anchor="ls")


W = (255, 255, 255)

# ---- 01: lista de conturi -------------------------------------------------
im = Image.open(SRC + "01_lista_conturi.png").convert("RGB")
d = ImageDraw.Draw(im)
patch(d, (44, 154, 340, 176), W, "Acme Corp - Calendar", (46, 168))
patch(d, (612, 154, 960, 176), W, "https://caldav.example.com/", (615, 168))
im.save(DST + "caldav_accounts.png")

# ---- 02: formularul contului ---------------------------------------------
im = Image.open(SRC + "02_cont_configurat.png").convert("RGB")
d = ImageDraw.Draw(im)
patch(d, (64, 68, 242, 92), W, "Acme Corp - Calendar", (66, 86), size=17)
patch(d, (91, 173, 340, 194), W, "Acme Corp - Calendar", (93, 187))
patch(d, (886, 173, 1240, 194), W, "https://caldav.example.com/", (888, 187))
patch(d, (886, 210, 1240, 231), W, "odoo@example.com", (888, 224))
patch(
    d,
    (886, 319, 1500, 340),
    W,
    "https://caldav.example.com/calendars/odoo%40example.com/calendar/",
    (888, 333),
    fg=(110, 110, 110),
)
im.save(DST + "caldav_account_form.png")

# ---- 03: evenimentele sincronizate ---------------------------------------
im = Image.open(SRC + "03_evenimente_sincronizate.png").convert("RGB")
d = ImageDraw.Draw(im)
patch(d, (198, 53, 380, 73), W, "Acme Corp - Calendar", (200, 67), size=12, fg=(1, 126, 132))
px = im.load()
for baseline in (169, 209, 249, 329):
    bg = px[420, baseline - 5]
    patch(d, (44, baseline - 15, 340, baseline + 6), bg, "Team meeting - weekly sync", (46, baseline))
row4_bg = px[420, 284]
patch(d, (44, 274, 340, 295), row4_bg, "Offer presentation - new client", (46, 289))
# chip participant: repictează pila la lățimea noului nume
d.rectangle((876, 274, 992, 296), fill=row4_bg)
d.rounded_rectangle((878, 277, 940, 294), radius=8, fill=(230, 221, 221))
d.text((884, 289), "John Doe", font=font(11), fill=(60, 60, 60), anchor="ls")
im.save(DST + "caldav_synced_events.png")

# ---- 04: calendarul Odoo --------------------------------------------------
im = Image.open(SRC + "04_calendar_odoo.png").convert("RGB")
d = ImageDraw.Draw(im)
patch(d, (636, 534, 814, 551), (213, 213, 213), "Team meeting - weekly s...", (640, 547), size=12, fg=(0, 0, 0))
patch(d, (826, 682, 1004, 698), (170, 216, 213), "Offer presentation - ne...", (830, 694), size=12, fg=(0, 0, 0))
im.save(DST + "caldav_calendar.png")

print("gata")
