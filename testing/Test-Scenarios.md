# Test Scenarios

  -------------------------------------------------------------------------
  Scenario ID             Module                  Test Scenario
  ----------------------- ----------------------- -------------------------
  TS-001                  Sensor                  Verify that the sensor
                                                  collects patient-related
                                                  readings.

  TS-002                  Sensor                  Verify continuous sensor
                                                  data collection.

  TS-003                  Controller              Verify that ESP32/NodeMCU
                                                  receives sensor readings.

  TS-004                  Controller              Verify that sensor data
                                                  is not lost during normal
                                                  operation.

  TS-005                  IoT                     Verify Wi-Fi/IoT
                                                  connection between
                                                  controller and
                                                  server/cloud.

  TS-006                  IoT                     Verify transmission of
                                                  processed sensor data.

  TS-007                  Cloud                   Verify that transmitted
                                                  data is stored correctly.

  TS-008                  Cloud                   Verify retrieval of
                                                  stored monitoring data.

  TS-009                  Processing              Verify noise
                                                  filtering/preprocessing
                                                  flow.

  TS-010                  Processing              Verify
                                                  normalization/feature
                                                  preparation flow.

  TS-011                  ML                      Verify prediction request
                                                  with valid processed
                                                  data.

  TS-012                  ML                      Verify system behavior
                                                  for invalid/incomplete
                                                  input.

  TS-013                  Dashboard               Verify sensor readings
                                                  are displayed correctly.

  TS-014                  Dashboard               Verify prediction results
                                                  are displayed.

  TS-015                  Dashboard               Verify monitoring
                                                  history/report
                                                  information is displayed.

  TS-016                  Alert                   Verify buzzer activation
                                                  for abnormal conditions.

  TS-017                  Alert                   Verify LCD warning
                                                  display for abnormal
                                                  conditions.

  TS-018                  Alert                   Verify notification flow
                                                  for abnormal conditions.

  TS-019                  Integration             Verify sensor →
                                                  controller → server/cloud
                                                  → dashboard flow.

  TS-020                  Regression              Re-test affected
                                                  functionality after a
                                                  defect fix.

  TS-021                  Cloud Database          Verify no unintended data
                                                  loss/corruption during
                                                  storage.

  TS-022                  Cloud Database          Verify authorized users
                                                  can retrieve monitoring
                                                  information.
  -------------------------------------------------------------------------
