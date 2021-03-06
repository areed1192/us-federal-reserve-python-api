# United States Federal Reserve API

## Table of Contents

- [Current Version](#current-version)
- [Overview](#overview)
- [Setup](#setup)
- [Usage](#usage)
- [Support These Projects](#support-these-projects)

## Current Version

Version: **0.1.0**

## Overview

What is FRED? Short for Federal Reserve Economic Data, FRED is
an online database consisting of hundred of thousands of economic
data time series from scores of national, international, public, and
private sources. FRED, created and maintained by the Research Department at
the Federal Reserve Bank of St. Louis, goes far beyond simply providing data:
It combines data with a powerful mix of tools that help the user understand, interact
with, display, and disseminate the data. In essence, FRED helps users tell their
data stories. The purpose of this article is to guide the potential (or current)
FRED user through the various aspects and tools of the database.

This library will give you the capability to query data from FRED using Python. To
get started using this library all you need is an API key. To register for an API
Key please go the [developers resources](https://fred.stlouisfed.org/docs/api/api_key.html)
provided by Fred.

## Setup

**Setup - Requirements Install:**

For this particular project, you only need to install the dependencies, to use the project. The dependencies
are listed in the `requirements.txt` file and can be installed by running the following command:

```console
pip install -r requirements.txt
```

After running that command, the dependencies should be installed.

**Setup - Local Install:**

If you are planning to make modifications to this project or you would like to access it
before it has been indexed on `PyPi`. I would recommend you either install this project
in `editable` mode or do a `local install`. For those of you, who want to make modifications
to this project. I would recommend you install the library in `editable` mode.

If you want to install the library in `editable` mode, make sure to run the `setup.py`
file, so you can install any dependencies you may need. To run the `setup.py` file,
run the following command in your terminal.

```console
pip install -e .
```

If you don't plan to make any modifications to the project but still want to use it across
your different projects, then do a local install.

```console
pip install .
```

This will install all the dependencies listed in the `setup.py` file. Once done
you can use the library wherever you want.

**Setup - PyPi Install:**

To **install** the library, run the following command from the terminal.

```console
pip install federal-reserve-python-api
```

**Setup - PyPi Upgrade:**

To **upgrade** the library, run the following command from the terminal.

```console
pip install --upgrade federal-reserve-python-api
```

## Usage

Here is a simple example of using the `fred` library to query some category
data.

```python
from pprint import pprint
from configparser import ConfigParser
from fred.client import FederalReserveClient

# Initialize the Parser.
config = ConfigParser()

# Read the file.
config.read('config/config.ini')

# Get the specified credentials.
api_key = config.get('main', 'api_key')

# Initialize the Client.
fred_client = FederalReserveClient(api_key=api_key)

# Initialize the Categories Service.
categories_service = fred_client.categories()

# Grab a category by it's ID.
pprint(categories_service.get_category(category_id='125'))
```

## Support These Projects

**Patreon:**
Help support this project and future projects by donating to my [Patreon Page](https://www.patreon.com/sigmacoding). I'm
always looking to add more content for individuals like yourself, unfortuantely some of the APIs I would require me to
pay monthly fees.

**YouTube:**
If you'd like to watch more of my content, feel free to visit my YouTube channel [Sigma Coding](https://www.youtube.com/c/SigmaCoding).

**Questions:**
If you have questions please feel free to reach out to me at [coding.sigma@gmail.com](mailto:coding.sigma@gmail.com?subject=[GitHub]%20Fred%20Library)
