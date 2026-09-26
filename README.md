# DriveMotion-Unity

실차 주행 중 측정된 데이터를 기반으로 운전자/탑승자의 움직임을 Unity에서 시각화하는 프로젝트입니다.

현재는 Xsens MTi-620 IMU 3개를 사용한 데이터를 기반으로 개발하고 있으며,
추후 카메라, 차량 데이터 등 다양한 센서 데이터로 확장하는 것을 목표로 합니다.

## Pipeline

Raw Data
→ Column Detection
→ Data Preprocessing
→ Quaternion / Coordinate Conversion
→ Unity Visualization

## Structure

```
drive-motion-unity/
│
├── README.md
├── .gitignore
│
├── data/
│   ├── raw/
│   └── processed/
│
├── preprocessing/
│   ├── main.py
│   ├── column_detector.py
│   └── imu_processor.py
│
└── unity/
    └── DriveMotionUnity/
        ├── Assets/
        │   ├── Scenes/
        │   │   └── Main.unity
        │   └── Scripts/
        │       ├── DataLoader.cs
        │       ├── MotionPlayer.cs
        │       └── ImuVisualizer.cs
        ├── Packages/
        └── ProjectSettings/
```

Current Data
Xsens MTi-620 × 3
Head IMU
Left Shoulder IMU
Right Shoulder IMU
Vehicle Speed / Acceleration / Yaw Rate
Goal

원본 주행 데이터를 입력하면 필요한 데이터를 자동으로 탐색 및 전처리하고,
Unity에서 주행 당시 탑승자의 움직임을 재생할 수 있는 파이프라인을 구축합니다.