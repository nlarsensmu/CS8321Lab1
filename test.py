import tensorflow as tf 

if tf.test.gpu_device_name(): 

    print('Default GPU Device')
else:

   print("Please install GPU version of TF")