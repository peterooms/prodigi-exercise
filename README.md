# prodigi-exercise

Colour Matcher exercise solution.

The function matchColourFromUrl takes in the URL of an image, and a path to a JSON file that defines colours and their names.
If successful, it outputs the name of the colour it has identified, and if unsuccessful it throws an error.

## Methodology
The script downloads the images to a temp directory on the disk, then works out the average colour of the four corners of the 
image, then compares it to the reference colours it has been supplied in the json file. It returns the first one that is 
close enough (this threshold is configurable).

If none of the colours are close enough, or the URL provided is invalid, it throws an error.

## Assumptions

I've assumed that the four corners of the image are sufficient to get the colour we want to identify. 
Although the supplied images were in PNG format, taking the average of the four points helps us to smooth out any minor inaccuracies 
in the colours (e.g. if there are JPEG artefacts). 

If the format of the image changes significantly, we'd need to revise which pixels we looked at.

## Work not completed / next steps

* I didn't build the solution out into a full endpoint in order to complete it with enough time to get it accross. However, it would be 
simple to incorporate into a django or flask route, and could be used as-is in an AWS Lambda. 

* Before moving into prod we'd want to build out logging and error handling some more as this is very much a proof-of-concept. If this was going to be an AWS Lambda, we'd code it
in terraform, as well as some CloudWatch alarms to notify us if anything went wrong. In that case, we'd use API Gateway to give 
us an endpoint and a lot of the scaling is done for us. API Gateway has excellent tools to throttle the rate if necessary, and if we were worried about interferance we could add authentication.

* If this was going to be self-hosted, I'd look to implement a queue system (e.g. celery). As the images take a few 
seconds to download we might end up with problems during high-demand times and a queueing system would mitigate this.

* The tests are very basic integration tests at the moment - this is fine to demonstrate the concept but for prod I'd ideally want full
unit tests.

* If the same images were appearing over and over again, we could look into caching them as an additional cost-saving measure. I'd
also like to investigate if we can perform this matching without downloading the whole image first, as downloading them to disk is a long process, and AWS Lambdas are charged by the millisecond.

## How to run

Before you start, run `pip install -r requirements.txt` to install any requirements you don't already have.

The best way to run the code is by running the supplied tests via `pytest test_colourMatcher.py`. This will run the code six
times - four of which are successful, and two of which are unsuccessful. 