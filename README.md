# Valuation Office Ireland

An unofficial Python API for the [Valuation Office API](https://www.valoff.ie/en/open-data/api/)

## Installation

```python
pip install valuation-office-ireland
```

## Basic Usage

To download all Valuation Office categories for Dublin:

```python
from valuation_office_ireland.download import download_valuation_office_categories

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

See `example.ipynb` for more information