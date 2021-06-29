# Python Dependency management

We use pip-tools for dependency management.

## Steps to use

Create a file <name>.in file and list all the dependencies in that. Typically we will have `requirements-base.in` which contains all packages required for the project and `requirements-dev.in` which contains all the dev dependencies like formatter, linter etc.

Then run the following command to generate the requirements-\*.txt file(s).

```sh
pip-compile requirements-dev.in
pip-compile requirements-base.in
```

## Installing in virtual environment

Create a virtual environment Refer [venv](./create-venv.md). Then install using

```
pip install -r requirements-dev.txt
pip install -r requirements-base.txt
```

We can create the following shell command to ease the work,

```sh

function install() {
  if [[ "$1" == 'dev' ]]
  then
    echo "installing *.base.in"
    pip-compile requirements-base.in
    pip install -r requirements-base.txt
  else
  echo "installing *.dev.in"
    pip-compile requirements-dev.in
    pip install -r requirements-dev.txt
  fi
}
```
