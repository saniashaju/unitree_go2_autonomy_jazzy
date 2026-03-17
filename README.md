# unitree_go2_autonomy_jazzy
Internship project Unitree Go2 Autonomy Stack to ROS 2 Jazzy on Ubuntu 24.04. Includes Gazebo simulation validation, real-world L1 LiDAR testing, and a strategic pivot to the official SDK for stable CycloneDDS communication
## 🛠️ Project Overview
The initial objective was to deploy the CMU Autonomy Stack onto the physical Unitree Go2 EDU robot to enable autonomous mapping (SLAM) and navigation. Development was conducted on Ubuntu 24.04 using ROS 2 Jazzy. 

Due to hardware constraints and system resource limitations, the project underwent a strategic pivot to the official `unitree_ros2` SDK to prioritize system stability and establish a robust communication foundation.

## 💻 Phase 1: Simulation & Testing (Gazebo)
To ensure code safety before hardware deployment, a "Digital Twin" simulation was configured.
* **Outcome:** Successfully spawned the URDF model in Gazebo, visualized sensor data in RViz2, and validated basic teleoperation and mapping logic.


## 🚧 Phase 2: Real-World Hardware Limitations
Deploying the custom autonomy stack to the physical hardware revealed key engineering constraints:
1. **SLAM Localization Drift:** The onboard Unitree L1 solid-state LiDAR has a narrower Field of View (FoV) and lower point density compared to the 360° spinning LiDARs the stack was originally designed for. This caused the SLAM algorithm to fail to localize, resulting in severe map drift.
2. **Resource Saturation:** Attempting to fuse the heavy 3D point cloud with a live GStreamer camera feed inside the ROS 2 RViz environment maxed out host CPU and RAM, leading to system freezes.

## 🚀 Phase 3: Strategic Pivot to Official SDK (`unitree_ros2`)
To establish a stable, crash-free "spinal cord" for the robot, development was pivoted to the official Unitree SDK utilizing **CycloneDDS** middleware. 

### Key Engineering Achievements:
* **Stable Teleoperation Bridge:** Developed a custom `bridge.py` ROS 2 node that translates standard `cmd_vel` Twist messages into `unitree_api` requests (API ID: 1008). 
* **Robot Handover Validation:** Successfully bypassed the physical remote by unlocking the robot's API (`/api/sport/request`), establishing a direct, zero-latency laptop-to-robot control loop.
* **Optimized Vision Pipeline:** Extracted live video via direct UDP (`gst-launch-1.0`), bypassing the heavy ROS 2 processing pipeline. This resulted in zero-latency video without host saturation.

## 🗺️ Future Roadmap
With a robust CycloneDDS foundation now established, future iterations will focus on:
1. Safely subscribing to the L1 LiDAR's `PointCloud2` topics via the stable bridge.
2. Utilizing lightweight point-cloud processing (e.g., 3D Voxel/Elevation grids) rather than full SLAM.
3. Developing a custom, resource-efficient obstacle avoidance script.




