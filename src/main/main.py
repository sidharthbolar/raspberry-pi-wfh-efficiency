# imports
from constants import SRC_PATH_INPUT_SAMPLE \
    , SRC_PATH_OUTPUT_SAMPLE \
    , SRC_PATH_MODELS_SAMPLE \
    , SRC_PATH_OUTPUT_RB \
    , SRC_PATH_MODELS_RB \
    , SLEEP_TIME \
    , START_HOUR \
    , END_HOUR
from src.main.image_processor import ImageProcessor

# std imports
import logging
import os
import datetime
import time
from src.main.rbpi_server import PiCameraCustom


def main(detector, camera) -> None:
    logging.info("Initiating image detection in Pi")
    camera.capture_image(SLEEP_TIME)
    detections = detector.object_detector()
    logging.info("Computing person detection")
    detector.person_detector(detections)


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    current_time = datetime.datetime.now()
    detector = ImageProcessor()
    camera = PiCameraCustom()
    while ((current_time.hour >= START_HOUR) & (current_time.hour <= END_HOUR)):
        main(detector, camera)
        current_time = datetime.datetime.now()
        time.sleep(SLEEP_TIME)
