# Monitoring Fishing Activity-Kaggle
## Introduction
Given over 500MB colored jpeg pictures with fishes, classify the fish into six different catagories including: other fishes.
## files:
import_image.py: Use to import images from the directory and turn them into 3D RGB matrices.

main.py: Use a CNN with over 200 layers with about 200 nodes/layer to classify the images.
## How to use:
Basically, modify the folder names in main.py to correctly pointing to the pictures.
This model does not save the trained classifier automatically. So, you probablity need to do them yourselves.

## Method:
It is not magical. Basically, this is designed as a 300 * 200 CNN. The F score is only about 70. 
I suspect that the images can be better classified with another import format other than RGB.

