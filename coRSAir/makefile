INC = /Users/preina-g/.brew/opt/openssl@3/include
LIB = /Users/preina-g/.brew/opt/openssl@3/lib
CFLAGS = -Werror -Wall -Wextra -Wno-deprecated-declarations
NAME = corsair

RED		=	\033[0;31m
RESET	= 	\033[0m

all: corsair

corsair: corsair.o
	gcc corsair.o -L$(LIB) -lssl -lcrypto -o corsair -g

corsair.o: corsair.c
	gcc -c corsair.c $(CFLAGS) -I$(INC) -o corsair.o -g

clean:
	@echo "$(RED)Cleaning$(RESET)"
	@rm -rf $(NAME) corsair.o 

fclean: clean
	@echo "$(RED)Removing: $(NAME)$(RESET)"
	@echo "$(RED)Removing: corsair.o$(RESET)"


re:
	@$(MAKE) fclean
	@$(MAKE) all

generate:
	python3 generate.py

.PHONY: all clean fclean re