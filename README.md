### Hexlet tests and linter status:
[![Actions Status](https://github.com/VitalRusinov/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/VitalRusinov/python-project-50/actions)

### GitActions tests and lint status

[![Python CI](https://github.com/VitalRusinov/python-project-50/actions/workflows/python-ci.yml/badge.svg)](https://github.com/VitalRusinov/python-project-50/actions/workflows/python-ci.yml)

### SonarCloud Tests Coverage status

[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=VitalRusinov_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=VitalRusinov_python-project-50)

This **package** is a CLI, which allows user **to parse** two different datas from files in three formats.

Types of files allowed:

- *.json* files;
- *.yaml* or *.yml* files;

#### FAQ

Install the package

```
git clone https://github.com/VitalRusinov/python-project-50.git
cd python-project-50
make install
make link
```

Start the programm with

```
gendiff [-h] [-f] *needed format* tests/fixtures/YOUR-FILE1 tests/fixtures/YOUR-FILE2
```

Below you can see the examples of using the parser.

#### Parsing float JSON-files

[![asciicast](https://asciinema.org/a/632924.svg)](https://asciinema.org/a/632924)

#### Parsing float YAML-files

[![asciicast](https://asciinema.org/a/633254.svg)](https://asciinema.org/a/633254)

#### Parsing trees

[![asciicast](https://asciinema.org/a/634501.svg)](https://asciinema.org/a/634501)

#### PLAIN format for trees

[![asciicast](https://asciinema.org/a/634774.svg)](https://asciinema.org/a/634774)

#### JSON format for trees

[![asciicast](https://asciinema.org/a/635456.svg)](https://asciinema.org/a/635456)