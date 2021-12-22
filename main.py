from textwrap import wrap
from time import time

import pandas as pd
from PIL import Image, ImageColor, ImageDraw, ImageFont

import config as c


def main():
    start = time()

    # load certifcates data
    df_certif = pd.read_csv(c.CERT_FILENAME)
    df_certif.drop(columns=["voucher_code", "certif_link"], inplace=True)
    df_certif["student_name"] = df_certif["student_name"].apply(
        lambda name: name.title()
    )

    df_certif.apply(write_certificate, axis=1)
    print("Done generating all {} certificates in {:.2f}s".format(
        df_certif.shape[0], time() - start
    ))

def write_certificate(row):
    if row["student_name"] != "Sitti Hadira Nur Alifya":
        continue
    certif_type = "graduation"
    if row.certif_type == "penyelesaian":
        certif_type = "completion"

    if row.class_title == "Raih penghasilan jutaan dari Instagram":
        certif_type = "old"

    if certif_type == "completion":
        template = c.CERT_COMPLETION_TEMPLATE
    elif certif_type == "graduation":
        template = c.CERT_GRADUATION_TEMPLATE
    else:
        template = c.CERT_OLD_TEMPLATE

    certificate = Image.open(template)
    drawer = ImageDraw.Draw(certificate)

    for location in c.DICT_FONT_STYLE[certif_type].keys():
        if location == "competency_list":
            competency_file = (c.COMPETENCY_DIR / row.class_title)
            with competency_file.open("r") as f:
                text = [
                    "\n".join(wrap(line))
                    for line in f
                ]
                if certif_type == "completion":
                    text = "\n\n".join(text)
                else:
                    text = "\n".join(text)
        else:
            text = "\n".join(wrap(str(row[location])))

        font_dir = c.FONT_DIR / c.DICT_FONT_STYLE[certif_type][location][
            "font_type"
        font_style = ImageFont.truetype(
            (
                font_dir
                / (
                    c.DICT_FONT_STYLE[certif_type][location]["font_type"]
                    + "-"
                    + c.DICT_FONT_STYLE[certif_type][location]["font_style"]
                    + ".ttf"
                )
            ).as_posix(),
            size=(
                c.DICT_FONT_STYLE[certif_type][location]["font_size"]
                if certif_type != "completion"
                else
                c.DICT_FONT_STYLE[certif_type][location]["font_size"]*4
            )
        )
        font_color = ImageColor.getrgb(
            "#" + c.DICT_FONT_STYLE[certif_type][location]["font-color"]
        )

        drawer.textsize(
            text, font=font_style
        )

        drawer.text(
            c.DICT_FONT_STYLE[certif_type][location]["coordinate"],
            text=text,
            anchor="la",
            font=font_style,
            fill=font_color,
        )

    certificate.save(
        (
            c.CERT_TARGET_DIR / f"dec/{row.certif_id}_{row.student_name}.png"
        ).as_posix()
    )


if __name__ == "__main__":
    main()
