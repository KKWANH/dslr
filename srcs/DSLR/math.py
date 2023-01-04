# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    math.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kkim <kkim@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/01/03 16:44:47 by kkim              #+#    #+#              #
#    Updated: 2023/01/04 14:22:06 by kkim             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# ------------------------------------------------------------------------------
# import : library
import numpy

# ------------------------------------------------------------------------------
# sum of xs
def ft_sum(_x):
    rst = 0
    for x in _x:
        if numpy.isnan(x):
            continue
        rst = rst + x
    return rst

# count of xs
def ft_count(_x):
    try:
        _x = _x.astype('float')
        _x = _x[~numpy.isnan(_x)]
        return len(_x)
    except:
        return len(_x)

# average of xs
def ft_mean(_x):
    return (ft_sum(_x) / len(_x))

# standard deviation of xs
def ft_std(_x):
    mean = ft_mean(_x)
    total = 0
    for x in _x:
        if numpy.isnan(x):
            continue
        total = total + (x - mean) ** 2
    return (total / ft_count(_x)) ** 0.5

# minimum of xs
def ft_min(_x):
    min = _x[0]
    for x in _x:
        value = x
        if value < min:
            min = value
    return min

# maximum of xs
def ft_max(_x):
    max = _x[0]
    for x in _x:
        value = x
        if value < max:
            max = value
    return max

# certain percentile of xs
def ft_percentile(_x, _p):
    _x.sort()
    k = (len(_x) - 1) * (_p / 100)
    f = numpy.floor(k)
    c = numpy.ceil(k)

    if f == c:
        return _x[int(k)]
    
    d0 = _x[int(f)] * (c - k)
    d1 = _x[int(c)] * (k - f)
    return d0 + d1
