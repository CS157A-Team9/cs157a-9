# cs157a-9
CS157A Team #9 project

## Project Proposal
https://docs.google.com/document/d/1cPT1TBGzdlqpoYTMWRF7JZ2daHiAtQl9f8OHPTmBvnM/edit?usp=sharing

## Project Requirements
https://docs.google.com/document/d/1ilFfwDIK17xxILQx0scwFLeDIWO_rgJXE4wsyqgTEao/edit?usp=sharing

# Development Guide

## System Dependencies
| Name   | Version |
|--------|---------|
| Apache | *       |
| MySQL  | 8       |
| Python | 3       |
| Pipenv | *       |

\* No specific version requirement

## Installation (Mac)

### Homebrew
Homebrew is a package manager for Mac which will be used to install the necessary software for this project.

Ensure command line tools are installed by running the following in your terminal
```
--xcode-select --install
```

Run the following to install Homebrew on your system
```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### Python 3
Install python 3 via Homebrew
```
brew install python
```

### Pipenv
Pipenv helps to manage the python virtual environment as well as python dependencies.
Install via Homebrew
```
brew install pipenv
```

## Getting Started
Once all system dependencies have been installed, install python dependencies with pipenv
```
pipenv install
```

To activate the virtual environment run `pipenv shell` from the command line. You can exit the shell with `exit`. Once in the shell, the django commands can be readily accessed.
