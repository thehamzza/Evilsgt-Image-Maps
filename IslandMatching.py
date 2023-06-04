import numpy as np
from skimage.color import rgb2gray
from skimage import  io
from skimage.filters import gaussian, threshold_otsu
from skimage.segmentation import active_contour
import pandas as pd

def getContour(image: str):
    image = rgb2gray(image)

    thresh = threshold_otsu(image)
    image = image > thresh

    radius = min(image.shape[0], image.shape[1]) // 2

    s = np.linspace(0, 2*np.pi, 400)
    r = image.shape[0]//2 + radius*np.sin(s)
    c = image.shape[1]//2 + radius*np.cos(s)
    init = np.array([r, c]).T

    snake = active_contour(gaussian(image, 3, preserve_range=False), init, alpha=0.015, beta=0.01, gamma=0.01)
    return snake

def append():
    # Ask the user for an image 
    img_path = input("Enter the path to the image: ")

    # Ask the user for the name of the island
    island_name = input("Enter the name of the island: ")

    # Extract contours and save them
    snake = getContour(image = io.imread(img_path))

    df = None
    try:
        df = pd.read_pickle("island_database.csv")
        df.loc[len(df.index)] = [snake, island_name] 
    except:
        df = pd.DataFrame({
            "contour": [snake],
            "name": [island_name]
        })
        
    df.to_pickle("island_database.csv")
    
def match():
    df = pd.read_pickle("island_database.csv")
    from skimage.transform import rotate


    image_pth = input("Enter the path of the unknown island image: ")
    image = io.imread(image_pth)

    # Creating 36 rotations of the image, one with a 10 degree rotation
    rotated_images = []
    for i in range(37):
        rotated_images.append(rotate(image, i*10))
        
    # Getting contours for said rotations
    rotated_contours = []
    for i in range(len(rotated_images)):
        rotated_contours.append(getContour(rotated_images[i]))
        print(i+1)
        
    df2 = pd.DataFrame({
        "rotated_contours": rotated_contours
    })
    
    len_df = len(df)
    df = pd.concat([df]*len(df2),ignore_index=True)
    df2 = pd.concat([df2]*len_df,ignore_index=True)
    
    distances = [np.linalg.norm(df["contour"].values[x] - df2["rotated_contours"].values[x]) for x in range(len(df))]
    island_name_prediction = df["name"].values[distances.index(min(distances))]
    
    print(f"The island appears to be: {island_name_prediction}")
    
while True:
    input_option = input("Which mode to choose? append(a) or match(m) or quit(q): ")
    if input_option.lower() == "a":
        append()
    elif input_option.lower() == "m":
        match()
    elif input_option.lower() == "q":
        break
    else:
        print("Invalid input!")

    