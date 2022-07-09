# Summary - Project Inspiration 

With remote working becoming a new norm maintaining work life balance has become an increasing challenge :technologist:

One of my 2022 "resolutions"  to enforce a more strict boundary between work and personal life and not be a :juggling_person:

Being a DE I wanted to have a data driven approach to tackle this problem. :nerd_face: :nerd_face: :computer:

First step to solve any problem is to identify it!  :trollface: :trollface: :trollface:

Questions that needed answers was How much was I working ?

Was I really glued at my home office workstation? 

To answer and quantify these queries , have decided to use a spare Raspberry Pi lying around couple with a pre-trained image detector model

Let’s see how I chose to tackle this

## Problem Statement: Quantify the time spent time working

### Assumptions:If I am ‘detected’at my work station then its assumed I am working :)

#### Note:Time spent in attending virtual meetings still counts as work!!!

## Solution:Interface a Pi Cam module with Raspberry PI and if a person is detected(wfh would mean only I am detected)then count that instance has working

1. At EOD, aggregate the count of instances working and the summary results are notified via email

2. This would help me identify the problem at hand and answer the question whether I am really “working a lot” backed by Data!

### Detailed Solution:

The solution module is split into 4 sections:

1. RbPi Server Processor: This module is responsible for controlling the camera Interfaced with Pi and handle the actions associated for capturing an Image.
2. Image Processor: This module is associated for performing the object detection on the image captured by the earlier module.Have utilized the pre-trained object detection model from Image AI. The reference docs explain the OOB functionality and it meets the initial crude requirement
3. Alert Processor: This module is responsible for sending the notification.In the initial release this will only notify via email
4. Report Processor: This module is responsible for computing the actual time spent working and generate a summary result to be dispatched by the earlier module
5. Model: The pre-trained model YOLOv3 model has been downloaded and used “as-is” to minimize complexity


#### Unit Testing: Unit testing was a challenge as the picamera module is not supported on windows environment however for all other modules and its associated methods have added corresponding unit tests added to ensure new features added do no break existing functionality


