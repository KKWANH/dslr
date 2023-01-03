import argparse
from DSLR.core import ft_describe

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", type=str)
    args = parser.parse_args()
    ft_describe(args.file_name)