#include <iostream>
#include <visp3/core/vpMath.h>
#include <visp3/core/vpRotationMatrix.h>
#include <visp3/core/vpThetaUVector.h>
#include <fstream> 
#include <string>
using namespace std;
int main()
{
  int fileCount = 1;
  while (true){
    ostringstream poseFileName; 
    poseFileName << "../RoboDK_Pose_" << fileCount;

    // Read from the pose file
    ifstream poseFile(poseFileName.str());

    //If no more files exist, exit program
    if (!poseFile) {
      cout << "Finished Creating Files" << endl;
      break;
    }

    //Init necessary variables
    float c1, c2, c3,x,y,z;
    int lineCount = 0;
    vpThetaUVector tu;
    vpRotationMatrix R;

    //Iterate over lines
    while (poseFile >> c1 >> c2 >> c3)
    {
        if (lineCount == 0){
          x = c1/1000;
          y = c2/1000;
          z = c3/1000;
          lineCount++;
          continue;
        }

        R[lineCount-1][0] = c1; 
        R[lineCount-1][1] = c2; 
        R[lineCount-1][2] = c3; 

        lineCount++;
    }
    
    //Create thetaU vector from rotation matrix
    tu.buildFrom(R);
    //cout << tu << endl;
    //cout << R << endl;
    
    //Create visp pose vector from translation and thetaU representation
    vpPoseVector minimalPose;
    minimalPose[0] = x;
    minimalPose[1] = y;
    minimalPose[2] = z;
    minimalPose[3] = tu[0];
    minimalPose[4] = tu[1];
    minimalPose[5] = tu[2];

    ostringstream yamlFilename; 
    yamlFilename << "../pose_fPe_" << fileCount <<".yaml";
    minimalPose.saveYAML(yamlFilename.str(), minimalPose);
    cout << "Saved Visp Pose to " << yamlFilename.str() << " successfully" << endl;
    fileCount+=1;
    }
}