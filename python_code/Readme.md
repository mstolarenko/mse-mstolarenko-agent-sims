# Python Code Read.me<BR>
**Here are some basic instructions to run the code for each question in Part 1.**

## Part 1.1<BR>
Directions for running the Von Neumann and Moore parameters:
- For the Moore Neighborhood: No changes are needed. The Moore argument is already set to 'True'
- For the Von Nueomann Neighborhood:  In [agent.py](https://github.com/IDS6145-Fall2022/assignment3-abm-mstolarenko/blob/main/python_code/mesa-main/examples/forest_fire/forest_fire/agent.py), change the 'True' Statement in line 33 to 'False.'<BR>

## Part 1.2<BR>
Directions for changing the rate of spread in a Von Neumann neighborhood:<BR>
1. Modify the 'True' statement to 'False' in [agent.py](https://github.com/IDS6145-Fall2022/assignment3-abm-mstolarenko/blob/main/python_code/mesa-main/examples/forest_fire/forest_fire/agent.py) line 33 to define a Von Neumann neighborhood
2. Modify the spread rate at the end of line 33 in the same file. It is currently set to a spread rate of 1. Change the number to 2 and 4, respectively.

## Part 1.3<BR>
All three images use the RBG parameter g > 60, change filename directory to respective images:
1. hunters.jpg
2. eggman.jpg
3. sus.jpg<BR>

## Part 1.4<BR>
Directions for changing the initial burn points:
- Adjust the "if x == 0:" line in [model.py](https://github.com/IDS6145-Fall2022/assignment3-abm-mstolarenko/blob/main/python_code/mesa-main/examples/forest_fire/forest_fire/model.py) to a specific (x,y) point.
- Duplicate the "if x == 0:" line for additional initial burn locations<BR>

## Part 1.5<BR>
1. St. Louis, Missouri (st-louis.png) uses the parameters g > 50 and b < 40 at initial burn point (x,y) = (70, 10)
2. Chicago, Illinois (chicago.png) uses the parameters g > 45 and b < 50 at initial burn point (x,y) = (10, 80)
3. Seattle, Washington (washington.png) uses the parameters g > 45 and b < 48 with an initial burn point (x,y) = (18,25)

## Part 1.6<BR>
Directions and parameters for running different forest fire scenarios:
1. St. Louis, Missouri (st-louis-bl.png) uses the parameters g > 50 and b < 40 at initial burn point (x,y) = (70,10)
2. Chicago, Illinois (chicago-bl.png) uses the parameters g > 45 and b < 50 at initial burn point (x,y) = (10, 80)
3. Seattle, Washington (seattle-bl.png) uses the parameters g > 45 and b < 48 with an initial burn point (x,y) = (18,25)
