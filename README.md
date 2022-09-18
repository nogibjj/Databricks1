# Fakenews Detection Check!
A repo to assimilate databricks and fastapi


## API Explanation for the Project
![API_databricks](https://user-images.githubusercontent.com/112578755/190914864-afd04731-35f1-4458-902f-c0b0ac791a4d.jpg)


## Data Source
[Kaggle Dataset](https://www.kaggle.com/datasets/ruchi798/source-based-news-classification?resource=download)

This is the dataset containing content posted by politicians, news channels, newspaper websites, or even common civilians on social media. It has been a concern that social media provides the room for people spreading mis-information. The creators of the dataset have classified all the articels into 'Fake' and 'Real' label, which the project will mainly use to design the interactive web app.


## Goal of the Project

The project aims to design an interactive small game of identifying fake news. 

* First, Databricks is used to upload the `news articles` dataset and connect it with codespaces by using the microservice(FastAPI) and the command-line tool(click and app). 

* fakenews_app is the main code of the project that users can see the overall fakenews trend in the dataset, e.g. what are those authors generating the fakenews. Additionally, users can randomly select a number (up to 2078) and read the article to guess it is fake news or real news. 

* The goal of the project is to let users experience their sense of detecting fake news! It might hopefully help readers to be more cautious when they are reading news articles in their daily life.

## Demo of the project


## Setup auth

[databricks-python](https://docs.microsoft.com/en-us/azure/databricks/dev-tools/python-api)

Place in Codespace secrets
* [unix, linux, mac](https://docs.microsoft.com/en-us/azure/databricks/dev-tools/python-api#unixlinuxandmacos)

```bash
DATABRICKS_HOST
DATABRICKS_TOKEN
DATABRICKS_SERVER_HOSTNAME
DATABRICKS_HTTP_PATH
```

## Test out CLI

```
databricks clusters list --output JSON | jq
databricks fs ls dbfs:/
databricks jobs list --output JSON | jq
```
## Remote connect

[databricks-connect](https://docs.databricks.com/dev-tools/databricks-connect.html)

## Databricks SQL Connector

[Setup table first!](https://docs.databricks.com/dbfs/databricks-datasets.html)

[sql remote](https://docs.databricks.com/dev-tools/python-sql-connector.html)
https://docs.databricks.com/integrations/bi/jdbc-odbc-bi.html#connection-details-cluster