# GenDiff:


### Tests, coverage and linter status (Статсус тестов):
[![Actions Status](https://github.com/mrjonsonDD/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/mrjonsonDD/python-project-lvl2/actions)
<a href="https://codeclimate.com/github/mrjonsonDD/python-project-lvl2/maintainability"><img src="https://api.codeclimate.com/v1/badges/b087bb49d759b9c571fd/maintainability" /></a>
<a href="https://codeclimate.com/github/mrjonsonDD/python-project-lvl2/test_coverage"><img src="https://api.codeclimate.com/v1/badges/b087bb49d759b9c571fd/test_coverage" /></a>

## Description (Описание):

The gendiff program finds differences in files and outputs them in 3 formats (JSON and YML/YAML).

Программа gendiff находит различия в файлах и выводит их в 3 форматах (JSON и YML/YAML).

## Installation (Установка): 

<ul>$ pip install --user git+https://github.com/mrjonsonDD/python-project-lvl2.git
 
 
 ## Usage (Использование):
 

Running (Вызов):
gendiff --format path/to/file1 path/to/file2

If you need help use the flag:
 
Есть возможность вызвать справку используя флаг:
gendiff -h

Default output format 'stylish', it is also possible to select the output format 'plain' и 'json' use the flag:
 
Формат вывода по умолчанию 'stylish', так же возможно выбрать формат вывода 'plain' и 'json' с помощью флага:
gendiff --format plain
 
 

<ul>-'stylish' output (--format stylish).

 -'plain' text output (--format plain).

 -'json' output (--format json).'.json' and '.yaml'/'.yml'.

'stylish' - default</ul>


## Installation and Running

<ul>$ pip install --user git+https://github.com/mrjonsonDD/python-project-lvl2.git

$ gendiff filepath1 filepath2</ul>

## Optional arguments:
<ul>  
 -f, --format [type]  Output format: 'plain', 'json' or (default: 'stylish')
 -h, --help           output usage information</ul>
  
## Use gendiff:

<a href="https://asciinema.org/a/0xKt7FcteUM12Iyu4xv28JV4E" target="_blank"><img src="https://asciinema.org/a/0xKt7FcteUM12Iyu4xv28JV4E.svg" /></a>

