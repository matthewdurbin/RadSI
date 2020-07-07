# RadSI - The Radiation Source Inventory

RadSI is a simple CLI method of tracking the activities in your inventory of radioactive sources.

![RadSI_Demo](RadSI_Demo.PNG)

## Motivation 
As is often the case, each source in a lab or hospital setting gets some sort of binder or massive chart that contains pages of look up tables. Thus to get the activity of a specific source, one has to find the binder or the chart and search through untill you find the right cell that gives you the activity of your source at a specific time.

If you add a new source to your inventory, you have to make a new binder. If you don't have the time you need in the look up table, you have to do some manual interpolation of full calculation to get what you need.

RadSI provides a more automated approach, in which you simply enter the source in your logged inventory and your activity is calculated - down to second if need be!

## Quick Documentation 
In addition to RadSI.py, there are two important documents:

inventory.csv - This file is your inventory of radiation sources. It can be edited directly, or through the command ADD and DELETE. It contains the following columns:  
        index       - this is the "nick name" of your specific sourc (Ex: medical1)  
        Isotope     - this is the isotope of your source, written as the elements initals dash mass number (Ex: Co-60)  
        R_Date      - this is the datetime at which your referenced activity was determined, written as day-month-year-hour:minute:second though not all timing info is needed.   (Ex: 12-7-2019-12:30:00)  
        R_Activity  - this is the activity of your source at the referenced date time (Ex: 30)  
        Unit        - this is the units of activity for your source (Ex: mCi) 
        
                
halflife.csv - This file is the library of isotopes and their halflifes in seconds. It can be edited directly. 

### Commands:

INVENTORY - this simply prints the current inventory

ADD - This adds a source to the inventory and updates inventory.csv. The paramaters are:  
        name       - this is the "nick name" of your specific sourc (Ex: medical1)  
        Isotope     - this is the isotope of your source, written as the elements initals dash mass number (Ex: Co-60)  
        R_Date      - this is the datetime at which your referenced activity was determined, written as day-month-year-hour:minute:second though not all timing info is needed. (Ex: 12-7-2019-12:30:00)  
        R_Activity  - this is the activity of your source at the referenced date time (Ex: 30)  
        Unit        - this is the units of activity for your source (Ex: mCi)  
        
DELETE - this deletes a source from the inventory and updates invetory.csv. The parameter is:
        name       - this is the "nick name" of your specific sourc (Ex: medical1)  
        
NOW - this calculates the current activity of the specified source. The paramter is:
        name       - this is the "nick name" of your specific sourc (Ex: medical1)  
        
ON - this calculates the activity of the specified source on a specified datetime. The parameters are:
        name       - this is the "nick name" of your specific sourc (Ex: medical1)
        date       - this is the datetime at which you wish to calculate the activity of the specified source
   
