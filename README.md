# Orbitals

This is an example python project that contains utilities to encode and solve differential equations.

The project currently contains modules for solving the Newton equation of motion for a particle in a gravitational field, either with an Euler or a Runge-Kutta method.

## Installation

Dependencies are handled with conda, you can install them with:
```sh
conda env create
```
Then activate the environment with
```sh
conda activate orbitals-env
```
The project can then be installed with pip:
```sh
pip install -e .
```
The `-e` flag is for editable, so you can modify the source code and the changes will be reflected in the installed package.

## Tests

You can run the tests with pytest by running the following command in the root directory of the project:
```sh
pytest -v
```

## Usage

An usage example notebook is provided under `examples/`.


## Contributors


-sophia 
- Álvaro