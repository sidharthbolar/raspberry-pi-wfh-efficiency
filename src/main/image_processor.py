# imports
import logging
import csv
from datetime import datetime
from imageai.Detection import ObjectDetection
from constants import SRC_PATH_INPUT_RB, SRC_PATH_OUTPUT_RB, SRC_PATH_MODELS_RB,RESULT_HEADERS


class ImageProcessor(ObjectDetection):
    default_model = "yolo.h5"
    default_speed = "fast"
    default_input_image_path = SRC_PATH_INPUT_RB
    default_image_output_path = SRC_PATH_OUTPUT_RB
    default_model_path = SRC_PATH_MODELS_RB
    default_results_path = SRC_PATH_OUTPUT_RB
    default_minimum_percentage_probability = 50

    def __init__(self, input_image_path=default_input_image_path
                 , output_image_path=default_image_output_path, model_path=default_model_path
                 , result_path=default_results_path, default_speed=default_speed, default_model=default_model
                 , *args, **kwargs):
        super(ImageProcessor, self).__init__(*args, **kwargs)
        self.input_image_path = input_image_path
        self.output_image_path = output_image_path
        self.result_path = result_path
        self.CustomObjects(person=True)
        self.setModelTypeAsYOLOv3()
        self.setModelPath(model_path + default_model)
        self.loadModel(detection_speed=default_speed)

    def object_detector(self) -> list:
        '''
        Uses the input Image object and detects object in them
        :return: an array of dictionaries, with each dictionary corresponding to the objects
                detected in the image. Each dictionary contains the following property:
                * name (string)
                * percentage_probability (float)
                * box_points (tuple of x1,y1,x2 and y2 coordinates)
        '''
        logging.info("running object detector module")
        detections = self.detectObjectsFromImage(input_image=self.input_image_path,
                                                 output_image_path=self.output_image_path + 'image_detect.jpg',
                                                 minimum_percentage_probability=self.default_minimum_percentage_probability)
        logging.info("Detections for image captured {}".format(detections))
        return detections

    @staticmethod
    def person_detector(detections: list, SRC_PATH_OUTPUT: str=SRC_PATH_OUTPUT_RB) -> None:
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
            if detections[0]['name'] == 'person':
                current_time = datetime.now()
                current_time_string = current_time.strftime("%d/%m/%Y %H:%M:%S")
                current_dict = {}
                current_dict[current_time_string] = '1'
                logging.info('current status 0 is {}'.format(current_dict))
                f = open(SRC_PATH_OUTPUT + 'result.csv', 'a')
                writer = csv.DictWriter(f, fieldnames=RESULT_HEADERS)
                for key in current_dict:
                    writer.writerow({'TIMESTAMP':key,'PRESENCE_BOOLEAN':current_dict[key]})
                f.close()

        except IndexError:
            current_time = datetime.now()
            current_time_string = current_time.strftime("%d/%m/%Y %H:%M:%S")
            current_dict = {}
            current_dict[current_time_string] = '0'
            logging.info('current status 1 is {}'.format(current_dict))
            f = open(SRC_PATH_OUTPUT + 'result.csv', 'a')
            writer = csv.DictWriter(f, fieldnames=RESULT_HEADERS)
            for key in current_dict:
                writer.writerow({'TIMESTAMP': key, 'PRESENCE_BOOLEAN': current_dict[key]})
            f.close()
