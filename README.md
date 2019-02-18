# Maya Texture Stylization Framework using  Machine Learning

Description
---
A Maya Texture Stylization tool which can be used for fast pre-visualisation of different styles and texturing/look development purposes. This tool was created as an assignment for the final years' "Innovations" unit.

The tool is based on:
* Leon A. Gatys' [A Neural Algorithm of Artistic Style](https://arxiv.org/abs/1508.06576)
* Justin Johnson's [Perceptual Losses for Real-Time Style Transfer and Super-Resolution](http://cs.stanford.edu/people/jcjohns/eccv16)

#### Prerequisites:

```
Tensorflow 1.12.0 
Numpy 1.14.5 
Scipy 1.1.0 
Pillow(PIL) 1.4.4 
```
A complete list with the dependencies available on a test system:


#### Contents:

    ├── runStyleTransfer.py       # Main script which runs in Maya.  
    ├── StyleTransfer             # Style transfer directory.    
    │   ├── input                 # Default input files directory.  
    │   ├── output                # Default output files directory.   
    │   ├── style                 # Trained model files directory.    
    │   ├── virtualEnviornment    # Virtual Environment containing the dependencies.    
    │   ├── ImageIO.py            # Image handling utilities.    
    │   ├── run.py                # Argument parser and main loop.    
    │   ├── runStyleTransfer.sh   # Bash script used to link Maya to the command-line tool and back.    
    │   ├── transform.py          # Neural network configurator.    
    │   └── styleTransfer.py      # Style transfer session handler.    
    └── 

#### Models Available
The trained models should be placed under StyleTransfer/style/. For keeping this repository light they are not included by default. You can download the 6 trained models from [here](https://mega.nz/#F!VEAm1CDD!ILTR1TA5zFJ_Cp9I5DRofg).


#### Sample results

TODO: Post renders here.

Installing and Running the tool
---

### Running the tool inside of Maya
In order to run the tool inside Maya:

1. Set your Maya project path.
2. Copy the content of this repository in the project location.
3. Run the "runStyleTransfer.py" script. A window will prompt to the screen:
4. Use the "Add/Delete the 'CNV' tag" and select the style that you would like to use for conversion.
5. Press Convert. The folders "CollectedTX" and "ConvertedTX" will be created in the project directory.
* `CollectedTX`: Contains the original textures to be converted.
* `ConvertedTX`: Contains the converted textures which are also going to be linked to the original "file" nodes.
6. Wait until the conversion is done. You can follow the progress through the command-line and the Maya script editor. 


### Running the tool outside of Maya  
You can run the tool outside of Maya through the command-line using:
```
python styleTransfer.py --input <path_to_content_file> --model <path_to_model_file> --output <path_to_output_file> 
```

* `--input`: The path to the file to be converted.
* `--model`: The model used to convert.
* `--output`: The export path of the converted file.  

References
---

The implementation is based on:

[1] Hwalsuk Lee's [Fast Style Transfer](https://github.com/hwalsuklee/tensorflow-fast-style-transfer).

[2] Shafeen Tejani's article [Style Transfer in Real-Time](https://shafeentejani.github.io/2017-01-03/fast-style-transfer/).

[3] Harish Narayanan's article [Convolutional Neural Networks For Artistic Style Transfer](https://harishnarayanan.org/writing/artistic-style-transfer/).


## Acknowledgements
This implementation has been tested on the Bournemouth University(NCCA) Redhat systems using Tensorflow 1.12 and Maya 2018.

Thanks for the guidance offered during this project by Dr. Hongchuang Yu and the Bournemouth University's Demonstrators.
