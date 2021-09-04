import os
import csv
from datetime import datetime
import json

CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")

#Usefull methods
class Um():

    def create_csv(self,fname,path):
        """
        Method that creates a csv file if not exits
        where path is path of the working directory | dtype is <str> | try using os.getcwd() to get the path
        and fname is the filanme | dtype is <str>
        """
        fname = fname + '_' + CURRENT_DATE + '.csv'
        if not fname in os.listdir(path): # if there is no file in the folder it create it
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
        and data is an array that contains the data we wanna write | dtype is <list>
        """
        fname = fname + '_' + CURRENT_DATE + '.csv'
        with open(os.path.join(path,fname), 'a',newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(data) 

    def create_json(self,fname,path):  
        """
        Method that creates a json file if not exits
        where path is path of the working directory | dtype is <str> | try using os.getcwd() to get the path
        and fname is the filanme | dtype is <str>
        """  
        dictionary ={'post_details':[]} 
        fname = fname + '_' + CURRENT_DATE + '.json'
        if not fname in os.listdir(path):
            with open(os.path.join(path,fname), "w") as outfile:
                json.dump(dictionary, outfile)
        else:
            with open(os.path.join(path,fname),"w") as outfile:
                json.dump(dictionary,outfile)
 

    def write_json(self,fname,path,info): 
        """
        Method that write the data in the json file
        where path is path of the working directory | dtype is <str> | try using os.getcwd() to get the path
        and fname is the filanme | dtype is <str>
        and info is an dictionary that contains the data we wanna write | dtype is <dict>
        """
        fname = fname + '_' + CURRENT_DATE + '.json'
        with open(os.path.join(path,fname), 'r+') as f:
            data = json.load(f)
            data['post_details'].append(info)
            f.seek(0)
            json.dump(data,f)
