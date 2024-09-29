# Legged-Locomotion


# DCM Bipedal Locomotion
This repository contains an environment for the first mini-project.

## Installation

Recommend using a virtualenv (or conda) with python3.6 or higher. After installing virtualenv with pip, this can be done as follows:

`virtualenv {leg_env, or choose another name venv_name} --python=python3`

To activate the virtualenv: 

`source {PATH_TO_VENV}/bin/activate` 

Your command prompt should now look like: 

`(venv_name) user@pc:path$`

The repository depends on recent versions of pybullet, numpy, etc. as described on moodle. 


## Additional dependency
install qp solver library based on the follwoing link:
https://qpsolvers.github.io/qpsolvers/installation.html

Fro example for the Python 3.8.10 (in th UBUNTU 20.04) the following command works:
`pip install qpsolvers`

For testing that it installed properly, run the following code:
`python qp.py`

You sould see the following output:
`QP solution: x = [ 0.3076548  -0.69232615  1.38448776]`

## Code resources
- The [PyBullet Quickstart Guide](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/edit#heading=h.2ye70wns7io3) is the current up-to-date documentation for interfacing with the simulation. 
 

## Using code
- First activate the python virtual environment.
- Run `jupyter notebook` and open the DCM-Locomotion.ipynb
