import requests
import json
import string
from math import sqrt
from pathlib import Path
from statistics import mean
from tempfile import TemporaryDirectory
from PIL import Image

# The threshold at which the function will consider the colours as equivalent
# Lower value = more precise
COLOUR_DIFFERENCE_THRESHOLD = 5.0

def calcColourDifference(rgb1:tuple, rgb2:tuple) -> float:
    '''
    Calculates the absolute difference between two colours using pythagoras

    Arguments:
        rgb1:tuple - The first colour to compare as a 3-dimensional tuple
        rgb2:tuple - The second colour to compare as a 3-dimensional tuple
    
    Returns:
        distance:float - the distance between the two colours
    '''
    dist_r = rgb1[0] - rgb2[0]
    dist_g = rgb1[1] - rgb2[1]
    dist_b = rgb1[2] - rgb2[2]
    return sqrt((dist_r * dist_r) + (dist_g * dist_g) + (dist_b * dist_b))

def matchColour(imageFilename:Path, references:dict) -> string:
    '''
    Perform the colour match using the average colour of the four corners of the image.

    Arguments:
        imageFilename:Path - Path to where the image is stored
        references: dict   - A dict that defines the reference colours to look at
    
    Returns:
        name:string - name of the matching colour
    
    Raises:
        RuntimeError if no colours match
    '''    
    # Open and load image
    with Image.open(imageFilename) as img:
        pix = img.load()

    # Get the co-ordinates of the four corners of the image
    corner_top_left = 0,0
    corner_top_right = img.width - 1,0
    corner_btm_left = 0, img.height - 1
    corner_btm_right = img.width - 1, img.height - 1
    points_to_check = [corner_top_left, corner_btm_left,
                        corner_btm_right, corner_top_right]

    # Get the pixels from the co-ordinates 
    pixels = [pix[point] for point in points_to_check]

    # Average the RGB values
    rgb = (mean(pixel[0] for pixel in pixels),
            mean(pixel[1] for pixel in pixels),
            mean(pixel[2] for pixel in pixels))
    
    # Work out which colour is matched
    for ref in references:
        referenceRgb = (ref['r'], ref['g'], ref['b'])
        if calcColourDifference(rgb, referenceRgb) < COLOUR_DIFFERENCE_THRESHOLD:
            return ref['name']
    
    # No colour has been matched - throw error
    raise RuntimeError('Does not match any colour in the references.')

def downloadImage(url:string, path:Path):
    '''
    Generic function to download an image to a location on the disk.

        Arguments:
            url:string - URL to attempt to download
            path:Path  - path of where to save the file

        Raises:
            HTTPError if unable to get the file
    '''
    res = requests.get(url)
    if res.status_code != 200:
        raise requests.HTTPError("Unable to get the image from the provided URL.")
    with open(path,'wb') as file:
        file.write(res.content)

def matchColourFromUrl(url:string, referencesPath:string) -> string:
    ''' 
    Downloads an image to a temp directory and performs the colour match 

    Arguments:
        url:string - URL of the image to colour match
        referencesPath:string - path to the JSON file that defines the reference colours

    returns:
        string - name of closest matching colour
    '''
    # Get colour references from configuration file
    with open(referencesPath) as refFile:
        references = json.load(refFile)
    
    # Download the image and store it in a temporary file.
    with TemporaryDirectory() as tempdir:
        imageFilename = Path(tempdir,'image')
        downloadImage(url, imageFilename)
        
        # Perform the colour match and return 
        colourMatchResult = matchColour(imageFilename, references)   
        return json.dumps ({'result':colourMatchResult, 'statusCode':200})