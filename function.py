import os
import csv

#Usefull methods
class Um():

    def create_csv(self,fname,path):
        """
        Method that creates a csv file if not exits
        where path is path of the working directory | dtype is <str> | try using os.getcwd() to get the path
        and fname is the filanme | dtype is <str>
        """
        if not fname in os.listdir(path):
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
        """
        with open(os.path.join(path,fname), 'a',newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(data) 