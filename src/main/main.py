# imports
from constants import SRC_PATH_INPUT_SAMPLE \
    , SRC_PATH_OUTPUT_SAMPLE \
    , SRC_PATH_MODELS_SAMPLE \
    , SRC_PATH_OUTPUT_RB \
    , SRC_PATH_MODELS_RB \
    , SLEEP_TIME \
    , START_HOUR \
    , END_HOUR\
    ,customcontents

from src.main.alert_processor import AlertProcessor
from src.main.image_processor import ImageProcessor

# std imports
import logging
import os
import datetime
import time
from src.main.rbpi_server import PiCameraCustom
from src.main.result_processor import ResultProcessor


def main(detector, camera) -> None:
    logging.info("Initiating image detection in Pi")
    camera.capture_image(SLEEP_TIME)
    detections = detector.object_detector()
    logging.info("Initiating person detection")
    detector.person_detector(detections)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    current_time = datetime.datetime.now()
    logging.info("Begin Running 1 ")
    detector = ImageProcessor()
    logging.info("Begin Running 2 ")
    camera = PiCameraCustom()
    logging.info("Begin Running 3 ")
    while ((current_time.hour >= START_HOUR) & (current_time.hour <= END_HOUR)):
        main(detector, camera)
        current_time = datetime.datetime.now()
        time.sleep(SLEEP_TIME)

    result = ResultProcessor(date=current_time.strftime("%Y-%m-%d"))
    alert = AlertProcessor(body=customcontents
                           .format(result.result_processor_total_detections()
                            ,result.result_processor_consecutive_detections())
                           ,subject="WFH Status for {}".format(datetime.datetime.date()))
