"""Utility tools for certificates."""
from pathlib import PosixPath
from typing import Dict
from zipfile import ZipFile

import pandas as pd

import certificate.config as c


def get_config(file: str = c.CONFIG_FILE) -> Dict:
    """Get configuration file.

    The configuration file must be a CSV and follow below rules:
    - the first column must be certificate type (`type`)
    - the remaining columns are tuples of component to write
      with convention (componentname_config). E.g. name_font_type

    Args:
        file (str): configuration file

    Returns:
        Dict: a dictionary of each certificate type with
            corresponding component configurations
    """
    config = pd.read_csv(file, index_col="type")
    for col in config.columns:
        if "loc" in col:
            config[col] = config[col].apply(
                lambda loc: tuple(map(int, loc.split(",")))
            )

    return config.to_dict(orient="index")


def make_zip(dirs: PosixPath, name: str = "certificates.zip",
             ext: str = ".png") -> str:
    with ZipFile(name, "w") as outs:
        for file in dirs.rglob("**/*" + ext):
            outs.write(file)

    return name
