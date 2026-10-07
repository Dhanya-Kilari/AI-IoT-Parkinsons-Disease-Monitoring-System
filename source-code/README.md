# Team Source Code

This folder contains the **team implementation source code** for the academic project.

## My Role

**Primary role: Manual Tester**

The source code is included for project reference. It should **not** be interpreted as code personally developed or solely owned by me.

My contribution is documented in the [`testing/`](../testing/) directory through the test plan, test scenarios, test cases, and defect-reporting documentation.

## Files

- `advanced_gui.py` — PyQt5-based monitoring dashboard with live cards, graph, ThingSpeak data retrieval, status logic, and alerts.
- `live_dashboard.py` — simplified PyQt5 live health dashboard with BPM, EMG/pulse status, movement status, and a live BPM graph.

## Security / Public GitHub Version

The original team files contained a ThingSpeak read API key directly in the source code. For public GitHub publication, that credential has been removed and replaced with environment variables.

Set these variables before running the dashboards:

```text
THINGSPEAK_CHANNEL_ID=your_channel_id
THINGSPEAK_READ_API_KEY=your_read_api_key
```

Do **not** commit real API keys, passwords, tokens, Wi-Fi credentials, or other secrets.

## Python Packages

The dashboards use:

- Python
- PyQt5
- Requests
- PyQtGraph

Install the required packages with:

```bash
pip install PyQt5 requests pyqtgraph
```

## Run

From this directory, after configuring the environment variables:

```bash
python advanced_gui.py
```

or

```bash
python live_dashboard.py
```
