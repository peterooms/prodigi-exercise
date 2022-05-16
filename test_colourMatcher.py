import json
import pytest
from requests import HTTPError
from colourMatcher import matchColourFromUrl

# 'Good' samples
SAMPLE_IMAGE_BLACK = "https://pwintyimages.blob.core.windows.net/samples/stars/test-sample-black.png"
SAMPLE_IMAGE_GREY = "https://pwintyimages.blob.core.windows.net/samples/stars/test-sample-grey.png"
SAMPLE_IMAGE_TEAL = "https://pwintyimages.blob.core.windows.net/samples/stars/test-sample-teal.png"
SAMPLE_IMAGE_NAVY = "https://pwintyimages.blob.core.windows.net/samples/stars/test-sample-navy.png"

# 'Bad' samples
SAMPLE_BAD_URL = "https://pwintyimages.blob.core.windows.net/samples/stars/this-file-does-not-exist-and-should-return-a-404.png"
SAMPLE_WRONG_COLOUR_IMAGE = "https://www.pngmagic.com/product_images/Vanilla-White-solid-color-background.jpg"

# References path which contains colours to check against
REFERENCESPATH = "references.json"

def test_colourMatcher_returns_black_with_black_sample_image():
    assert matchColourFromUrl(SAMPLE_IMAGE_BLACK, REFERENCESPATH) == json.dumps ({'result':'black', 'statusCode':200})

def test_colourMatcher_returns_grey_with_grey_sample_image():
    assert matchColourFromUrl(SAMPLE_IMAGE_GREY, REFERENCESPATH) == json.dumps ({'result':'grey', 'statusCode':200})

def test_colourMatcher_returns_teal_with_teal_sample_image():
    assert matchColourFromUrl(SAMPLE_IMAGE_TEAL, REFERENCESPATH) == json.dumps ({'result':'teal', 'statusCode':200})      

def test_colourMatcher_returns_navy_with_navy_sample_image():
    assert matchColourFromUrl(SAMPLE_IMAGE_NAVY, REFERENCESPATH) == json.dumps ({'result':'navy', 'statusCode':200})  

def test_colourMatcher_throws_httperror_with_invalid_url():
    with pytest.raises(HTTPError):
        matchColourFromUrl(SAMPLE_BAD_URL, REFERENCESPATH)

def test_colourMatcher_throws_runtimeerror_with_no_colours_matching():
    with pytest.raises(RuntimeError) as e:
        matchColourFromUrl(SAMPLE_WRONG_COLOUR_IMAGE, REFERENCESPATH)     