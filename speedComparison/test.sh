#!/bin/bash

   for i in *.py; do 
      tput setaf 2
      echo -e  "\n$i"
      tput sgr0
      python3 $i || python $i
   done
