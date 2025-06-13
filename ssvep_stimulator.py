"""
SSVEP Visual Stimulator

A PyQt5-based application for generating Steady-State Visual Evoked Potential (SSVEP) 
stimuli for neuroscience research and brain-computer interface applications.

Author: NeoGendaijin
License: MIT
"""

import sys
import math
from typing import Optional
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QLabel, QSlider, QSpinBox,
                             QFrame, QGroupBox)
from PyQt5.QtCore import QTimer, Qt, pyqtSignal
from PyQt5.QtGui import QPalette, QFont

class FlickeringWidget(QFrame):
    """
    Visual stimulus widget that flickers at a specified frequency.
    
    This widget creates a high-contrast black/white flickering pattern
    optimized for SSVEP (Steady-State Visual Evoked Potential) experiments.
    """
    
    def __init__(self, frequency: float = 10.0):
        """
        Initialize the flickering widget.
        
        Args:
            frequency: Flickering frequency in Hz (default: 10.0)
        """
        super().__init__()
        self.frequency = frequency  # Hz
        self.is_active = False
        self.is_on = False
        
        # Timer setup
        self.timer = QTimer()
        self.timer.timeout.connect(self.toggle_state)
        
        # Widget appearance settings
        self.setFrameStyle(QFrame.Box)
        self.setLineWidth(3)
        self.setMinimumSize(600, 600)
        self.setStyleSheet("background-color: black; border: 3px solid white;")
        
        # Frequency display label
        self.freq_label = QLabel(f"{frequency:.1f} Hz")
        self.freq_label.setAlignment(Qt.AlignCenter)
        self.freq_label.setFont(QFont("Arial", 16, QFont.Bold))
        self.freq_label.setStyleSheet("color: white; background-color: transparent; border: none;")
        
        layout = QVBoxLayout()
        layout.addWidget(self.freq_label)
        self.setLayout(layout)
    
    def set_frequency(self, frequency: float) -> None:
        """
        Set the flickering frequency.
        
        Args:
            frequency: New frequency in Hz
        """
        self.frequency = frequency
        self.freq_label.setText(f"{frequency:.1f} Hz")
        if self.is_active:
            self.start_flicker()
    
    def start_flicker(self) -> None:
        """Start the flickering animation."""
        if self.frequency > 0:
            interval = int(500 / self.frequency)  # Half period in milliseconds
            self.timer.start(interval)
            self.is_active = True
    
    def stop_flicker(self) -> None:
        """Stop the flickering animation and reset to black state."""
        self.timer.stop()
        self.is_active = False
        self.is_on = False
        self.setStyleSheet("background-color: black; border: 3px solid white;")
    
    def toggle_state(self) -> None:
        """Toggle between black and white states."""
        self.is_on = not self.is_on
        if self.is_on:
            self.setStyleSheet("background-color: white; border: 3px solid black;")
            self.freq_label.setStyleSheet("color: black; background-color: transparent; border: none;")
        else:
            self.setStyleSheet("background-color: black; border: 3px solid white;")
            self.freq_label.setStyleSheet("color: white; background-color: transparent; border: none;")

class FrequencyControl(QWidget):
    """
    Frequency control widget with slider and spinbox controls.
    
    Provides precise frequency adjustment for SSVEP stimuli with 0.1 Hz resolution.
    """
    
    frequency_changed = pyqtSignal(float)
    
    def __init__(self, initial_freq: float = 10.0, min_freq: float = 1.0, max_freq: float = 30.0):
        """
        Initialize the frequency control widget.
        
        Args:
            initial_freq: Initial frequency value in Hz
            min_freq: Minimum allowed frequency in Hz
            max_freq: Maximum allowed frequency in Hz
        """
        super().__init__()
        self.min_freq = min_freq
        self.max_freq = max_freq
        
        layout = QVBoxLayout()
        
        # Frequency display
        self.freq_display = QLabel(f"{initial_freq:.1f} Hz")
        self.freq_display.setAlignment(Qt.AlignCenter)
        self.freq_display.setFont(QFont("Arial", 14, QFont.Bold))
        
        # Slider control
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(int(min_freq * 10))
        self.slider.setMaximum(int(max_freq * 10))
        self.slider.setValue(int(initial_freq * 10))
        self.slider.valueChanged.connect(self.on_slider_changed)
        
        # Spinbox control
        self.spinbox = QSpinBox()
        self.spinbox.setMinimum(int(min_freq * 10))
        self.spinbox.setMaximum(int(max_freq * 10))
        self.spinbox.setValue(int(initial_freq * 10))
        self.spinbox.setSuffix(" × 0.1 Hz")
        self.spinbox.valueChanged.connect(self.on_spinbox_changed)
        
        layout.addWidget(self.freq_display)
        layout.addWidget(self.slider)
        layout.addWidget(self.spinbox)
        
        self.setLayout(layout)
    
    def on_slider_changed(self, value):
        freq = value / 10.0
        self.freq_display.setText(f"{freq:.1f} Hz")
        self.spinbox.setValue(value)
        self.frequency_changed.emit(freq)
    
    def on_spinbox_changed(self, value):
        freq = value / 10.0
        self.freq_display.setText(f"{freq:.1f} Hz")
        self.slider.setValue(value)
        self.frequency_changed.emit(freq)

