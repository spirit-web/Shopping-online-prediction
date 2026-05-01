# Shopping Online Prediction

Supervised Machine Learning project using the SmartConvert dataset.

## Goal

Predict whether a customer will purchase based on online shopping behavior.

## Dataset

Place the dataset files in:

- data/training_sample.csv
- data/testing_sample.csv

## Project structure

- data/ = dataset files
- notebooks/spirit/ = Spirit analysis
- notebooks/emmy/ = Emmy analysis
- notebooks/mahtab/ = Mahtab analysis
- reports/ = figures and presentation material

## Workflow

main = final stable version  
dev = shared working branch  
analysis-spirit = Spirit work branch  
analysis-emmy = Emmy work branch  
analysis-mahtab = Mahtab work branch  

Each person works in their own analysis branch and creates a pull request into dev.

## Setup

pip install -r requirements.txt

## Example data loading

```python
import pandas as pd

train_df = pd.read_csv("../../data/training_sample.csv")
test_df = pd.read_csv("../../data/testing_sample.csv")


## Swedish dataset version

We keep the original Kaggle files and also provide Swedish-renamed copies:

- data/training_sample_svenska.csv
- data/testing_sample_svenska.csv

Target variable in Swedish:

- genomfort_bestallning

Note: Some Swedish names are adapted to fit the Webhallen case/story. The underlying 0/1 values are unchanged from the original dataset.