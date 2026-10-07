## Test Scenarios

| Scenario ID | Module | Test Scenario |
|---|---|---|
| TS-001 | Sensor Data Collection | Verify that the sensors collect patient health data correctly. |
| TS-002 | Sensor Data Collection | Verify continuous collection of sensor data. |
| TS-003 | Sensor Data Collection | Verify that heartbeat, tremor and movement-related data are captured. |
| TS-004 | Controller | Verify that ESP32/NodeMCU receives sensor data correctly. |
| TS-005 | Controller | Verify that the controller processes the received sensor data correctly. |
| TS-006 | IoT Communication | Verify Wi-Fi communication between ESP32/NodeMCU and the server/cloud platform. |
| TS-007 | IoT Communication | Verify that processed sensor data is transmitted successfully. |
| TS-008 | Cloud | Verify that sensor data is stored correctly in the cloud platform. |
| TS-009 | Cloud | Verify retrieval of stored patient monitoring data. |
| TS-010 | Data Processing | Verify that raw sensor data is processed and prepared for analysis. |
| TS-011 | Data Processing | Verify noise filtering and normalization of sensor data. |
| TS-012 | Machine Learning | Verify that processed data is passed to the machine learning model. |
| TS-013 | Machine Learning | Verify that the XGBoost model generates prediction results. |
| TS-014 | Machine Learning | Verify prediction results for valid patient data. |
| TS-015 | Dashboard | Verify that patient health data is displayed correctly on the dashboard. |
| TS-016 | Dashboard | Verify that prediction results are displayed correctly. |
| TS-017 | Dashboard | Verify that monitoring history and graphical information are displayed correctly. |
| TS-018 | Alert System | Verify that the buzzer and LCD alerts are activated for abnormal conditions. |
| TS-019 | Alert System | Verify that alert notifications are generated when abnormal conditions are detected. |
| TS-020 | Regression | Verify affected functionality after system changes. |
| TS-021 | Cloud Database | Verify that stored data is not lost or corrupted. |
