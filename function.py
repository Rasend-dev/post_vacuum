import os
import csv
<<<<<<< HEAD
=======
from datetime import datetime

CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
>>>>>>> hotfix

#Usefull methods
class Um():

    def create_csv(self,fname,path):
        """
        Method that creates a csv file if not exits
        where path is path of the working directory | dtype is <str> | try using os.getcwd() to get the path
        and fname is the filanme | dtype is <str>
        """
<<<<<<< HEAD
        if not fname in os.listdir(path):
=======
        fname = fname + '_' + CURRENT_DATE + '.csv'
        if not fname in os.listdir(path): # if there is no file in the folder it create it
>>>>>>> hotfix
           with open(os.path.join(path, fname), 'w') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(['link','n_likes','n_comments']) 

        else:
            with open(os.path.join(path, fname), 'w') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(['link','n_likes','n_comments']) 
    
    def write_csv(self,fname,path,data):
        """
        Method that write the data in the csv file
        where path is path of the working directory | dtype is <str> | try using os.getcwd() to get the path
        and fname is the filanme | dtype is <str>
<<<<<<< HEAD
        """
        with open(os.path.join(path,fname), 'a',newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(data) 
        pass
=======
        and data is an array that contains the data we wanna write | dtype is <list>
        """
        fname = fname + '_' + CURRENT_DATE + '.csv'
        with open(os.path.join(path,fname), 'a',newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(data) 
>>>>>>> hotfix
