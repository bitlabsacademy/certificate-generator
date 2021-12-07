from time import time

import pandas as pd
from PIL import Image, ImageColor, ImageDraw, ImageFont

start = time()
data_filename = "data/names/wds09201.csv"
certif_filename = "data/certificates/wds09201.png"
# names = ["Vincent Nelwan", "Achmad Maulana Dzaky"]
names = pd.read_csv(
    data_filename,
    # parse_dates=["Start Date (UTC)", "Submit Date (UTC)"]
)
# names = names[names["Eligible for Sertif?"] == "Y"]
names.sort_values("Submitted At", inplace=True)
certid_prefix = "WDS09201{:03}"

# set font type and color for name
font_name = ImageFont.truetype(
    "data/fonts/Epilogue/Epilogue-SemiBold.ttf",
    size=2*22
)
color_name = ImageColor.getrgb("#192256")

# set font type and color for certificate ID
font_certid = ImageFont.truetype(
    "data/fonts/Space_Mono/SpaceMono-Regular.ttf",
    size=2*10
)
color_certid = ImageColor.getrgb("#434B75")

certificate = Image.open(certif_filename)
drawer = ImageDraw.Draw(certificate)

image_width, image_height = certificate.size

print("Generating {} certificates".format(names.shape[0]))
for idx, name in enumerate(names["Nama Lengkap"]):
# for idx, name in enumerate(names.head()):
    if (idx+1) % 50 == 0:
        print(f"Done generating {idx+1} certificates..")
    certificate = Image.open(certif_filename)
    drawer = ImageDraw.Draw(certificate)

    name_width, name_height = drawer.textsize(name.title(), font=font_name)
    certid_full = certid_prefix.format(idx+1)
    # certid_full = certid_prefix
    certid_width, certid_height = drawer.textsize(
        certid_full, font=font_certid
    )
    drawer.text(
        (image_width / 8, image_height / 2.68),
        text=name.title(),
        anchor="la",
        font=font_name,
        fill=color_name
    )
    drawer.text(
        (image_width / 8.5, image_height / 1.2),
        text=certid_full,
        anchor="la",
        font=font_certid,
        fill=color_certid
    )
    certificate.save(
        f"data/webinar-certificates/sep/WDS09201/{certid_full}-{name.title()}.png"
    )

print("Done generating all {} certificates in {:.2f}s".format(
    names.shape[0], time() - start
))
