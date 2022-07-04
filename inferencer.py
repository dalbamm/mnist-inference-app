import numpy as np
import cv2
import os
import onnxruntime as ort
import numpy as np

def run_inference(file):
    
    # read file
    npimg = np.fromstring(file.read(), np.uint8)
    image = cv2.imdecode(npimg,1)

    # convert, resize
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (28,28)).astype(np.float32)/255
    
    # reshape
    ipt = np.reshape(gray, (1,1,28,28))

    # init. onnx runtime inference session
    ort_sess = ort.InferenceSession('mnist-7.onnx')
    
    # run. ort session
    outputs = ort_sess.run(None, {'Input3': ipt})
    
    # Print Result
    result = outputs[0].argmax(axis=1)

    return int(result[0])
