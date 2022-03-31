# Use a Pre-Trained Image Classifier to Identify Dog Breeds
![This is an image taken from the Udacity website](images/udacity_project.png)

This is the first capstone project I worked on while taking the '[AI Programming with Python](https://www.udacity.com/course/ai-programming-python-nanodegree--nd089)' nanodegree at [Udacity](https://www.udacity.com/).

## Project goal
The project goal was to improve our programming skills in Python utilising a *created* image classifier to identify dog breeds. The image classifier used a deep learning model called a **convolutional neural network** (CNN). The CNN that had already learned the features relevant to the identification of dogs from a dataset of 1.2 million images, [ImageNet](https://image-net.org/).  

The main focus of the project was on Python and not on the actual classifier.

## Why an image classifier?
Our city is hosting a citywide dog show and we have volunteered to help the organizing committee with contestant registration. Every participant that registers must submit an image of their dog along with biographical information about their dog. The registration system tags the images based upon the biographical information. Some people are planning on registering pets that aren’t actual dogs. We are asked to use an already developed Python classifier to make sure the participants are dogs.

## Our tasks
Using our Python skills, we had to determine:

➡️ which image classification algorithm among AlexNet, VGG, and ResNet performed the best on classifying images as **dogs** or **not dogs**.

➡️ how well the best classification algorithm worked on correctly identifying a dog's breed.

➡️ how long each algorithm took to solve the classification problem (*runtime*).

## Forecasted difficulties

It is known that certain breeds of dogs look very similar. Udacity warned us about some breeds which can be easily misclassified: Great Pyrenees and Kuvasz, German Shepherd and Malinois, Beagle and Walker Hound, amongst others. It goes without saying that the more images of two similar-looking dog breeds that the algorithm *learns* from, the more likely the algorithm will be able to distinguish between those two breeds.

## Program Outline

1. Time the program
   - Use Time Module to compute program runtime
2. Get program Inputs from the user
   - Use command line arguments to get user inputs
3. Create Pet Images Labels
   - Use the pet images filenames to create labels
   - Store the pet image labels in a data structure (e.g., a dictionary)
4. Create Classifier Labels and Compare Labels
   - Use the Classifier function to classify the images and create the classifier labels
   - Compare Classifier Labels to Pet Image Labels
   - Store Pet Labels, Classifier Labels, and their comparison in a complex data structure (e.g. dictionary of lists)
5. Classifying Labels as "Dogs" or "Not Dogs"
   - Classify all Labels as "Dogs" or "Not Dogs" using dognames.txt file
   - Store new classifications in the complex data structure (e.g. dictionary of lists)
6. Calculate the Results
   - Use Labels and their classifications to determine how well the algorithm worked on classifying images
7. Print the Results

The tasks in 1-7 were to be repeated for each of the three image classification algorithms provided.
