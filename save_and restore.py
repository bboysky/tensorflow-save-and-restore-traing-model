# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 19:00:07 2017

@author: Administrator
"""

import tensorflow as tf

saver = tf.train.Saver()
# save the model
with tf.Session() as sess:
    sess.run(init_op)
    sess.save(sess,"save_path/file_name.ckpt")

#restore the model    
'''

with tf.Session() as sess:
    sess.run(init_op)
    saver.restore(sess,"save_path/file)
'''