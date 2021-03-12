The following is an abridged version of the directory structure from [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/). This directory structure represents a standardized way of organizing the code, data, and models for a typical data science project.

```
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
├── models             <- Trained models, predictions, or summaries
├── reports            <- Generated analysis
│   └── figures        <- Generated graphics
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then
│   │   │                 use trained models to make predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
```

Using this template, building and deploying a pipeline for a single machine learning model is a relatively straightforward process. A typical pipeline involves writing code to pre-process the data. The next stage of the pipeline usually involves code to extract features from the pre-processed data. These features serve as the input to machine learning algorithms which create a model as an output. The models and code used to generate the models are stored in git repository. Since the models and code are under version control, this means it is easy to go back to an earlier version of a model.

Starting with the [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/) as a starting guide, how could you use GitOps to automate the process of training and deploying models? How would that process work with a workflow engine like [Apache Airflow](https://airflow.apache.org/)?