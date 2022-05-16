from  colourMatcher import matchColourFromUrl


SAMPLE_IMAGE_BLACK = "https://pwintyimages.blob.core.windows.net/samples/stars/test-sample-black.png"
SAMPLE_IMAGE_GREY = "https://pwintyimages.blob.core.windows.net/samples/stars/test-sample-grey.png"
SAMPLE_IMAGE_TEAL = "https://pwintyimages.blob.core.windows.net/samples/stars/test-sample-teal.png"
SAMPLE_IMAGE_NAVY = "https://pwintyimages.blob.core.windows.net/samples/stars/test-sample-navy.png"

REFERENCESPATH = "references.json"

def test_colourMatcher_returns_black_with_black_sample_image():
    assert matchColourFromUrl(SAMPLE_IMAGE_BLACK, REFERENCESPATH) == 'black'

def test_colourMatcher_returns_grey_with_grey_sample_image():
    assert matchColourFromUrl(SAMPLE_IMAGE_GREY, REFERENCESPATH) == 'grey'

def test_colourMatcher_returns_teal_with_teal_sample_image():
    assert matchColourFromUrl(SAMPLE_IMAGE_TEAL, REFERENCESPATH) == 'teal'        

def test_colourMatcher_returns_navy_with_navy_sample_image():
    assert matchColourFromUrl(SAMPLE_IMAGE_NAVY, REFERENCESPATH) == 'navy'    

def test_colourMatcher_throws_error_with_invalid_sample_image():
    pass
#    assert colourMatcher(SAMPLE_IMAGE_INVALID) == 'navy'        

def test_colourMatcher_throws_error_with_invalid_sample_image():
    pass
#    assert colourMatcher(SAMPLE_IMAGE_INVALID) == 'navy'      