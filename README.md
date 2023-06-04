# Evilsgt-Image-Maps


### Arguments:
- The client wants to extract island data from OpenStreetMap API and create an active
contour model from it.
- The active contour model will be used to classify satellite images of the island and
identify its name.
- the client wants to create a dataset for the island using the active contour model.
- The dataset will contain multiple versions of the active contour model at different
rotations.
- By creating a dataset that contains multiple versions of the active contour model at
different rotations, the client will be able to classify images of the island regardless of
their orientation.

### Objectives:
-Extract island data from OpenStreetMap API. 
-Create an active contour model from the island data.
-Use the active contour model to classify satellite images of the island and identify its name. 
-Create a dataset for the island using the active contour model. 

### Requirements:
- Access to OpenStreetMap API data.
- An algorithm for extracting the coastline nodes of the island from OpenStreetMap data.
- An algorithm for creating an active contour model from the coastline nodes.
- Iterative closest point (ICP)” method for calculating the similarity.
- A method for creating a dataset for the island using the active contour model.

### Proposed Solution:

Here's a possible solution for the client's problem:
1. Extract OpenStreetMap data for the island(s) of interest.
2. Develop an algorithm for extracting the coastline nodes of the island from
OpenStreetMap data.
3. Use the extracted coastline nodes to create an active contour model of the island using an
algorithm such as the "snake" model.
4. Develop an algorithm to determine similarity between given sample and islands already
in the dataset.
5. Create a dataset for the island by rotating the active contour model at different angles and
extracting the corresponding list of nodes. This will produce multiple versions of the
active contour model in different rotations, which can be used to train the machine
learning algorithm.
6. Train the machine learning algorithm using the dataset and test it on a separate set of
images to evaluate its performance.
7. Once the algorithm is sufficiently accurate, use it to classify images of the island and
identify its name



### DEMO VIDEO
https://github.com/thehamzza/Evilsgt-Image-Maps/assets/45312947/12d6f35d-b606-440f-abeb-98c640c1b0d0




