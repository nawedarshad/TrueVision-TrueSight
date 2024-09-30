# TrueSight - Source Code

## Overview

This directory contains the source code for the Deepfake Detection System. The code is primarily designed for research and structural purposes at this stage. It serves as a foundational framework for ongoing development in the field of deepfake detection.

## Current Status

- **Research Phase**: The code is currently in the research phase and may not be fully functional or optimized for production use. It is intended to provide a structure for further exploration and experimentation.
- **Development Progress**: Initial development has begun, but the code has not yet been fully updated or completed. As research progresses, code updates will be made to improve functionality, performance, and accuracy.

## Folder Structure

The `src` directory contains the following files:

- **`main.py`**: The entry point for executing the deepfake detection system. This file orchestrates the flow of data and calls relevant functions from other modules.
- **`models.py`**: Contains the definitions and implementations of various models used in the detection process, including feature extraction and classification algorithms.
- **`audio_feature_extraction.py`**: Implements methods for extracting audio features using techniques like Fast Fourier Transform (FFT) and HuBERT.
- **`video_feature_extraction.py`**: Implements methods for extracting video features using advanced neural network architectures such as FABNet and Vision Transformers.
- **`temporal_analysis.py`**: Contains functions for analyzing temporal sequences in audio and video data using LSTMs and other models.
- **`utils.py`**: Provides utility functions that support various operations throughout the codebase.

## Future Updates

- The code will be continuously updated as new techniques and improvements are discovered during research.
- Planned updates include integrating more advanced models, optimizing performance, and refining detection algorithms.
- Contributions and suggestions for improvement are welcome as the project evolves.

## Contributing

If you wish to contribute to this project or provide feedback, please refer to the `contributing.md` file in the main directory for guidelines on how to get involved.

## Disclaimer

This code is for research purposes only and should not be used for malicious intent. The development of deepfake detection technologies aims to promote ethical use of AI and prevent misinformation.

For further information, please refer to the main `README.md` in the root of the repository.
