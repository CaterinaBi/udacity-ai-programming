#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: CaterinaBi
# DATE CREATED: 04.04.2022                                 
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Creates list of files in directory
    in_files = listdir(image_dir)
    
    # The code below processes each of the files to create a dictionary where the key
    # is the filename and the value is the picture label
 
    # Creates empty dictionary that will be returned by the function
    results_dic = dict()
   
    # Processes through each file in the directory, extracting only the words
    # that contain the pet image label
    for idx in range(0, len(in_files), 1):
       
       # Skips file if starts with '.', i.e., it isn't a pet image file
       if in_files[idx][0] != ".":
              
          # Uses split() to extract words of filename into list image_name
          image_name = in_files[idx].split("_")
              
          # Creates temporary label variable to hold pet label name extracted 
          pet_label = ""

          # Loops to check if word in pet name is only alphabetic characters
          # If true: appends word to pet_label separated by space 
          for word in image_name:
              if word.isalpha(): 
                # Adds whitespace between two words
                pet_label += word.lower() + " "
          # Strips off ending whitespace character in newly-created label
          pet_label = pet_label.rstrip()

       # If filename doesn't already exist in dictionary: adds it and its pet label
       # Else: prints an error message indicating duplicate files
       if in_files[idx] not in results_dic:
            results_dic[in_files[idx]] = [pet_label]
   
       else:
            print("** Warning: Duplicate files exist in directory:",in_files[idx])
                
    #Iterates through a dictionary and prints all keys + their associated values
    print("\nAll key-value pairs in dictionary results_dic are as follows:\n")
    for key in results_dic:
          print("Filename=", key, "   Pet Label=", results_dic[key][0])
    
    # Returns dictionary created within the function
    return results_dic
