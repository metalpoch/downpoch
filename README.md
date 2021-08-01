# Downpoch

*A simple download manager CLI written with Python 3.9.6*

Download your favorite files from the internet 

## Installation

##### Clone this repository [GitHub](https://github.com/metalpoch/downpoch) and create a virtual environment
```bash
git clone https://github.com/metalpoch/downpoch.git
cd downpoch/
python -m venv venv
source venv/bin/activate
```

##### Use [pip](https://pip.pypa.io/en/stable/) to install the modules in the file requirements.txt 
```bash
pip install -r requirements.txt
```

## Use
##### Download from url
```bash
python downpoch.py simple http://url/to/download
```

##### Download from multiple url
```bash
python downpoch.py multiple /path/to/document-with-url.txt
```

## Licence
[MIT](https://choosealicense.com/licenses/mit/)
