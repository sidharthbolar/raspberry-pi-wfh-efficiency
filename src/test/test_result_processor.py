
def test_result_processor_count_check(local_result_processor):
    print("input file path of csv ",local_result_processor.input)
    assert local_result_processor.result_processor_total_detections()==4

def test_result_processor_consecutive_detections(local_result_processor):
    assert local_result_processor.result_processor_consecutive_detections()==3
