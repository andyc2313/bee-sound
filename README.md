# 🐝 Bee Sound Feature Extraction

This folder contains all scripts and notebooks related to preprocessing, feature extraction, augmentation, and model training for analyzing bee sounds.

## 📄 Contents

- `Preprocessing.ipynb`  
  Raw data cleaning and formatting.

- `audio augmentation.ipynb`  
  Adds noise, pitch shift, time stretch, and volume gain to diversify audio data.

- `mfcc feature extraction.ipynb`  
  Extracts MFCC and other features from audio signals.

- `Feature_extraction.ipynb`  
  Combined processing and feature workflow notebook.

- `pca.ipynb`  
  Applies Principal Component Analysis for dimensionality reduction.

- `librosa_trans.py`  
  Helper functions for librosa-based transformations.

- `lstm_utils.py`  
  Custom LSTM utilities (model definitions, data preparation, etc.).

- `lstm_training.ipynb`  
  Notebook for training and evaluating LSTM models on the extracted features.

- `requirements.txt`  
  Dependencies for the entire feature extraction + model pipeline.
