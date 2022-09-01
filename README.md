# Kuka-Visp Hand-Eye Calibration
This repo allows the use of the Visp library to conduct extrinsic Hand-Eye calibration by capturing the robot's pose using the RoboDK python API and outputting the necessary pose file in YAML format. This can easily be extended to be used with other manufacturers as they are almost all supported by RoboDK. 
* You can find the list of manufacturers with supported RoboDK drivers [here](https://robodk.com/doc/en/Robot-Drivers.html) 

### Requirements:
- A working installation of RoboDK
- Python3
- Any Kuka robot with KukaVarProxy running in the background (See: [RoboDK driver for KUKA](https://robodk.com/doc/en/Robots-KUKA.html#DriverKUKA))
- A working installation of the VISP library

## Instructions
 #### 1 - Start RoboDK and Connect to Robot
* Start RoboDK using <br>
```./<RoboDK-Directory>/RoboDK-Start.sh ```
* Follow the corresponding [tutorial](https://robodk.com/doc/en/Robot-Calibration-LaserTracker-Connect-robot.html "tutorial") to connect to your robot

#### 2 - Start an image capture service
* You can use the `grabber` scripts included in the [visp library](https://visp-doc.inria.fr/doxygen/visp-daily/tutorial-grabber.html) or you can use an application like [Cheese](https://help.gnome.org/users/cheese/stable/)

#### 3 - Run the recordRobotPoses.py script
* `python3 recordRobotPose.py`

#### 4 - Collect Image-Pose pairs

  1. Move the robot to the required pose to capture the image 
  2. Capture an image using your preferred method 
  3. Press Enter in the open terminal to record robot pose
  4. Repeat this process until enough image-pose pairs have been captured. A useful guide to capturing good calibration poses can be found [in the Visp extrinsic calibration tutorial](https://visp-doc.inria.fr/doxygen/visp-3.4.0/tutorial-calibration-extrinsic.html)
  
#### 5 - Run savePose.cpp to correctly format the poses required by Visp

* Inside the kuka-calib directory, run `./build/savePose` to create appropriately formatted YAML files

  


