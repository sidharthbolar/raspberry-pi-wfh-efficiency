import pytest

from src.main.image_processor import ImageProcessor
from constants import *

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
