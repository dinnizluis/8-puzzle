#!/bin/bash
in=1,2,3,4,0,5,6,7,8
cd __pycache__
out=`python board_class.cpython-36.pyc $in`
echo $out