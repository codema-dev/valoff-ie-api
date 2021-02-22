import json
from pathlib import Path
import os
import requests
from requests import HTTPError
from typing import List
from typing import Union
from urllib.request import quote

from loguru import logger

HERE = os.path.dirname(__file__)

with open(os.path.join(HERE, "local_authorities.json")) as file:
    LOCAL_AUTHORITIES = [x['LaDesc'] for x in json.load(file)]

with open(os.path.join(HERE, "categories.json")) as file:
    CATEGORIES = [x['categorydesc'] for x in json.load(file)]

FILETYPES = ["csv", "json", "geojson"]

def docstring_parameter(*sub):
    def dec(obj):
        obj.__doc__ = obj.__doc__.format(*sub)
        return obj
    return dec


def _set_group(group, global_group):
    
    if group == "all":
        group = global_group
    else:
        if not set(group).issubset(set(global_group)):
            raise ValueError(
                f"{group} is not a subset of {global_group}"
            )
    return group


def _set_filetype(filetype, filetypes):

    if not set(filetype).issubset(set(filetypes)):
        raise ValueError(
            f"{filetype} is not a subset of {filetypes}"
        )
    return filetype

@docstring_parameter(Path.cwd(), LOCAL_AUTHORITIES, CATEGORIES, FILETYPES)
def download_valuation_office_categories(
    savedir: str=Path.cwd(),
    local_authorities: Union[List[str], str]="all",
    categories: Union[List[str], str]="all",
    filetype: str="csv",
):
    """Download Valuation Office categories.

    Args:
        savedir (str): Path to save directory. Defaults to {0}
        local_authorities (List[str], optional): Any of {1}. Defaults to 'all'.
        categories (List[str], optional): Any of {2}. Defaults to 'all'.
        filetype (str, optional): Any of {3}. Defaults to 'csv'.
    """
    dirpath = Path(savedir) / "valuation_office"
    if dirpath.exists():
        logger.info(f"Skipping creation of {dirpath} as already exists...")
    else:
        os.mkdir(dirpath)

    local_authorities = _set_group(local_authorities, LOCAL_AUTHORITIES)
    categories = _set_group(categories, CATEGORIES)
    filetype = _set_filetype(filetype, FILETYPES)

    for local_authority in local_authorities:
        for category in categories:
            local_authority_without_whitespace = local_authority.replace(" ", r"%20")
            url = (
                "https://api.valoff.ie/api/Property/GetProperties?"
                "Fields=*"
                f"&LocalAuthority={local_authority_without_whitespace}"
                f"&CategorySelected={category}"
                f"&Format={filetype}"
                "&Download=true"
            )
            category_without_slashes = category.replace("/", " or ")
            filepath = (
                dirpath / f"{local_authority} - {category_without_slashes}.{filetype}"
            )
            logger.info(
                f"Downloading {local_authority} {category_without_slashes} "
                f"to '{filepath}' via:\n {url}"
            )
            try:
                response = requests.get(url)
            except HTTPError as error:
                logger.error(error)
            
            with open(filepath, "wb") as file:
                file.write(response.content)
