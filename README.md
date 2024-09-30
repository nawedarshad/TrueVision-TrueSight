# TrueVision-TrueSight

## Introduction
Deepfake technology manipulates visual and audio data to create realistic forgeries, posing significant threats to media integrity. This project aims to combat deepfakes by using state-of-the-art machine learning models like Convolutional Neural Networks (CNNs), Recurrent Neural Networks (RNNs), and Generative Adversarial Networks (GANs). The project covers both how deepfakes work and the most effective methods to detect them.

## Repository Structure
- `/src`: Contains the source code for training and evaluating deepfake detection models.
- `/data`: Sample datasets to test and replicate the models.
- `/docs`: In-depth documentation on deepfake mechanisms, detection techniques, tools, and innovations.
- `/notebooks`: Jupyter notebooks demonstrating the deepfake detection pipeline.
- `/models`: Pre-trained models that can be used for quick testing and evaluation.

## Key Features
- **Multimodal Detection**: Combining visual and audio analysis.
- **Blockchain Verification**: Ensuring media authenticity.
- **Explainable AI (XAI)**: Explaining the decisions made by the detection models.
- **Advanced Algorithms**: CNNs, RNNs, GAN Fingerprints, Capsule Networks, Transformer Networks.

## Technologies Used
- **Python**
- **TensorFlow / PyTorch**
- **OpenCV / Dlib**
- **Deepware Scanner**
- **Blockchain for verification**
- **FaceForensics++**

---

## Setup Instructions

### Prerequisites
- Python 3.8+
- TensorFlow/PyTorch
- OpenCV

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/nawedarshad/TrueVision-TrueSight.git
    cd TrueVision-TrueSight
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Download sample data from FaceForensics++ and place it in the `/data` folder.

### Running the Models
```bash
python src/main.py
