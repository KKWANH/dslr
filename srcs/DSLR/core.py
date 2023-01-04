# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    core.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kkim <kkim@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/01/03 16:22:38 by kkim              #+#    #+#              #
#    Updated: 2023/01/04 14:22:01 by kkim             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# ------------------------------------------------------------------------------
# import : DSLR
from DSLR.math import ft_count, ft_mean, ft_std, ft_min, ft_max, ft_percentile
from DSLR.colors import colors as c

# ------------------------------------------------------------------------------
# import : library
import csv
import numpy
import matplotlib
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------
# util

# ft_read_csv(filename)
#   ~~~
#   float만 입력받~~~
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

# ------------------------------------------------------------------------------
# describe(filename)
#   ~~
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


# ------------------------------------------------------------------------------
# histogram(filename)
#   ~~
def ft_histogram(_file_name):
    # data reading
    dataset = ft_read_csv(_file_name)
    data    = dataset[1:, :]
    data    = data[data[:, 1].argsort()]

    # parameter setting
    x       = numpy.array(data[:, 16], dtype=float)
    legend  = ['Grynffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
    title   = dataset[0, 16]
    x_label = "Marks"
    y_label = "Number of student"

    # drawing
    h1 = x[:327]
    h1 = h1[~numpy.isnan(h1)]
    plt.hist(h1, color='red', alpha=0.5)

    h2 = x[327:856]
    h2 = h2[~numpy.isnan(h2)]
    plt.hist(h2, color='yellow', alpha=0.5)

    h3 = x[856:1299]
    h3 = h3[~numpy.isnan(h3)]
    plt.hist(h3, color='blue', alpha=0.5)

    h4 = x[1299:]
    h4 = h4[~numpy.isnan(h4)]
    plt.hist(h4, color='green', alpha=0.5)

    plt.legend(legend, loc='upper right', frameon=False)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
