
all: build test

build:
	java -jar antlr-4.7.1-complete.jar -Dlanguage=Python3 -o grammar/setlx/antlr SetlXgrammar.g4

test:
	python3 test.py tests/$(name).stlx