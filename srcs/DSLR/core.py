# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    core.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kkim <kkim@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/01/03 16:22:38 by kkim              #+#    #+#              #
#    Updated: 2023/01/03 20:01:31 by kkim             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import csv
import numpy
import matplotlib
import matplotlib.pyplot as plt
from DSLR.math import ft_count, ft_mean, ft_std, ft_min, ft_max, ft_percentile
from DSLR.colors import colors as c

def ft_describe(_file_name):
    dataset = ft_read_csv(_file_name)
    index = dataset[0]
    dataset = dataset[1:, :]
    print(f"{c.BLUE}┌─────────────────┬─────────────┬─────────────┬─────────────┬─────────────┬─────────────┬─────────────┬─────────────┬─────────────┐{c.RESET}")
    print(f'{c.BLUE}│ {"":15}',
          f'{c.RESET}{c.BLUE}│{c.RESET}{c.BOLD}{c.GREEN }{"Count":>12}',
          f'{c.RESET}{c.BLUE}│{c.RESET}{c.BOLD}{c.GREEN }{"Mean":>12}',
          f'{c.RESET}{c.BLUE}│{c.RESET}{c.BOLD}{c.GREEN }{"Std":>12}',
          f'{c.RESET}{c.BLUE}│{c.RESET}{c.BOLD}{c.YELLOW}{"Min":>12}',
          f'{c.RESET}{c.BLUE}│{c.RESET}{c.BOLD}{c.PURPLE}{"25%":>12}',
          f'{c.RESET}{c.BLUE}│{c.RESET}{c.BOLD}{c.PURPLE}{"50%":>12}',
          f'{c.RESET}{c.BLUE}│{c.RESET}{c.BOLD}{c.PURPLE}{"75%":>12}',
          f'{c.RESET}{c.BLUE}│{c.RESET}{c.BOLD}{c.YELLOW}{"Max":>12} {c.BLUE}│')
    print(f"{c.BLUE}├─────────────────┼─────────────┴─────────────┴─────────────┴─────────────┴─────────────┴─────────────┴─────────────┴─────────────┤{c.RESET}")
    for i in range(0, len(index)):
        print(f'{c.BLUE}│{c.RESET} {c.BOLD}{index[i]:15.15}{c.RESET}{c.BLUE}', end=' │')
        try:
            data = numpy.array(dataset[:, i], dtype=float)
            data = data[~numpy.isnan(data)]
            if not data.any():
                raise Exception()
            print(f"{c.RESET}{ft_count(data):>12.4f}", end='  ')
            print(f"{ft_mean(data):>12.4f}", end='  ')
            print(f"{ft_min(data):>12.4f}", end='  ')
            print(f"{ft_max(data):>12.4f}", end='  ')
            print(f"{ft_percentile(data, 25):>12.4f}", end='  ')
            print(f"{ft_percentile(data, 50):>12.4f}", end='  ')
            print(f"{ft_percentile(data, 75):>12.4f}", end='  ')
            print(f"{ft_max(data):>12.4f}{c.BLUE}", end=' │\n')
        except:
            print(f"{c.RESET}{ft_count(dataset[:, i]):>12}", end='  ')
            print(f'{"No numerical value to display":>60}                                     {c.BLUE}│')
    print(f"{c.BLUE}└─────────────────┴───────────────────────────────────────────────────────────────────────────────────────────────────────────────┘{c.RESET}")

# float만 입력받~~~
def ft_read_csv(_file_name):
    dataset = list()
    with open(_file_name) as csv_file:
        reader = csv.reader(csv_file)
        try:
            for line in reader:
                row = list()
                for value in line:
                    try:
                        value = float(value)
                    except:
                        if not value: #
                            value = numpy.nan
                    row.append(value)
                dataset.append(row)
        except csv.Error as exp:
            print("error occured")
    return numpy.array(dataset, dtype=object)