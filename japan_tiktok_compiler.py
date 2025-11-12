import pandas as pd

#This code is used to allow easier encoding of tiktok information for the Japan Trip
#It must create a dataframe with the following details: Region, Activity, Cost, and Link
#The code must also be saved to an excel file for sheets uploading.
#Furthermore, it must be editable for future addition to the compilation
#Lastly, I also want it to be able to create an itinerary for the chosen code. This will use additional time and date variables.

#Let us try to make the function to create or choose an excel file to use
def excel_sheet():
    user_choice=input('\nCreate an excel file [A]\nChoose an excel file [B]\nChoice: ').lower()

    try:
        if user_choice== 'a':
            file_name= input('\nName of file: ')
            file_name = str(file_name) + '.xlsx'
            df_temp = pd.DataFrame(columns=['Location', 'Activity', 'Cost', 'Link'])
            df_temp.to_excel(file_name, index=False) #create excel file
            print(f'\n{file_name} has been created.')
            return file_name

        elif user_choice== 'b':
            file_name= input('\nName of file: ')
            file_name = str(file_name) + '.xlsx'
            print(f'\n{file_name} has been chosen.')
            return file_name
        
        else:
            print('\nInvalid Choice')
            excel_sheet()

    except FileNotFoundError:
        print(f'\n{file_name} was not found in directory.')

    except Exception as e:
        print(f'\nError Occured: {e}.')

#let's get the data from the file
def parse_data(file_name):
    print('\nParsing Data...')
    try:
        df= pd.read_excel(file_name, dtype={'Location':str,'Activity':str,'Cost':float,'Link':str})
        list_of_dicts = df.to_dict(orient='records')
        print('\nParsing Completed.')
        return list_of_dicts
    
    except FileNotFoundError:
        print(f'\n{file_name} was not found in directory.')

    except Exception as e:
        print(f'\nError Occured: {e}.')

#Let us create a class the will cover all the trips
class Trip(object):
    def __init__(self, location, activity, cost, link):
        self.location = str(location).title()
        self.activity = str(activity).title()
        self.cost = cost
        self.link = link

    #This will use the list created from an excel file and append the Trip Object details
    #example use in code: golden_festival.addTrip(list_name)
    #remember to prep the object names from user input (replace spaces with underscore)

    def addTrip(self, list_of_dicts): #changing into list of dicts because appending using DFs is more expensive
            #df.loc[len(df)]= [self.region, self.activity, self.cost, self.link]
            #df.to_excel(file_name)
            
            list_of_dicts= list_of_dicts.append({'Location':self.location, 'Activity':self.activity, 'Cost':self.cost, 'Link':self.link})
            print(f'\nAdded {self.activity} successfuly.')

file_name = excel_sheet()
list_of_dicts= parse_data(file_name)
print(list_of_dicts)