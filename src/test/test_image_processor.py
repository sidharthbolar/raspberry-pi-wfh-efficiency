from constants import SRC_PATH_OUTPUT_SAMPLE
import os

def test_object_detector(local_positive_image_processor):
    assert isinstance(local_positive_image_processor.object_detector(), list)


def test_person_positive_detector(local_positive_image_processor):
    detections = local_positive_image_processor.object_detector()
    print(detections)
    assert detections[0]['name'] == 'person'


def test_person_negative_detector(local_negative_image_processor):
    detections = local_negative_image_processor.object_detector()
    assert len(detections)==0

def test_write_when_person_detected(local_positive_image_processor):
    detections = local_positive_image_processor.object_detector()
    local_positive_image_processor.person_detector(detections, SRC_PATH_OUTPUT_SAMPLE)
    assert os.path.exists(SRC_PATH_OUTPUT_SAMPLE+'result.csv')

def test_write_when_person_not_detected(local_negative_image_processor):
    detections = local_negative_image_processor.object_detector()
    local_negative_image_processor.person_detector(detections, SRC_PATH_OUTPUT_SAMPLE)
    assert os.path.exists(SRC_PATH_OUTPUT_SAMPLE+'result.csv')