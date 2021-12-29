#imports
from constants import SRC_PATH_INPUT_RB

def capture_image(camera: object,SLEEP_TIME: int,SRC_PATH_INPUT:str =SRC_PATH_INPUT_RB) -> str:
    '''
    :type SLEEP_TIME:
    :param SRC_PATH_INPUT Path where image is captured
    :param SLEEP_TIME:Sleep time between consecutive image maintained in constants file
    :return: Path where image is captured and overwritten in each consecutive run with default name image.jpg
    '''
    from time import sleep
    sleep(5)
    camera.capture(SRC_PATH_INPUT)
    camera.close()
    return SRC_PATH_INPUT
