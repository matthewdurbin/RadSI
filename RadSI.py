# -*- coding: utf-8 -*-
"""
Simple command-line interface for a radiactove source inventory
Author: Matthew Durbin
Date: Tue July 07 2020
"""
import fire
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


class RadSI(object):
    """
    RadSI interacts with a saved inventory (inventory.csv) to keep track of 
    source activities via a pandas dataframe. Entries to the inventory can be
    made, and the activity can be predicted now, or at a specified time. 
    halflife.csv acts as a libraty for isotopic half lifes
    """

    def load_inventory():
        """
        Loads "inventory.csv" with the source name as the index, and R_Date
        Column read in as a datetime 
        """
        return pd.read_csv("inventory.csv", index_col=0, parse_dates=["R_Date"])

    def load_halflife():
        """
        Loads "halflife.csv" with the isotope as the index.
        half life values are in seconds
        """
        return pd.read_csv("halflife.csv", index_col=0)

    def elapsed_time(time1, time2):
        """
        Returns the absolute value of the time elapsed between two datetimes
        in units of seconds
        time1 - first datetime
        time2 - second datetime
        """
        elapsed = np.abs(timedelta.total_seconds(time1 - time2))
        return elapsed

    def INVENTORY(self):
        """
        Prints the current invnetory (invetory.csv)
        """
        inventory = RadSI.load_inventory()
        print(inventory)

    def ADD(self, name, isotope, date, activity, unit):
        """
        Adds a new source to the inventory and updates invetory.csv
        name - reference name of a specific source
        isotope - isotope of the source. Format: El-## (element-isotope no)
        date - datetime of referenced activity
        activity - activity of the source at the referenced datetime
        unit - units used for referenced activity
        """
        new = pd.DataFrame(
            [[isotope, date, activity, unit]],
            index=[name],
            columns=["Isotope", "R_Date", "R_Activity", "Unit"],
        )
        inventory = RadSI.load_inventory()
        inventory = inventory.append(new)
        inventory.to_csv("inventory.csv")

    def DELETE(self, name):
        """
        Deletes a source from the inventory and updates invetory.csv
        name - reference name of a specific source
        """
        inventory = RadSI.load_inventory()
        inventory = inventory.drop([name])
        inventory.to_csv("inventory.csv")

    def NOW(self, name):
        """
        Calculates the current source activity based on the halflife and
        time elapsed since calibrated/fererenced activity, in the unites
        of the reference activity
        name - reference name of a specific source in the inventory
        """
        inventory = RadSI.load_inventory()
        halflife = RadSI.load_halflife()
        isotope = inventory.at[name, "Isotope"]
        unit = inventory.at[name, "Unit"]
        time1 = inventory.at[name, "R_Date"]
        time2 = datetime.now()
        delta_t = RadSI.elapsed_time(time1, time2)
        t_hl = halflife.at[isotope, "Half-Life"]
        A_0 = inventory.at[name, "R_Activity"]
        A = A_0 * np.e ** (-delta_t * np.log(2) / t_hl)
        print("The activity of " + name + " is currently:")
        print(A, unit)

    def ON(self, name, date):
        """
        Calculates the source activity at a specified datetime based on the
        half life and time elapsed between the calibrated/referenced activity
        and the specified datetime, in the units of the refernce activity
        name - reference name of a specific source in the inventory
        date - datetime to calculate the activity
        """
        inventory = RadSI.load_inventory()
        halflife = RadSI.load_halflife()
        isotope = inventory.at[name, "Isotope"]
        unit = inventory.at[name, "Unit"]
        time1 = inventory.at[name, "R_Date"]
        time2 = pd.to_datetime(date)
        delta_t = RadSI.elapsed_time(time1, time2)
        t_hl = halflife.at[isotope, "Half-Life"]
        A_0 = inventory.at[name, "R_Activity"]
        A = A_0 * np.e ** (-delta_t * np.log(2) / t_hl)
        print("The activity of " + name + " on " + date + " will be:")
        print(A, unit)

    def PLOT(self, name, date=datetime.now()):
        """
        Makes a plot of the activity of a specified source from the original
        referenced activity, untill the specified datetime.
        name - reference name of a specific source in the inventory
        date - datetime bound to plot the activity. The current datetime is
        usedi if not specified
        """
        inventory = RadSI.load_inventory()
        halflife = RadSI.load_halflife()
        isotope = inventory.at[name, "Isotope"]
        unit = inventory.at[name, "Unit"]
        time_0 = inventory.at[name, "R_Date"]
        time_f = pd.to_datetime(date)
        delta_t = RadSI.elapsed_time(time_0, time_f)
        time = np.linspace(0, delta_t, 100)
        t_hl = halflife.at[isotope, "Half-Life"]
        A_0 = inventory.at[name, "R_Activity"]
        A = A_0 * np.e ** (-time * np.log(2) / t_hl)
        labels = [
            time_0.strftime("%b %d %Y %H:%M"),
            (time_0 + timedelta(0, delta_t / 3)).strftime("%b %d %Y %H:%M"),
            (time_0 + 2 * timedelta(0, delta_t / 3)).strftime("%b %d %Y %H:%M"),
            time_f.strftime("%b %d %Y %H:%M"),
        ]
        plt.plot(time, A, color="black")
        plt.grid()
        plt.ylabel("Activity in " + unit)
        plt.xticks(np.linspace(0, delta_t, 4), labels, rotation=25)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    fire.Fire(RadSI)
