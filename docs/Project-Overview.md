# Project Overview

## 1. Project Title

**AI and IoT Based Parkinson's Disease Prediction and Monitoring
System**

## 2. Objective

The project aims to provide early prediction and continuous monitoring
of Parkinson's disease-related symptoms by combining IoT sensors,
artificial intelligence, machine learning, cloud technologies, and
remote monitoring.

## 3. System Flow

1.  Sensors collect patient-related physiological and movement data.
2.  ESP32/NodeMCU receives and processes the sensor readings.
3.  Data is transmitted using Wi-Fi/IoT communication.
4.  Backend processing performs data preparation such as filtering,
    normalization and feature extraction.
5.  The machine-learning component analyzes processed data and generates
    prediction results.
6.  Cloud storage/monitoring keeps relevant records.
7.  The Streamlit dashboard provides remote monitoring.
8.  LCD/buzzer alerts are used for abnormal conditions.

## 4. Hardware

The report lists components including:

-   ESP32 / NodeMCU
-   Pulse/heart-rate sensor
-   LCD display
-   Buzzer module
-   Power supply module
-   USB cable
-   Jumper wires
-   Breadboard
-   Laptop / computer
-   Wi-Fi connectivity

## 5. Software and Platforms

The report mentions:

-   Windows / Linux
-   Embedded C / Python
-   Arduino IDE
-   Blynk / ThingSpeak
-   MySQL / Cloud Storage
-   HTML / CSS / JavaScript
-   Flask / Django (listed under backend framework)
-   Scikit-learn, TensorFlow, Pandas, NumPy
-   Google Chrome
-   Arduino Serial Monitor
-   Streamlit dashboard in the implementation/deployment description

## 6. Testing Perspective

Testing is described as an important phase used to verify functionality,
performance, reliability and accuracy across hardware and software
components.

The major testing areas are:

### Sensor and Data Collection

Verify that sensor values are collected correctly and continuously and
that the controller receives readings without data loss.

### IoT Communication and Cloud

Verify Wi-Fi communication, transmission to the cloud/server, storage
integrity, and remote access.

### Data Processing and Machine Learning

Verify preprocessing such as filtering, normalization and feature
extraction, and verify that the prediction flow produces results without
processing errors.

### Dashboard and Alert System

Verify patient status, sensor readings, prediction results, reports,
monitoring history, buzzer behavior and LCD warnings.

### Cloud Database

Verify storage, retrieval, reliability and integrity of patient-related
records, sensor readings, prediction results and monitoring reports.

## 7. My Contribution

**Role: Manual Tester**

The testing work is documented separately in the `testing/` directory.
It is intended to demonstrate a QA-oriented contribution within the
group project without claiming ownership of the entire development
implementation.

## 8. System Design Diagrams

The repository includes the diagrams from the final project report:

- System Design Architecture
- Sequence Diagram
- Use Case Diagram
- Class Diagram
- Deployment Diagram
