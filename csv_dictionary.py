#Code to convert csv items into a list of dictionaries

from csv import DictReader                              #Used to add values and read values from a csv fil

#Function to take CSV and make a list of dictionaries
def csv_to_dictionary_list():
    global story_keyword

    with open('stories_keywords.csv', 'r') as read_obj:
        # pass the file object to DictReader() to get the DictReader object
        dict_reader = DictReader(read_obj)
        # get a list of dictionaries from dct_reader
        story_keyword = list(dict_reader)
        # print list of dict i.e. rows
        print(story_keyword)

        #Returns list of dictionaries
        return story_keyword
