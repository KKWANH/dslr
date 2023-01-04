# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    histogram.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kkim <kkim@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/01/03 20:09:10 by kkim              #+#    #+#              #
#    Updated: 2023/01/04 14:25:09 by kkim             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# ------------------------------------------------------------------------------
# import : DSLR
from DSLR.core import ft_histogram

# ------------------------------------------------------------------------------
# import : library
import numpy
import argparse

# ------------------------------------------------------------------------------
# main
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", type=str)
    args = parser.parse_args()
    ft_histogram(args.file_name)