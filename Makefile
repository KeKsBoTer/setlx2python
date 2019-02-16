
all: build

build:
	java -jar antlr-4.7.1-complete.jar -Dlanguage=Python3 -o grammar/antlr SetlXgrammar.g4
