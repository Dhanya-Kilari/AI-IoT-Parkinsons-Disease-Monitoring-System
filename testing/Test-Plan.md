# Manual Testing -- Test Plan

## 1. Purpose

This test plan defines the manual testing coverage for the AI and IoT
Based Parkinson's Disease Prediction and Monitoring System.

## 2. Scope

Testing covers the functional interaction between:

-   Sensor/data collection
-   ESP32/NodeMCU controller
-   IoT/Wi-Fi communication
-   Backend/data processing
-   Machine-learning prediction flow
-   Cloud storage
-   Streamlit dashboard
-   LCD and buzzer alert behavior

## 3. Testing Types

The repository focuses on practical manual QA coverage:

-   Functional Testing
-   Integration Testing
-   System Testing
-   UI Testing
-   Negative Testing
-   Regression Testing
-   Basic usability verification
-   Cloud data/storage verification

## 4. Test Environment

Use the actual team environment when executing the cases. Record the
real versions/devices before marking execution results.

Suggested fields to record:

-   OS:
-   Browser:
-   ESP32/NodeMCU version/board:
-   Sensor configuration:
-   Backend version:
-   Dashboard URL/environment:
-   Cloud platform:
-   Test date:
-   Tester:

## 5. Entry Criteria

-   Required hardware and software are available.
-   Test environment is accessible.
-   Application/dashboard can be started.
-   Sensor inputs can be generated or collected.
-   Test data is available.

## 6. Exit Criteria

-   Planned test cases are executed.
-   Critical defects are resolved or formally accepted.
-   Regression checks are completed.
-   Final test results are recorded.

## 7. Defect Severity

-   **Critical:** System cannot perform a core function or creates a
    major safety/security impact.
-   **High:** Important function fails and there is no practical
    workaround.
-   **Medium:** Function is affected but a workaround exists.
-   **Low:** Minor UI/content/usability issue.

## 8. Important Note

The test cases in this repository are derived from the functionality and
testing areas described in the project report. Execution results must be
filled using the team's actual observations. Do not mark a case as
Pass/Fail without performing the test.
