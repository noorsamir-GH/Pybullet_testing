# 🤖 PyBullet Robotics Learning Journey

> A hands-on robotics simulation project built from scratch as part of a career transition into robotics research.
> Starting from zero — an Electrical Engineering graduate relearning robotics through binge sprints.

---

## 📽️ Demo

| Sprint 3 — Robot Dance | Sprint 4 — Inverse Kinematics |
|---|---|
| All 7 joints dancing with live sliders | Robot arm reaching for a moving target |
| ![Sprint 3 Demo](assets/sprint3_demo.gif) | ![Sprint 4 Demo](assets/sprint4_demo.gif) |

---

## 🗂️ Project Structure

```
pybullet-robotics/
│
├── sprint1/
│   └── hello_pybullet.py        # First simulation — robot moving on screen
│
├── sprint2/
│   └── joint_control.py         # Multi-joint velocity & position control
│
├── sprint3/
│   └── robot_dance.py           # 7-joint sine wave dance with live GUI sliders
│
├── sprint4/
│   ├── inverse_kinematics.py    # IK with live XYZ target sliders
│   └── basketball.py            # Robot bouncing a ball with cosine trajectory
│
└── README.md
```

---

## 🚀 What Each Sprint Builds

### Sprint 1 — Hello PyBullet
> **Goal:** Get a robot moving on screen. Anything. Just make it move.

- Installed Python, VS Code, PyBullet
- Loaded the built-in PyBullet physics examples
- First contact with URDF robot files and the physics simulation loop

**Key concepts learned:** `p.connect()`, `p.loadURDF()`, `p.stepSimulation()`

---

### Sprint 2 — Joint Control
> **Goal:** Stop running other people's code. Make a robot move YOUR way.

- Loaded the KUKA iiwa robot arm
- Queried and printed all joint info (names, types, limits)
- Controlled individual joints with velocity and position control
- Built direction-reversal logic to bounce joints within their limits
- Moved two joints simultaneously and independently

**Key concepts learned:** `getJointInfo()`, `setJointMotorControl2()`, `POSITION_CONTROL`, `VELOCITY_CONTROL`

```python
# Two joints moving independently at different speeds
p.setJointMotorControl2(robot_id, revolute_joints[0],
    controlMode=p.VELOCITY_CONTROL, targetVelocity=4 * direction, force=500)

p.setJointMotorControl2(robot_id, revolute_joints[3],
    controlMode=p.VELOCITY_CONTROL, targetVelocity=2 * direction_2, force=500)
```

---

### Sprint 3 — The Robot Dance
> **Goal:** All 7 joints moving in a coordinated sine wave. Build a live control panel.

- All 7 joints driven by sine waves with different frequencies
- Live GUI sliders for Joint Speed, Amplitude, and Wave Spread
- Custom scene helpers (`make_sphere`, `make_box`) for building environments
- Dark grid floor, hidden camera panels, clean viewport
- Added a physics-enabled sphere as a scene object

**Key concepts learned:** `addUserDebugParameter()`, `readUserDebugParameter()`, `createVisualShape()`, `createMultiBody()`

```python
# Each joint gets its own frequency — organic, fluid motion
angle = amplitude * math.sin(i * speed * 0.01 * (n + spread))
```

🎥 [Watch Sprint 3 on X →](https://x.com/i/status/2033330640414797851)

---

### Sprint 4 — Inverse Kinematics
> **Goal:** Stop controlling joints. Tell the robot WHERE to put its hand.

- Implemented full inverse kinematics using `calculateInverseKinematics()`
- Live XYZ sliders to drag a target sphere anywhere in 3D space
- Robot arm tracks the target in real time
- **Bonus experiment:** Cosine wave on Z axis = robot bouncing a ball 🏀

**Key concepts learned:** `calculateInverseKinematics()`, end effector control, workspace limits, trajectory functions

```python
# The magic line — PyBullet solves all 7 joint angles automatically
joint_angles = p.calculateInverseKinematics(robot_id, end_effector_index, target_pos)

# Bouncing ball experiment — cosine trajectory on Z
target_pos = [0.5, 0.3, 0.3 + 0.2 * math.cos(i * 0.05)]
```

---

## ⚙️ Setup & Installation

### Requirements
- Python 3.8+
- Linux (Ubuntu 22.04 recommended) or Windows
- NVIDIA GPU recommended but not required

### Install

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/pybullet-robotics.git
cd pybullet-robotics

# Install dependencies
pip3 install pybullet numpy matplotlib --break-system-packages
```

### Run any sprint

```bash
# Sprint 3 — Robot Dance
python3 sprint3/robot_dance.py

# Sprint 4 — Inverse Kinematics
python3 sprint4/inverse_kinematics.py

# Sprint 4 — Basketball experiment
python3 sprint4/basketball.py
```

### If GUI doesn't open on Linux

```bash
sudo apt install python3-opengl freeglut3-dev -y
```

---

## 🧠 Key Concepts Covered

| Concept | Sprint | Description |
|---|---|---|
| Physics simulation loop | 1 | `stepSimulation()` advancing time |
| Forward kinematics | 2 | Direct joint angle control |
| Joint limits | 2 | Reading and respecting URDF limits |
| Sine wave motion | 3 | Smooth periodic joint trajectories |
| GUI sliders | 3 | Live parameter control during simulation |
| Inverse kinematics | 4 | Position-based end effector control |
| Trajectory functions | 4 | Time-parameterized target positions |

---

## 🗺️ What's Next

- [ ] **Sprint 5** — Reinforcement Learning: train a policy to reach targets autonomously
- [ ] **MuJoCo port** — Recreate Sprint 4 in MuJoCo for comparison
- [ ] **ROS 2 integration** — Bridge simulation to real robot middleware
- [ ] **Pick and place** — Full grasp and move task

---

## 👤 About

EE graduate with 8 years of experience, making a career transition into robotics research.
Building in public — one sprint at a time.

🐦 Follow the journey on X: [@YOUR_HANDLE](https://x.com/YOUR_HANDLE)

---

## 📄 License

MIT License — feel free to use this as a starting point for your own robotics learning journey.
