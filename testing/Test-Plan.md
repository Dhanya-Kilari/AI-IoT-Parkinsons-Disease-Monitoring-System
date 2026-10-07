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

The testing was performed using the project hardware and software environment specified in the system requirements.

- Operating System: Windows
- Browser: Google Chrome
- Microcontroller: ESP32 / NodeMCU
- IoT Platform: Blynk / ThingSpeak
- Dashboard: Streamlit
- Testing: Manual testing

## 5. Entry Criteria

-   Required hardware and software are available.
-   Test environment is accessible.
-   Application/dashboard can be started.
-   Sensor inputs can be generated or collected.
-   Test data is available.

## 6. Exit Criteria

-   Planned test cases are executed.
-   Critical defects, if identified, are resolved or formally accepted.
-   Regression checks are completed.
-   Final test results are recorded.

## 7. Defect Severity

-   **Critical:** System cannot perform a core function or creates a
    major safety/security impact.
-   **High:** Important function fails and there is no practical
    workaround.
-   **Medium:** Function is affected but a workaround exists.
-   **Low:** Minor UI/content/usability issue.
