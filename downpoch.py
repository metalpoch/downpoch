'''
Download your files with this app
'''
import os
import click

import requests.exceptions
from utilities import download


@click.group()
def main():
    pass


@main.command()
@click.argument('url')
@click.option(
    '--output-dir', '-o',
    default=os.getcwd,
    metavar='',
    help='Output directory'
)
def simple(url: str, output_dir: str):
    '''
    Download only a file
    '''
    try:
        download(url, output_dir)
    except requests.exceptions.MissingSchema:
        print(f"Invalid URL: '{url}'")

@main.command()
@click.argument('file')
@click.option(
    '--output-dir', '-o',
    default=os.getcwd,
    metavar='',
    help='Output directory'
)
def multiple(file: str, output_dir: int):
    '''
    Download multiple files from a text document with URL
    '''
    # Read file input with the urls and create a list
    with open(file, 'r') as f:
        urls = [_.rstrip('\n') for _ in f.readlines()]

    # Download list of url
    for url in urls:
        try:
            download(url, output_dir)
        except requests.exceptions.MissingSchema:
            print(f"Invalid URL on line {urls.index(url) + 1}: '{url}'")


if __name__ == '__main__':
    main()
