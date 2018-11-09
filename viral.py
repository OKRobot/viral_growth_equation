import sys
import argparse
import numpy as np
import math

import matplotlib
import matplotlib.pyplot as plt

def parse_arguments():
    # Command-line flags are defined here.
    parser = argparse.ArgumentParser()
    parser.add_argument('--i', dest='invitations', type=int,
                        default=2, help="Invitations sent per new user.")
    parser.add_argument('--conv', dest='conversion_rate', type=float,
                        default=0.25, help="The chance an invitation will convert a new user")
    parser.add_argument('--ct', dest='cycle_time', type=float,
                        default=5, help="The cycle time in days")
    parser.add_argument('--starting-users', dest='starting_users', type=int,
                        default=2, help="The number of new users at cycle 0.")
    parser.add_argument('--days', dest='days', type=int,
                        default=50, help="The number of days to plot")


    return parser.parse_args()

def main(args):
    # Parse command-line arguments.
    args = parse_arguments()
    invites = args.invitations
    conv = args.conversion_rate
    ct = args.cycle_time
    starting_users = args.starting_users
    days = args.days

    k = invites*conv
    max_cycles = math.floor(days/ct) + 1
    user_t = np.zeros(max_cycles) 
    day_t = np.linspace(0,days,num=max_cycles)

    for ix in range(max_cycles):
        if ix == 0:
            users = starting_users
        else:
            users = round(users*k)
        user_t[ix] = users

    plt.title("New users over time with i={}, conv={}, ct={}".format(invites,conv,ct))
    plt.xlabel("Days")
    plt.ylabel("New users")


    plt.plot(day_t, user_t)
    plt.show()


if __name__ == '__main__':
    main(sys.argv)
