#!/bin/bash

##########################################################################################
# How to use: https://github.com/wmatyskiewicz/workspace/wiki/Python-Virtual-Environment #
##########################################################################################

# Configuration
package[0]="bpython" # bpython is a fancy interface to the Python interpreter for Unix-like operating systems.
package[1]="pdbpp" # pdb++, a drop-in replacement for pdb
package[2]="pep8" # pep8 is a tool to check your Python code against some of the style conventions in PEP 8.

# Create a virtual environment
echo -e "\n"
echo -e "\033[32m --------------------------------------------------------------------------------\e[00m"
echo -e "\033[32m Creating a virtual environment\e[00m"
echo -e "\033[32m --------------------------------------------------------------------------------\e[00m"

virtualenv . --distribute --no-site-packages
source bin/activate
mkdir project

# Instaling packages
for ((i=0; i<${#package[*]}; i++)) 
do
  echo -e "\033[32m -------------------------------------------------------------------------------\e[00m"
  echo -e "\033[32m Instaling ${package[$i]}...\e[00m"
  echo -e "\033[32m -------------------------------------------------------------------------------\e[00m"
  pip install ${package[$1]}
  echo "\n"
done

deactivate
