from constants import curr_date_str,customcontents,customsubject

def test_send_mail(local_alert_processor):
    local_alert_processor.send_mail()

def test_send_mail_with_result(local_alert_processor,local_result_processor):
    t1=curr_date_str
    t2=local_result_processor.result_processor_total_detections()
    t3=local_result_processor.result_processor_consecutive_detections()
    subject_computed=t1
    body_computed=customcontents.format(t2,t3)
    print('subject computed is ',subject_computed)
    local_alert_processor.send_mail(customsubject=subject_computed,customcontents=body_computed)



