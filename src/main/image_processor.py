#imports
import logging
import csv
from datetime import datetime
from imageai.Detection import ObjectDetection

def detector_initialiser(SRC_PATH_MODELS: str) -> object:
    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(SRC_PATH_MODELS+"/yolo.h5")
    detector.loadModel(detection_speed="flash")
    return detector

def object_detector(detector: object,INPUT_IMAGE: str, OUTPUT_IMAGE: str, SRC_PATH_MODELS: str) -> list:
    '''
    :param INPUT_IMAGE: Path where input image is present in jpg format for which object detection needs to occur
    :param OUTPUT_IMAGE: Path where output image with object detection labels added with probailities
    :param SRC_PATH_MODELS: Path where pre-trained models is stored, by default this is yolo.h5
    :return: an array(List) of dictionaries, with each dictionary corresponding to the objects
            detected in the image. Each dictionary contains the following property:
            * name (string)
            * percentage_probability (float)
            * box_points (list of x1,y1,x2 and y2 coordinates)
    '''
    logging.info("running object detector module")
    detections = detector.detectObjectsFromImage(input_image=INPUT_IMAGE, output_image_path=OUTPUT_IMAGE+'image_detect.jpg',minimum_percentage_probability=50)
    logging.info("Detections for image captured {}".format(detections))
    return detections

def person_detector(detections: list, SRC_PATH_OUTPUT: str) -> None:
    '''
    :param detections:  an array(List) of dictionaries, with each dictionary corresponding to the objects
                        detected in the image. Each dictionary contains the following property:
                        * name (string)
                        * percentage_probability (float)
                        * box_points (list of x1,y1,x2 and y2 coordinates)
    :param SRC_PATH_OUTPUT:Output where csv output of results is written based on if a person is detected or not
    :return: None
    '''
    try:
        if  detections[0]['name']=='person':
            current_time = datetime.now()
            current_time_string = current_time.strftime("%d/%m/%Y %H:%M:%S")
            current_dict={}
            current_dict[current_time_string]='1'
            logging.info('current status 0 is {}'.format(current_dict))
            f = open(SRC_PATH_OUTPUT+'result.csv', 'a')
            writer = csv.writer(f)
            writer.writerow(current_dict.items())
            f.close()

    except IndexError:
        current_time = datetime.now()
        current_time_string = current_time.strftime("%d/%m/%Y %H:%M:%S")
        current_dict = {}
        current_dict[current_time_string] = '0'
        logging.info('current status 1 is {}'.format(current_dict))
        f = open(SRC_PATH_OUTPUT + 'result.csv', 'a')
        writer = csv.writer(f)
        writer.writerow(current_dict.items())
        f.close()
