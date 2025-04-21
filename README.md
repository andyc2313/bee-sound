# 🐝 Bee Sound Feature Extraction & Classification

This folder contains scripts and notebooks used in the analysis of **honeybee hive internal audio data**, aiming to detect and classify environmental or biological changes based on sound features. 

## 🎯 Project Overview

The goal of this project is to monitor and classify the condition of a beehive by analyzing sound recordings collected from inside the hive. This is part of a broader effort to develop early-warning systems for colony health and stress, focusing on conditions such as:

- **Queenlessness**
- **Pesticide exposure**
- **Virus infections**

By comparing the audio characteristics **before and after experimental interventions**, this system attempts to extract meaningful features and train machine learning models (including LSTM) to detect subtle changes.

---

## 🧱 Folder Structure and Module Descriptions

### 🔹 Preprocessing & Augmentation

- `Preprocessing.ipynb`  
  Cleans and formats raw audio data for further processing. This includes renaming, trimming, converting, or normalizing audio files.

- `audio augmentation.ipynb`  
  Applies data augmentation methods such as:
  - Background noise addition
  - Time-stretching
  - Pitch shifting
  - Volume changes  
  This enhances model robustness and increases dataset diversity.

- `librosa_trans.py`  
  Utility functions for audio transformation using the `librosa` library (e.g., for speed, pitch, gain, noise).

---

### 🔹 Feature Extraction

- `mfcc feature extraction.ipynb`  
  Extracts MFCC (Mel-Frequency Cepstral Coefficients) and other statistical features from `.wav` files.

- `Feature_extraction.ipynb`  
  Integrates preprocessing, MFCC extraction, labeling, and visualization in a unified pipeline.

- `pca.ipynb`  
  Reduces feature dimensionality using Principal Component Analysis (PCA) for visualization and noise reduction.

---

### 🔹 LSTM Training

- `lstm_utils.py`  
  Contains reusable functions and LSTM model definitions (PyTorch/Keras) used for training on time-series MFCC data.

- `lstm_training.ipynb`  
  Handles dataset loading, training, validation, and testing of LSTM models to classify hive condition states based on audio input.

---

### 📦 Environment Setup

To install all dependencies, run:

```bash
pip install -r requirements.txt
