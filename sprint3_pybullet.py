import pybullet as p
import pybullet_data
import time
import math

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)

# Sliders Configuration 
p.configureDebugVisualizer(p.COV_ENABLE_RGB_BUFFER_PREVIEW, 0)
p.configureDebugVisualizer(p.COV_ENABLE_DEPTH_BUFFER_PREVIEW, 0)
p.configureDebugVisualizer(p.COV_ENABLE_SEGMENTATION_MARK_PREVIEW, 0)

planeId  = p.loadURDF("plane.urdf")
p.changeVisualShape(planeId, -1, rgbaColor=[0.15, 0.15, 0.15, 1])
robot_id = p.loadURDF("kuka_iiwa/model.urdf", basePosition=[0,0,0], useFixedBase=True)

x_slider = p.addUserDebugParameter("Target X", -0.8, 0.8, 0.5)
y_slider = p.addUserDebugParameter("Target Y", -0.8, 0.8, 0.3)
z_slider = p.addUserDebugParameter("Target Z",  0.0, 1.0, 0.4)

# The end effector is the "hand" — the last link of the arm
end_effector_index = 6

# Place a visual target — a small red sphere
def make_sphere(radius, pos, rgba, mass=0.0):
    col = p.createCollisionShape(p.GEOM_SPHERE, radius=radius)
    vis = p.createVisualShape(p.GEOM_SPHERE, radius=radius, rgbaColor=rgba)
    return p.createMultiBody(mass, col, vis, pos)

# Target position — this is WHERE we want the hand to go
target_pos = [0.8, 0.3, 0.9]
target_id  = make_sphere(0.05, target_pos, [1, 0, 0, 1])  # red sphere

for i in range(100000):
    
    #target_pos = [
    X_x = p.readUserDebugParameter(x_slider),
    Y_y = p.readUserDebugParameter(y_slider),
    Z_z = p.readUserDebugParameter(z_slider)
    #            ]

    target_pos = [
    0.4,
    0.4,
    abs(0.6 * math.cos(i * 0.005))
                ]

    # Move the red sphere to match
    p.resetBasePositionAndOrientation(target_id, target_pos, [0,0,0,1])

    # Solve IK for new target
    joint_angles = p.calculateInverseKinematics(robot_id, end_effector_index, target_pos)


    # Apply the solved angles to all joints
    for j in range(len(joint_angles)):
        p.setJointMotorControl2(
            robot_id, j,
            controlMode=p.POSITION_CONTROL,
            targetPosition=joint_angles[j],
            force=500
        )

    p.stepSimulation()
    time.sleep(1./240.)

p.disconnect()