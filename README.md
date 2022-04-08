# Use a Pre-Trained Image Classifier to Identify Dog Breeds
![This is an image taken from the Udacity website](images/udacity_project.png)

This is the first capstone project I worked on while taking the '[AI Programming with Python](https://www.udacity.com/course/ai-programming-python-nanodegree--nd089)' nanodegree at [Udacity](https://www.udacity.com/).

## Project goal
The project goal was to improve our programming skills in Python utilising a *created* image classifier to identify dog breeds. The image classifier used a deep learning model called a **convolutional neural network** (CNN). The CNN that had already learned the features relevant to the identification of dogs from a dataset of 1.2 million images, [ImageNet](https://image-net.org/). The main focus of the project was on Python and not on the actual classifier.

## Languages and tools

<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://pytorch.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pytorch/pytorch-icon.svg" alt="pytorch" width="40" height="40"/> </a> </p>

## Our tasks
Using our Python skills, we had to determine:

➡️ which [Pytorch](https://pytorch.org/) image classification algorithm among AlexNet, VGG, and ResNet performes best on classifying images as **dogs** or **not dogs**.

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

## Results

The total images to classify were 40, 10 of which were not dogs. The three architectures performed as follows:

![This is a table of the results](images/results.png)

### Incorrect dog breed assignments

1- Target: great pyrenees. Classifier: kuvasz. (VGG, AlexNet, ResNet)

2- Target: beagle. Classifier: walker hound, walker foxhound. (VGG, AlexNet, ResNet)

3- Target: beagle. Classifier: english foxhound (AlexNet)

4- Target: boston terrier. Classifier: basenji (AlexNet)

5- Target: golden retriever. Classifier: tibetan mastiff (AlexNet)

6- Target: golden retriever. Classifier: afghan hound (AlexNet)

7- Target: golden retriever. Classifier: leonberg (ResNet)

The only breeds mis-identified by the VGG architecture feature impressive similarities. These were also mis-classified by AlexNet and ResNet. Comparative images are provided below:

![This is an image that compares great pyrenees and kuvaszs](images/dog_comparison1.png)
![This is an image that compares beagles and walker hounds](images/dog_comparison2.png)

A similar mis-classification was done by AlexNet, as illustrated below:

![This is an image that compares beagles and english foxhounds](images/dog_comparison3.png)

Conversely, most mis-classifications done exclusively by AlexNet and/or ResNet were of breeds which shared less distinctive features:

![This is an image that compares golden retrievers and tibetan mastiffs](images/dog_comparison5.png)
![This is an image that compares golden retrievers and afghan hounds](images/dog_comparison6.png)
![This is an image that compares golden retrievers and leonbergs](images/dog_comparison7.png)

While one of the classifications done by AlexNet, which classified a boston terrier as a basenji, was really ill-advised - the two breeds don't even share similar colours.

![This is an image that compares boston terriers and basenjis](images/dog_comparison4.png)

### Comments on the results

Of the three architectures, VGG was by far best in all classification tasks. It indeed classified correctly all 'dogs' vs. 'non dogs', like AlexNet, while ResNet only scored 90% in the identification of 'non dogs'. VGG was also impressive at identifying dog breeds, where it scored 93.33%, and merely mis-indentified two images with very similar breeds (great pyrenees with kuvaszs, and beagles with walker hounds). AlexNet and ResNet made less obvious mistakes, with AlexNet going as far as mis-identifying two dog breeds which don't have similar fur colours.

However, the running time of VGG was considerably greater than those of AlexNet and Resnet: respectively, the three architectures took 35", 6" and 3" to perform the task. I would be curious to test the three architectures on a wider range of images.

## Additional task: Uploading 4 new images to further test the performance of the three architectures

The last task required by the project was selecting and uploading four additional pictures to the program, and test how the architectures perform with them. The requirements were that the images be squares, had a .jpg extension, and featured: one dog whose breed we knew, one animal which was not a dog, one object, and one horizontally-flipped version of the selected dog image. My choices were the following:

**Photo 1, dog (pug):**

![This is an image of a pug](images/Dog_01.jpn)

**Photo 2, cat (maine coon):**

![This is an image of a maine coon](images/Maine_coon_01.jpn)

**Photo 3, coffee mug:**

![This is an image of a coffee mug](images/Coffee_mug_01.jpn)

**Photo 4, horizontally-flipped version of Photo 1:**

![This is a horizontally-flipped version of the image of a pug above](images/Dog_02.jpn)


