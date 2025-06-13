# SSVEP Visual Stimulator

A PyQt5-based application for generating Steady-State Visual Evoked Potential (SSVEP) stimuli for neuroscience research and brain-computer interface applications.

## Overview

SSVEP (Steady-State Visual Evoked Potential) is a natural response to visual stimuli flickering at specific frequencies. This application provides a dual-channel visual stimulator that can generate precise flickering patterns at customizable frequencies, commonly used in:

- Brain-Computer Interface (BCI) research
- Neuroscience experiments
- Cognitive load assessment
- Attention and perception studies

## Features

- **Dual-channel stimulation**: Independent left and right visual stimuli
- **Precise frequency control**: Adjustable from 1.0 to 30.0 Hz with 0.1 Hz precision
- **Real-time control**: Start/stop and reset functionality
- **Visual feedback**: Clear frequency display and state indication
- **User-friendly interface**: Intuitive sliders and controls

## Installation

### Using Poetry (Recommended)

```bash
# Clone the repository
git clone <your-repo-url>
cd SSVEP

# Install dependencies with Poetry
poetry install

# Run the application
poetry run python ssvep_stimulator.py
```

### Using pip

```bash
# Clone the repository
git clone <your-repo-url>
cd SSVEP

# Install dependencies
pip install -r requirements.txt

# Run the application
python ssvep_stimulator.py
```

## Requirements

- Python >= 3.13
- PyQt5 >= 5.15.11

## Usage

1. **Launch the application**:
   ```bash
   poetry run python ssvep_stimulator.py
   ```

2. **Set frequencies**:
   - Use sliders or spin boxes to adjust the frequency for each stimulus
   - Left stimulus: Default 10.0 Hz
   - Right stimulus: Default 15.0 Hz

3. **Control stimulation**:
   - Click "Start Stimulation" to begin flickering
   - Click "Stop Stimulation" to pause
   - Click "Reset" to stop and reset all stimuli

## Technical Details

### SSVEP Background

Steady-State Visual Evoked Potentials (SSVEPs) are neural oscillations from the visual cortex that occur when a person views a visual stimulus flickering at a fixed frequency. The brain's response contains strong spectral power at the flickering frequency and its harmonics.

### Implementation

- **Timing precision**: Uses QTimer for accurate timing control
- **Visual rendering**: High-contrast black/white alternation for maximum SSVEP response
- **Frequency range**: 1-30 Hz (optimal SSVEP range)
- **Dual stimuli**: Enables frequency-division multiplexing for multi-class BCI

### Frequency Recommendations

- **Alpha band (8-12 Hz)**: Strong SSVEP responses, good for relaxed states
- **Beta band (13-30 Hz)**: Clear responses, good for active attention tasks
- **Avoid 50/60 Hz**: Power line interference in EEG recordings

## Development

### Project Structure

```
SSVEP/
├── ssvep_stimulator.py    # Main application
├── pyproject.toml         # Poetry configuration
├── poetry.lock           # Dependency lock file
├── requirements.txt      # Pip requirements
└── README.md            # This file
```

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Citation

If you use this software in your research, please cite:

```bibtex
@software{ssvep_stimulator,
  title={SSVEP Visual Stimulator},
  author={NeoGendaijin},
  year={2024},
  url={<your-repo-url>}
}
```

## Acknowledgments

- Built with PyQt5
- Inspired by neuroscience research community needs
- Designed for BCI and cognitive research applications

## Support

For questions, issues, or contributions, please open an issue on the GitHub repository.
