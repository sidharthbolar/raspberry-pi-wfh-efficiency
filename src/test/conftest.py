import pytest
from src.main.image_processor import ImageProcessor
from constants import *
from src.main.result_processor import ResultProcessor
from src.main.alert_processor import AlertProcessor

@pytest.fixture
def local_alert_processor():
    alert=AlertProcessor()
    return  alert

@pytest.fixture
def local_result_processor():
    result=ResultProcessor(SRC_PATH_OUTPUT_SAMPLE)
    return result

@pytest.fixture
def local_positive_image_processor() -> object:
    detector = ImageProcessor(SRC_PATH_INPUT_SAMPLE
                              , SRC_PATH_OUTPUT_SAMPLE
                              , SRC_PATH_MODELS_SAMPLE
                              , SRC_PATH_OUTPUT_SAMPLE)
    return detector

@pytest.fixture
def local_negative_image_processor() -> object:
    detector = ImageProcessor(SRC_PATH_INPUT_NEGATIVE_SAMPLE
                              , SRC_PATH_OUTPUT_SAMPLE
                              , SRC_PATH_MODELS_SAMPLE
                              , SRC_PATH_OUTPUT_SAMPLE)
    return detector