class SSVEPStimulator(QMainWindow):
    """
    Main window for SSVEP visual stimulation.
    
    Provides a dual-channel SSVEP stimulator with independent frequency controls
    for neuroscience research and brain-computer interface applications.
    """
    
    def __init__(self):
        """Initialize the SSVEP stimulator main window."""
        super().__init__()
        self.init_ui()
        self.is_running = False
        
    def init_ui(self) -> None:
        """Initialize the user interface."""
        self.setWindowTitle("SSVEP Visual Stimulator")
        self.setGeometry(100, 100, 800, 600)
        
        # Main widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        # Main layout
        main_layout = QVBoxLayout()
        
        # Title
        title = QLabel("SSVEP Visual Stimulator")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setStyleSheet("margin: 10px; padding: 10px;")
        
        # Stimuli display area
        stimuli_layout = QHBoxLayout()
        
        # Left stimulus
        left_group = QGroupBox("Left Stimulus")
        left_layout = QVBoxLayout()
        
        self.left_stimulus = FlickeringWidget(frequency=10.0)
        self.left_control = FrequencyControl(initial_freq=10.0)
        self.left_control.frequency_changed.connect(self.left_stimulus.set_frequency)
        
        left_layout.addWidget(self.left_stimulus)
        left_layout.addWidget(self.left_control)
        left_group.setLayout(left_layout)
        
        # Right stimulus
        right_group = QGroupBox("Right Stimulus")
        right_layout = QVBoxLayout()
        
        self.right_stimulus = FlickeringWidget(frequency=15.0)
        self.right_control = FrequencyControl(initial_freq=15.0)
        self.right_control.frequency_changed.connect(self.right_stimulus.set_frequency)
        
        right_layout.addWidget(self.right_stimulus)
        right_layout.addWidget(self.right_control)
        right_group.setLayout(right_layout)
        
        stimuli_layout.addWidget(left_group)
        stimuli_layout.addWidget(right_group)
        
        # Control buttons
        control_layout = QHBoxLayout()
        
        self.start_button = QPushButton("Start Stimulation")
        self.start_button.clicked.connect(self.toggle_stimulation)
        self.start_button.setFont(QFont("Arial", 14))
        self.start_button.setMinimumHeight(50)
        
        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_stimulation)
        self.reset_button.setFont(QFont("Arial", 14))
        self.reset_button.setMinimumHeight(50)
        
        control_layout.addWidget(self.start_button)
        control_layout.addWidget(self.reset_button)
        
        # Usage instructions
        instruction = QLabel("""
Usage Instructions:
• Use sliders or spinboxes to adjust frequency for each stimulus
• Click "Start Stimulation" to begin/stop stimulation
• Click "Reset" to stop all stimuli and initialize
        """)
        instruction.setStyleSheet("background-color: #f0f0f0; padding: 10px; border: 1px solid #ccc; margin: 5px;")
        
        # Layout assembly
        main_layout.addWidget(title)
        main_layout.addLayout(stimuli_layout)
        main_layout.addLayout(control_layout)
        main_layout.addWidget(instruction)
        
        main_widget.setLayout(main_layout)
        
        # Window styling
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QGroupBox {
                font-weight: bold;
                border: 2px solid #ccc;
                border-radius: 5px;
                margin: 5px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
        """)
    
    def toggle_stimulation(self) -> None:
        """Toggle stimulation start/stop."""
        if not self.is_running:
            self.left_stimulus.start_flicker()
            self.right_stimulus.start_flicker()
            self.start_button.setText("Stop Stimulation")
            self.start_button.setStyleSheet("""
                QPushButton {
                    background-color: #f44336;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    padding: 5px;
                }
                QPushButton:hover {
                    background-color: #da190b;
                }
                QPushButton:pressed {
                    background-color: #c1170a;
                }
            """)
            self.is_running = True
        else:
            self.left_stimulus.stop_flicker()
            self.right_stimulus.stop_flicker()
            self.start_button.setText("Start Stimulation")
            self.start_button.setStyleSheet("")
            self.is_running = False
    
    def reset_stimulation(self) -> None:
        """Reset all stimulation to initial state."""
        self.left_stimulus.stop_flicker()
        self.right_stimulus.stop_flicker()
        self.start_button.setText("Start Stimulation")
        self.start_button.setStyleSheet("")
        self.is_running = False

def main() -> None:
    """
    Main function to run the SSVEP Visual Stimulator application.
    """
    app = QApplication(sys.argv)
    
    # Set application style
    app.setStyle('Fusion')
    
    window = SSVEPStimulator()
    window.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
