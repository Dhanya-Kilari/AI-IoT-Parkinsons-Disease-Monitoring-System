import sys
import os
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QVBoxLayout, QHBoxLayout, QFrame
)
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont
import pyqtgraph as pg


# =========================
# THINGSPEAK CONFIG
# =========================

CHANNEL_ID = os.getenv("THINGSPEAK_CHANNEL_ID", "")
READ_API_KEY = os.getenv("THINGSPEAK_READ_API_KEY", "")

URL = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds/last.json?api_key={READ_API_KEY}"


# =========================
# MAIN WINDOW
# =========================

class HealthMonitor(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("IoT Health Monitoring System")
        self.setGeometry(200, 100, 900, 500)

        self.setStyleSheet("""
            QWidget {
                background-color: #111;
                color: white;
            }
        """)

        # =========================
        # TITLE
        # =========================

        title = QLabel("LIVE HEALTH MONITOR")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        # =========================
        # BPM CARD
        # =========================

        self.bpmLabel = QLabel("--")
        self.bpmLabel.setFont(QFont("Arial", 40, QFont.Bold))
        self.bpmLabel.setAlignment(Qt.AlignCenter)

        bpmTitle = QLabel("BPM")
        bpmTitle.setAlignment(Qt.AlignCenter)

        bpmFrame = self.createCard(bpmTitle, self.bpmLabel)

        # =========================
        # ECG CARD
        # =========================

        self.ecgLabel = QLabel("Unknown")
        self.ecgLabel.setFont(QFont("Arial", 25))

        ecgTitle = QLabel("EMG Status")
        ecgTitle.setAlignment(Qt.AlignCenter)

        ecgFrame = self.createCard(ecgTitle, self.ecgLabel)

        # =========================
        # GYRO CARD
        # =========================

        self.gyroLabel = QLabel("Unknown")
        self.gyroLabel.setFont(QFont("Arial", 25))

        gyroTitle = QLabel("Movement")
        gyroTitle.setAlignment(Qt.AlignCenter)

        gyroFrame = self.createCard(gyroTitle, self.gyroLabel)

        # =========================
        # TOP LAYOUT
        # =========================

        topLayout = QHBoxLayout()

        topLayout.addWidget(bpmFrame)
        topLayout.addWidget(ecgFrame)
        topLayout.addWidget(gyroFrame)

        # =========================
        # GRAPH
        # =========================

        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setBackground("#222")

        self.graphWidget.setTitle("Live BPM Graph")

        self.graphWidget.showGrid(x=True, y=True)

        self.x = list(range(20))
        self.y = [0] * 20

        self.line = self.graphWidget.plot(
            self.x,
            self.y,
            pen=pg.mkPen(width=3)
        )

        # =========================
        # MAIN LAYOUT
        # =========================

        layout = QVBoxLayout()

        layout.addWidget(title)
        layout.addLayout(topLayout)
        layout.addWidget(self.graphWidget)

        self.setLayout(layout)

        # =========================
        # TIMER
        # =========================

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateData)
        self.timer.start(3000)

    # =========================
    # CARD UI
    # =========================

    def createCard(self, title, value):

        frame = QFrame()

        frame.setStyleSheet("""
            QFrame {
                background-color: #222;
                border-radius: 15px;
                padding: 20px;
            }
        """)

        layout = QVBoxLayout()

        layout.addWidget(title)
        layout.addWidget(value)

        frame.setLayout(layout)

        return frame

    # =========================
    # FETCH DATA
    # =========================

    def updateData(self):

        try:

            response = requests.get(URL)

            data = response.json()

            bpm = data['field1']
            ecg = data['field2']
            gyro = data['field3']

            # =========================
            # BPM
            # =========================

            self.bpmLabel.setText(str(bpm))

            self.y = self.y[1:]
            self.y.append(int(float(bpm)))

            self.line.setData(self.x, self.y)

            # =========================
            # ECG
            # =========================

            if ecg == "1":
                self.ecgLabel.setText("Pulse Detected")
            else:
                self.ecgLabel.setText("No Pulse")

            # =========================
            # GYRO
            # =========================

            if gyro == "1":
                self.gyroLabel.setText("Movement")
            else:
                self.gyroLabel.setText("Stable")

        except Exception as e:
            print("Error:", e)


# =========================
# RUN APP
# =========================

app = QApplication(sys.argv)

window = HealthMonitor()
window.show()

sys.exit(app.exec_())