import tensorflow as tf
import os
from src import utils
from src import style_transfer_tester
import argparse
import time


model_name = ['la_muse','rain_princess','shipwreck','the_scream','udnie']
#model_name = ['shipwreck']
model_dict = {}
for i in model_name:
    model_dict[i]='models/'+i+'.ckpt'


def style_image(image_path):
    content_image = utils.load_image(image_path)
    soft_config = tf.ConfigProto(allow_soft_placement=True)
    soft_config.gpu_options.allow_growth = True # to deal with large image
    sess = tf.Session(config=soft_config)

    # build the graph
    transformer = style_transfer_tester.StyleTransferTester(session=sess,
                                                            model_path="",
                                                            content_image=content_image,
                                                            )
    start_time = time.time()
    for key in model_dict:
        transformer.model_path = model_dict[key]                 
        output_image = transformer.test()
    # save result
        utils.save_image(output_image, 'output/'+key+'.jpg')
    end_time = time.time()
    # report execution time
    shape = content_image.shape #(batch, width, height, channel)
    print('Execution time for a %d x %d image : %f msec' % (shape[0], shape[1], 1000.*float(end_time - start_time)/60))


print("Model hasn't been downloaded now since one model is around 200mb.")