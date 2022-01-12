import random

import pandas as pd
import streamlit as st
from streamlit.uploaded_file_manager import UploadedFile

import certificate.config as c
from certificate import Certificate
from certificate.utils import get_config, make_zip


def custom():
    custom_template = st.sidebar.file_uploader(
        label="Upload template sertifikat:",
        key="custom_template"
    )
    if custom_template:
        st.write("**Custom template:**")
        st.image(custom_template)



def main():
    st.title("Certificate Generator App")

    certificate_types = c.DICT_CONTENT
    certificate_type = st.sidebar.selectbox(
        label="Pilih jenis sertifikat:",
        options=certificate_types.keys(),
        key="chosen_certificate_type"
    )
    if certificate_type == "custom":
        custom()
    else:
        certificate = Certificate(template_image=certificate_type)
        template_image = certificate.template

        st.write("**{} certificate template:**".format(certificate_type.title()))
        st.image(template_image)

    file = st.sidebar.file_uploader(
        label="Upload recipients data",
        key="recipients"
    )
    if file:
        recipients = pd.read_csv(file, parse_dates=["submit_at"])
        recipients["name"] = recipients["name"].str.title()
        recipients.sort_values("submit_at", inplace=True)
        recipients.reset_index(drop=True, inplace=True)
        st.write("Sample recipients:\n", recipients.head())

        prefix_text = st.text_input("Masukkan prefix ID sertifikat:",
                                    value="WBL0101")

    if c.CONFIG_FILE.exists():
        config = get_config(c.CONFIG_FILE)
    else:
        config = c.DICT_CONTENT

    custom_config = st.sidebar.file_uploader(
        label="Upload custom component configurations",
        key="custom_config"
    )
    if custom_config:
        use_custom_config = st.sidebar.checkbox(
            label="Use custom configurations"
        )
        if use_custom_config:
            config = get_config(custom_config)

    generate = st.button("Generate certficates", key="is_generate")
    if generate:
        if not file:
            st.error(
                "Harap upload daftar penerima sertifikat terlebih dahulu!"
            )
        else:
            certificates = []
            for recipient in recipients.itertuples(name="Recipient"):
                certificate = Certificate(
                    name=recipient.name,
                    template_image=certificate_type,
                )
                certificate.generate(
                    recipient, certificate.template, config, prefix_text
                )
                certificate.save(recipient, prefix_text, c.OUT_DIR)
                certificates.append(certificate.certificate_)


            st.write("Preview sertifikat:")
            st.image(random.sample(certificates, 1))

            zip_file = make_zip(c.OUT_DIR)
            with open(zip_file, "rb") as file:
                download = st.download_button(
                    label="Download certificates",
                    data=file,
                    file_name="certificates.zip",
                    mime="application/zip",
                    key="download_certificates"
                )


if __name__ == "__main__":
    main()
