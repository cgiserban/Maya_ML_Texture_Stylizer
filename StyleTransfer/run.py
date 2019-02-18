#Importing Libs

import tensorflow as tf
import os
import argparse
import time
import imageIO
import styleTransfer

#Parsing Data and Checking Arguments to be valid

#Create arguments
def parse_arguments():
  
  parser = argparse.ArgumentParser(description = "Maya Style Transfer")
  
  
  parser.add_argument('--model', type=str, default='models/la_muse.ckpt', 
                     help='please path your model "*ckpt" file', required = True)
  
  
  parser.add_argument('--input', type=str, default='input/default.jpg', 
                     help='please path your input file', required = True)
  
  
  parser.add_argument('--output', type=str, default='output/output.jpg', 
                     help='please select the path to your output file', required = True)
  
  return check_arguments(parser.parse_args())


#Check each argument and print errors
def check_arguments(args):
  
  #Model
  
  try:
    assert os.path.exists(args.model + '.index') and os.path.exists(args.model + '.meta') and os.path.exists(
            args.model + '.data-00000-of-00001')
    
  except:
    print ('Please make sure that your model contains all the required files: *.index, *.meta, *.data-00000-of-00001"')
    return None
  
  #Input
  
  try:
    assert os.path.exists(args.input)
  except:
    print ('Your input file does not exist')
    return None
  
  #Output
  
    dirname = os.path.dirname(args.output)
    try:
      if len(dirname) > 0:
          os.stat(dirname)
    except:
      os.mkdir(dirname)
      return None
  
  return args

#Run the program
  
def main():
  args = parse_arguments()
  if args is None:
    exit()

  #Load content image
  content = imageIO.loadImage(args.input)

  #Start session
  sessionStart = tf.ConfigProto(allow_soft_placement=True)
  sessionStart.gpu_options.allow_growth = True
  sess = tf.Session(config = sessionStart)
  transformer = styleTransfer.styleTransfer(session = sess, model_path=args.model, content_image=content)

  start_time = time.time()
  output_image = transformer.test()
  end_time = time.time()

  imageIO.saveImage(output_image, args.output)

  print('Execution done in %f msec' %(1000.*float(end_time - start_time)/60))

if __name__ == '__main__':
    main()
