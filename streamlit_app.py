import streamlit as st
from streamlit.uploaded_file_manager import UploadedFile

import certificate.config as c
from certificate import Certificate


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

    certificate_types = c.DICT_CONTENT.keys()
    certificate_type = st.sidebar.selectbox(
        label="Pilih jenis sertifikat:",
        options=certificate_types,
        key="chosen_certificate_type"
    )
    if certificate_type == "custom":
        custom()
    else:
        certificate = Certificate(certificate_type)

        st.write("**{} certificate template:**".format(certificate_type))
        st.image(certificate.template)

if __name__ == "__main__":
    main()
