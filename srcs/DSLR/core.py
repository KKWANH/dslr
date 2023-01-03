# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    core.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kkim <kkim@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/01/03 16:22:38 by kkim              #+#    #+#              #
#    Updated: 2023/01/03 16:53:59 by kkim             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import csv
import numpy
import matplotlib
import matplotlib.pyplot as plt
from DSLR.math import ft_count

def ft_describe(_file_name):
    dataset = ft_read_csv(_file_name)
    index = dataset[0]
    dataset = dataset[1:, :]
    print(f'{"":15} |{"Count":>12} |{"Mean":>12} |{"Std":>12} |{"Min":>12} |{"25%":>12} |{"50%":>12} |{"75%":>12} |{"Max":>12}')
    for i in range(0, len(index)):
        print(f'{index[i]:15.15}', end=' |')
        try:
            data = numpy.array(dataset[:, i], dtype=float)
            data = data[~numpy.isnan(data)]
            if not data.any():
                raise Exception()
            print(f"{ft_count(data):>12.4f}", end=' |')
            print(f"{ft_count(data):>12.4f}", end=' |')
            print(f"{ft_count(data):>12.4f}", end=' |')
            print(f"{ft_count(data):>12.4f}", end=' |')
            print(f"{ft_count(data):>12.4f}", end=' |')
            print(f"{ft_count(data):>12.4f}", end=' |')
            print(f"{ft_count(data):>12.4f}", end=' |')
            print(f"{ft_count(data):>12.4f}", end=' |')
            print(f"{ft_count(data):>12.4f}")
        except:
            print(f"{ft_count(dataset[:, i]):>12}", end=' |')
            print(f'{"No numerical value to display":>60}')

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