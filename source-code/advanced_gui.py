import sys
import os
import requests
from datetime import datetime

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
   QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QGridLayout,
)

import pyqtgraph as pg


# =========================================================
# THINGSPEAK CONFIG
# =========================================================

CHANNEL_ID = os.getenv("THINGSPEAK_CHANNEL_ID", "")
READ_API_KEY = os.getenv("THINGSPEAK_READ_API_KEY", "")

URL = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds/last.json?api_key={READ_API_KEY}"


# =========================================================
# MAIN WINDOW
# =========================================================

class ParkinsonMonitor(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "AI AND IOT BASED PARKINSON’S DISEASE PREDICTION AND MONITORING SYSTEM"
        )

        self.setGeometry(100, 50, 1400, 800)

        # =========================================================
        # DARK THEME
        # =========================================================

        self.setStyleSheet("""
            QWidget {
                background-color: #0f1117;
                color: white;
                font-family: Arial;
            }
        """)

        # =========================================================
        # TITLE
        # =========================================================

        title = QLabel(
            "AI AND IOT BASED PARKINSON’S DISEASE PREDICTION AND MONITORING SYSTEM"
        )

        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        subtitle = QLabel(
            "Real-Time Patient Health Monitoring Dashboard"
        )

        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("color: #00d4ff;")

        # =========================================================
        # LIVE CLOCK
        # =========================================================

        self.timeLabel = QLabel()
        self.timeLabel.setFont(QFont("Arial", 12))
        self.timeLabel.setAlignment(Qt.AlignRight)

        # =========================================================
        # CARDS
        # =========================================================

        self.bpmValue = QLabel("--")
        self.bpmValue.setFont(QFont("Arial", 38, QFont.Bold))

        self.ecgValue = QLabel("Unknown")
        self.ecgValue.setFont(QFont("Arial", 24))

        self.gyroValue = QLabel("Unknown")
        self.gyroValue.setFont(QFont("Arial", 24))

        self.statusValue = QLabel("Monitoring")
        self.statusValue.setFont(QFont("Arial", 24, QFont.Bold))

        bpmCard = self.createCard(
            "Heart Rate (BPM)",
            self.bpmValue,
            "#00d4ff"
        )

        ecgCard = self.createCard(
            "EMG Status",
            self.ecgValue,
            "#00ff99"
        )

        gyroCard = self.createCard(
            "Movement Detection",
            self.gyroValue,
            "#ffcc00"
        )

        statusCard = self.createCard(
            "Patient Status",
            self.statusValue,
            "#ff4d4d"
        )

        # =========================================================
        # GRID LAYOUT
        # =========================================================

        grid = QGridLayout()

        grid.addWidget(bpmCard, 0, 0)
        grid.addWidget(ecgCard, 0, 1)
        grid.addWidget(gyroCard, 1, 0)
        grid.addWidget(statusCard, 1, 1)

        # =========================================================
        # BPM GRAPH
        # =========================================================

        self.graphWidget = pg.PlotWidget()

        self.graphWidget.setBackground("#161b22")

        self.graphWidget.setTitle(
            "Live Heart Rate Monitoring",
            color="w",
            size="16pt"
        )

        self.graphWidget.showGrid(x=True, y=True)

        self.graphWidget.setLabel('left', 'BPM')
        self.graphWidget.setLabel('bottom', 'Time')

        self.x = list(range(50))
        self.y = [0] * 50

        self.line = self.graphWidget.plot(
            self.x,
            self.y,
            pen=pg.mkPen('#00d4ff', width=3)
        )

        # =========================================================
        # ALERT BOX
        # =========================================================

        self.alertLabel = QLabel("System Running Normally")

        self.alertLabel.setAlignment(Qt.AlignCenter)

        self.alertLabel.setStyleSheet("""
            background-color: #1f2937;
            border-radius: 12px;
            padding: 15px;
            color: #00ff99;
            font-size: 16px;
            font-weight: bold;
        """)

        # =========================================================
        # MAIN LAYOUT
        # =========================================================

        layout = QVBoxLayout()

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(self.timeLabel)
        layout.addSpacing(10)

        layout.addLayout(grid)

        layout.addSpacing(20)

        layout.addWidget(self.graphWidget)

        layout.addSpacing(20)

        layout.addWidget(self.alertLabel)

        self.setLayout(layout)

        # =========================================================
        # TIMER
        # =========================================================

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateData)
        self.timer.timeout.connect(self.updateClock)

        self.timer.start(3000)

    # =========================================================
    # CARD CREATOR
    # =========================================================

    def createCard(self, titleText, valueWidget, color):

        frame = QFrame()

        frame.setStyleSheet(f"""
            QFrame {{
                background-color: #161b22;
                border: 2px solid {color};
                border-radius: 20px;
                padding: 20px;
            }}
        """)

        title = QLabel(titleText)
        title.setFont(QFont("Arial", 15, QFont.Bold))
        title.setStyleSheet(f"color: {color};")

        layout = QVBoxLayout()

        layout.addWidget(title)
        layout.addSpacing(15)
        layout.addWidget(valueWidget)

        frame.setLayout(layout)

        return frame

    # =========================================================
    # UPDATE CLOCK
    # =========================================================

    def updateClock(self):

        current = datetime.now().strftime("%d-%m-%Y  %I:%M:%S %p")

        self.timeLabel.setText(current)

    # =========================================================
    # FETCH THINGSPEAK DATA
    # =========================================================

    def updateData(self):

        try:

            response = requests.get(URL)

            data = response.json()

            bpm = data.get('field1', '0')
            ecg = data.get('field2', '0')
            gyro = data.get('field3', '0')

            bpm = int(float(bpm))

            # =========================================================
            # BPM
            # =========================================================

            self.bpmValue.setText(str(bpm))

            self.y = self.y[1:]
            self.y.append(bpm)

            self.line.setData(self.x, self.y)

            # =========================================================
            # ECG STATUS
            # =========================================================

            if ecg == "1":

                self.ecgValue.setText("Pulse Detected")
                self.ecgValue.setStyleSheet("color: #00ff99;")

            else:

                self.ecgValue.setText("No Pulse")
                self.ecgValue.setStyleSheet("color: red;")

            # =========================================================
            # GYRO STATUS
            # =========================================================

            if gyro == "1":

                self.gyroValue.setText("Movement Detected")
                self.gyroValue.setStyleSheet("color: orange;")

            else:

                self.gyroValue.setText("Stable")
                self.gyroValue.setStyleSheet("color: #00ff99;")

            # =========================================================
            # AI STATUS LOGIC
            # =========================================================

            if bpm < 50 or bpm > 120:

                self.statusValue.setText("Abnormal")
                self.statusValue.setStyleSheet("color: red;")

                self.alertLabel.setText(
                    "ALERT : Abnormal Heart Rate Detected"
                )

                self.alertLabel.setStyleSheet("""
                    background-color: #3b0d0d;
                    border-radius: 12px;
                    padding: 15px;
                    color: red;
                    font-size: 16px;
                    font-weight: bold;
                """)

            elif gyro == "1":

                self.statusValue.setText("Movement Alert")
                self.statusValue.setStyleSheet("color: orange;")

                self.alertLabel.setText(
                    "Tremor / Movement Activity Detected"
                )

                self.alertLabel.setStyleSheet("""
                    background-color: #332400;
                    border-radius: 12px;
                    padding: 15px;
                    color: orange;
                    font-size: 16px;
                    font-weight: bold;
                """)

            else:

                self.statusValue.setText("Normal")
                self.statusValue.setStyleSheet("color: #00ff99;")

                self.alertLabel.setText(
                    "Patient Condition Stable"
                )

                self.alertLabel.setStyleSheet("""
                    background-color: #0f2e1f;
                    border-radius: 12px;
                    padding: 15px;
                    color: #00ff99;
                    font-size: 16px;
                    font-weight: bold;
                """)

        except Exception as e:

            print("Error:", e)

            self.alertLabel.setText("Connection Error")

            self.alertLabel.setStyleSheet("""
                background-color: #3b0d0d;
                border-radius: 12px;
                padding: 15px;
                color: red;
                font-size: 16px;
                font-weight: bold;
            """)


# =========================================================
# RUN APPLICATION
# =========================================================

app = QApplication(sys.argv)

window = ParkinsonMonitor()
window.showMaximized()

sys.exit(app.exec_())