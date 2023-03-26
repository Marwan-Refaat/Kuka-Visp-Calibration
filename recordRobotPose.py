from operator import truediv
from robolink import *                  # import the robolink library
from robodk import *                    # import the robodk library


RDK = Robolink()                        # connect to the RoboDK API
robot  = RDK.Item('', ITEM_TYPE_ROBOT)  # Retrieve a robot available in RoboDK

#target  = RDK.Item('Target 1')         # Retrieve a target (example)

print("------------------------------------------------------\n")
i = 1
correctJoints = 0
while True:
    try:
    
        print("Press ENTER to save robot pose or CTRL+C to exit")
        x = input()

        #Update RoboDK with most recent joint positions
        if robot.Connect() > 0:
            robot.Joints()
        
        #Get Pose from RoboDK
        pose = robot.Pose() #4x4 Homogeneous Matrix
        print(pose)
        pos = pose.Pos() # [x,y,z] Translation
        rotMatrix = pose.Rot33().Rows()  #3x3 Rotation matrix e.g: [[1,0,0],[0,1,0],[0,0,1]]  
        
       
        #print(rotMatrix.Rows())
        fileName = f"RoboDK_Pose_{i}"
        f = open(fileName, "w")
        f.write(f"{pos[0]} {pos[1]} {pos[1]} \n") #Write pose to first line

        #Write Rotation matrices to following lines
        f.write(f"{round(rotMatrix[0][0],5)} {round(rotMatrix[0][1],5)} {round(rotMatrix[0][2],5)}\n") 
        f.write(f"{round(rotMatrix[1][0],5)} {round(rotMatrix[1][1],5)} {round(rotMatrix[1][2],5)}\n") 
        f.write(f"{round(rotMatrix[2][0],5)} {round(rotMatrix[2][1],5)} {round(rotMatrix[2][2],5)}\n")

        f.close()
        print("Recorded pose is ", pose)
        print(f"Pose written to {fileName} successfully")
        print("\n------------------------------------------------------\n")
        
        pose = 0
        pos = 0
        rotMatrix = 0
        i+=1
    except KeyboardInterrupt:
        exit()





