#imports
from constants import SRC_PATH_INPUT_SAMPLE\
    ,SRC_PATH_OUTPUT_SAMPLE\
    ,SRC_PATH_MODELS_SAMPLE\
    ,SRC_PATH_OUTPUT_RB\
    ,SRC_PATH_MODELS_RB\
    ,SLEEP_TIME
from src.main.image_processor  import object_detector\
    ,person_detector\
    ,detector_initialiser
from src.main.rbpi_server import capture_image

#std imports
import logging
import os
import datetime
import time

def main(detector:object) -> None:
    if os.name == 'nt':
        logging.info("current working directory is {}".format(os.getcwd()))
        logging.info("Initiating image detection in local")
        detections = object_detector(detector,SRC_PATH_INPUT_SAMPLE
                                     , SRC_PATH_OUTPUT_SAMPLE
                                     , SRC_PATH_MODELS_SAMPLE)
        logging.info("Computing person detection")
        person_detector(detections
                        , SRC_PATH_OUTPUT_SAMPLE)

    else:
        from picamera import PiCamera
        camera = PiCamera()
        logging.info("Initiating image detection in Pi")
        detections = object_detector(detector,capture_image(camera,SLEEP_TIME)
                                     , SRC_PATH_OUTPUT_RB
                                     , SRC_PATH_MODELS_RB)
        logging.info("Computing person detection")
        person_detector(detections
                        , SRC_PATH_OUTPUT_RB)

if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    current_time = datetime.datetime.now()
    detector=detector_initialiser(SRC_PATH_MODELS_RB)
    print("type of detecor ",type(detector))
    while ((current_time.hour>=8)&(current_time.hour<=22)):
        main(detector)
        current_time = datetime.datetime.now()
        time.sleep(300)
