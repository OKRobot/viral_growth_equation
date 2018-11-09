# The viral growth equation
Requires Python3 packages: numpy, matplotlib, pyplot, argparse

## How to run
* clone or download the repository
* navigate to the root folder
* Use the following instruction:
* python3 viral.py

## command line arguments
* i = invitations sent per user, default = 2
* conv = conversion rate of invitation recipient, default = 0.25
* ct = cycle time in days, default = 5
* starting-users = the number of users at cycle 0, default = 2
* days = the number of days to plot, default = 50

## example with all arguments
python3 viral.py --i 5 --conv 0.6 --ct 8 --starting-users 3 --days 40

