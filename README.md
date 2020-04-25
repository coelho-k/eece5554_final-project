# EECE5554 Final Project - Group 2
## LiDAR Object Detection and Classification

### Group Members
- Kyle Coelho
- Yiwei Gan
- Sheng Xiang
- Vlad Vandalovsky


### How to Run 
1. Copy the [src](./src) folder into your `catkin_ws`
2. Change directory to your `catkin_ws`
3. Run `catkin_make` or `catkin build` based on your desired build approach
4. Run `source devel/setup.bash`
5. Ensure that `source devel/setup.bash` is also in your ~/.bashrc
5. Run `roscore`
6. In a new terminal, run `roslaunch tracking_lib lidar_tracking.launch`
7. In another new terminal, start playback for the `LIDAR_mapping_bicycle_pedestrian_detection` bag file (from the provided Google Drive in class)
   
### What to expect
1. An `RVIZ` Window will open with the orignal LiDAR feed overlayed with the object tracking highlighting
2. `Bicyclists` will appear as boxes with `green` labels
3. `Pedestrians` will appear as boxes with `blue` labels