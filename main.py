from argparse import ArgumentParser, Namespace
import os

from lib import dft_scf

G16_PATH = '/home/gridsan/oscarwu/GRPAPI/Software/g16/'

parser = ArgumentParser()

parser.add_argument('--job_folder', type=str, default='DFT',
                    help='folder for DFT job')

args = parser.parse_args()

pdir = args.job_folder

for f in os.listdir(pdir):
    try:
        dft_scf(args.DFT_folder, G16_PATH, f)
    except Exception as e:
        pass
    


