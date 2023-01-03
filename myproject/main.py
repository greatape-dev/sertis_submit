import os
import click
import logging

from lib.cleansing import DataProcessor

@click.command()
@click.option('--source', '-s')
@click.option('--database', '-d')
@click.option('--table', '-t')

def main(source: str, database: str, table: str):
  logging.info

if __name__ == '__main__':
    main()




