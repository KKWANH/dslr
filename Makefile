# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kkim <kkim@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/28 12:28:15 by kimkwanho         #+#    #+#              #
#    Updated: 2023/01/05 12:27:29 by kkim             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


TRAIN	= "data/dataset_train.csv"
TEST	= "data/dataset_test.csv"

all:
	@make help

clean:
	@printf "\033[1m\033[31m[Clean]\033[0m\t Remove previous files\n"
	@rm -rf __pycache__
	@rm -rf ft_env
	@rm -rf parameter.dat

setup:
	@printf "\033[1m\033[32m[Setup]\033[0m\t Setting virtual-environment\n"
	@sh "srcs/setup.sh"

env:
	@printf "\033[1m\033[32m[Env]\033[0m\t Running virtual-environment.\n"
	@source "ft_env/bin/activate"
	@printf "\033[1m\033[32m     \033[0m\t If the next path is not in \033[1m\033[96mft_env\033[0m, this means there are some \033[1m\033[91merror\033[0m on this progress.\n"
	@printf "\033[1m\033[32m     \033[0m\t \033[1m\033[4m"
	@which python
	@printf "\033[0m\n"
	@printf "\033[1m\033[32m     \033[0m\t If it doesn't works well, please run [\033[1m\033[4m\033[33msource ft_env/bin/activate\033[0m].\n"

describe:
	@printf "\033[1m\033[34m[Run]\033[0m\t Running the describe.py code\n"
	@python3 "srcs/describe.py" $(TRAIN)

histogram:
	@printf "\033[1m\033[34m[Run]\033[0m\t Running the histogram.py code\n"
	@python3 "srcs/histogram.py" $(TRAIN)

predict:
	@printf "\033[1m\033[34m[Run]\033[0m\t Running the predict.py code\n"
	@python3 "srcs/logreg_predict.py" $(TEST)

train:
	@printf "\033[1m\033[34m[Run]\033[0m\t Running the train.py code\n"
	@python3 "srcs/logreg_train.py" $(TRAIN)

evaluate:
	@printf "\033[1m\033[34m[Run]\033[0m\t Running the evaluate.py code\n"
	@python3 "srcs/logreg_evaluate.py" $(TRAIN)

help:
	@printf "\033[1m\033[33m[Help]\033[0m\t \033[4m\033[1mthere are 5 options.\033[0m\n"
	@printf "\033[1m\033[33m      \033[0m\t \033[31m[make clean]\033[0m    remove pycache, env folder, and parameter.dat\n"
	@printf "\033[1m\033[33m      \033[0m\t \033[32m[make setup]\033[0m    setup the virtual python environment\n"
	@printf "\033[1m\033[33m      \033[0m\t \033[32m[make env]\033[0m      let the python run in the folder ft_env\n"
	@printf "\033[1m\033[33m      \033[0m\t \033[34m[make describe TRAIN=file_name.csv]\033[0m Run describe.py\n"
	@printf "\033[1m\033[33m      \033[0m\t \033[34m[make histogram TRAIN=file_name.csv]\033[0m Run histogram.py\n"
	@printf "\033[1m\033[33m      \033[0m\t \n"
	@printf "\033[1m\033[33m      \033[0m\t We recommend you to execute this project by this order.\n"
	@printf "\033[1m\033[33m      \033[0m\t \033[1m\033[4m\033[31mmake clean\033[0m → \033[1m\033[4m\033[32mmake setup\033[0m → \033[1m\033[4m\033[32mmake env\033[0m → \033[1m\033[4m\033[34mmake read\033[0m → \033[1m\033[4m\033[34mmake train\033[0m → \033[1m\033[4m\033[34mmake read\033[0m\n"