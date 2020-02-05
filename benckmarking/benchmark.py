from contextlib import contextmanager
import logging
import pyarrow.parquet as pq
import time
import argparse
from glob import glob

@contextmanager
def time_usage(name=""):
    """log the time usage in a code block
    prefix: the prefix text to show
    """
    start = time.time()
    yield
    end = time.time()
    elapsed_seconds = float("%.4f" % (end - start))
    logging.info('%s: elapsed seconds: %s', name, elapsed_seconds)

logging.getLogger().setLevel(logging.INFO)
parser = argparse.ArgumentParser(description='Pandas Query Benchmark')
parser.add_argument('path', metavar='path',
                    help='Path of input Parquet file, e.g. /data/input')
args = parser.parse_args()
files = glob(args.path + '/*/*.parquet')
with time_usage("read parquet file"):
    df = pq.ParquetDataset(files).read(nthreads=32).to_pandas()

""" more examples
with time_usage("Q1: sum of single column"):
    df[['ss_customer_sk']].sum()
with time_usage("Q2: distinct count"):
    df['ss_customer_sk'].nunique()
with time_usage("Q3: sum of single column with group by"):
    df[['ss_store_sk', 'ss_net_profit']].groupby('ss_store_sk').sum()
"""