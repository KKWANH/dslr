# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kkim <kkim@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/28 12:28:15 by kimkwanho         #+#    #+#              #
#    Updated: 2023/01/06 15:03:50 by kkim             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

all:
	@make help

clean:
	@printf "\033[1m\033[31m[Clean]\033[0m\t Remove previous files\n"
	@rm -rf __pycache__
	@rm -rf ft_env
	@rm -rf parameter.dat
	@rm -rf houses.csv
	@rm -rf wb.dat

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

FILE = "data/dataset_train.csv"
describe:
	@printf "\033[1m\033[34m[Run]\033[0m\t Running the describe.py code.\n"
	@printf "\033[1m\033[34m     \033[0m\t You can change input [.csv] file with [FILE='data/dataset_train.csv'].\n"
	@python3 "srcs/describe.py" $(FILE)

FILE = "data/dataset_train.csv"
INDEX = "Arithmancy"
histogram:
	@printf "\033[1m\033[34m[Run]\033[0m\t Running the histogram.py code\n"
	@printf "\033[1m\033[34m     \033[0m\t We recommend you to run the index: \033[31m6\033[0m(Arithmancy), \033[31m15\033[0m(Potions), \033[31m16\033[0m(Care of magical creatures).\n"
	@printf "\033[1m\033[34m     \033[0m\t You can change input [\033[1m\033[4m\033[32m.csv\033[0m] file like [\033[1m\033[4m\033[33mFILE='data/dataset_train.csv'\033[0m].\n"
	@printf "\033[1m\033[34m     \033[0m\t You can change input [\033[1m\033[4m\033[32mindex\033[0m] number like [\033[1m\033[4m\033[33mINDEX='6' or INDEX='Arithmancy'\033[0m].\n"
	@python3 "srcs/histogram.py" $(FILE) $(INDEX)

FILE = "data/dataset_train.csv"
scatter_plot:
	@printf "\033[1m\033[34m[Run]\033[0m\t Running the scatter_plot.py code\n"
	@printf "\033[1m\033[34m     \033[0m\t You can change input [.csv] file with [FILE='data/dataset_train.csv'].\n"
	@python3 "srcs/scatter_plot.py" $(FILE)

FILE = "data/dataset_train.csv"
pair_plot:
	@printf "\033[1m\033[34m[Run]\033[0m\t Running the pair_plot.py code\n"
	@printf "\033[1m\033[34m     \033[0m\t You can change input [.csv] file with [FILE='data/dataset_train.csv'].\n"
	@python3 "srcs/pair_plot.py" $(FILE)

PREDICT = "data/dataset_test.csv"
predict:
	@printf "\033[1m\033[34m[Run]\033[0m\t Running the predict.py code\n"
	@printf "\033[1m\033[34m     \033[0m\t You can change input [.csv] file with [PREDICT='data/dataset_test.csv'].\n"
	@python3 "srcs/logreg_predict.py" $(PREDICT)

FILE = "data/dataset_train.csv"
train:
	@printf "\033[1m\033[34m[Run]\033[0m\t Running the train.py code\n"
	@printf "\033[1m\033[34m     \033[0m\t You can change input [.csv] file with [FILE='data/dataset_train.csv'].\n"
	@python3 "srcs/logreg_train.py" $(FILE)

FILE = "data/dataset_train.csv"
evaluate:
	@printf "\033[1m\033[34m[Run]\033[0m\t Running the evaluate.py code\n"
	@printf "\033[1m\033[34m     \033[0m\t You can change input [.csv] file with [FILE='data/dataset_train.csv'].\n"
	@python3 "srcs/logreg_evaluate.py" $(FILE)

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