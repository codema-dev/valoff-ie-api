# Unofficial `valoff.ie` Python API

[![PyPI version shields.io](https://img.shields.io/pypi/v/valoff-ie-api.svg)](https://pypi.python.org/pypi/valoff-ie-api/)

An unofficial Python API for https://www.valoff.ie/en/open-data/api/

## Installation

```python
pip install valoff-ie-api
```

## Basic Usage

To download all Valuation Office categories for Dublin:

```python
from valoff_ie_api import download_valuation_office_categories

download_valuation_office_categories(
    savedir="data",
    local_authorities=[
        "DUBLIN CITY COUNCIL",
        "DUN LAOGHAIRE RATHDOWN CO CO",
        "FINGAL COUNTY COUNCIL",
        "SOUTH DUBLIN COUNTY COUNCIL",
    ]
)
```

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/codema-dev/valoff-ie-api/HEAD?labpath=example.ipynb) ⬅️ Run `example.ipynb` for more information