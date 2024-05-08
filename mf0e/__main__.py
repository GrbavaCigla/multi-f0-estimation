import os
import argparse
from argparse import FileType

from .estimate import F0Estimate


# set up command line argument structure
parser = argparse.ArgumentParser(description='Estimate the pitches in an audio file.')
parser.add_argument("file", type=FileType("rb"))
parser.add_argument('-v', '--verbose', help='increase output verbosity', action='store_true')
  

if __name__ == '__main__':
    # parse command line arguments
    args = parser.parse_args()

    # check file extensions are correct for this type of conversion
    _, input_ext = os.path.splitext(args.file.name)
    if input_ext != '.wav':
        raise ValueError('Input path must be a wav file')

    freq_est = F0Estimate(max_poly=6)
    f0_estimates, notes = freq_est.estimate_f0s(args.file.name)
    notes_c = freq_est.collapse_notes(notes)
    print(*notes_c, sep='\n')
