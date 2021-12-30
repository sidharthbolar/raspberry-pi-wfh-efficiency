#imports
from constants import SRC_PATH_INPUT_RB,CAMERA_SLEEP_TIME
from picamera import PiCamera


class PiCameraCustom(PiCamera):

    def __init__(self,*args, **kwargs):
        super(PiCameraCustom, self).__init__(*args, **kwargs)

    def capture_image(self,CAMERA_SLEEP_TIME: int =CAMERA_SLEEP_TIME,SRC_PATH_INPUT:str =SRC_PATH_INPUT_RB) -> str:
        '''
        :param CAMERA_SLEEP_TIME: default time between consequtive cliks
        :param SRC_PATH_INPUT Path where image is captured
        :param SLEEP_TIME:Sleep time between consecutive image maintained in constants file
        :return: Path where image is captured and overwritten in each consecutive run with default name image.jpg
        '''
        from time import sleep
        sleep(CAMERA_SLEEP_TIME)
        self.capture(SRC_PATH_INPUT)
        self.close()
        return SRC_PATH_INPUT
