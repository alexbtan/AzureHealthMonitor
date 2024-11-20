# AzureHealthMonitor
A set of Azure functions for simulating and managing patient health data

## Functions Outline
### Function 1: DataIngestion
Uses a timer trigger and the simulation + cleaning of data to replicate the input of patient information in an SQL database through the output binding

### Function 2: HDPrediction
Uses custom ML model to predict risk of heart disease based on health metrics of patients. Uses sqltrigger and runs every time a new patient is added to HealthMetrics table in SQL database


### Function 2: DataVisualisation
Uses HTTPtrigger and returns data visualisations of key health metrics compared with heart disease predictions

## Run Instructions
Use azurite to replicate functionality of Microsoft Azure Storage locally
use func start to run the Azure functions
Requirements.txt contains all required modules

Made using Python 3.11

