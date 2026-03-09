# llm-sql-analytics-agent
AI analytics agent that converts natural language queries into SQL and retrieves insights from structured datasets using LLMs.
# LLM SQL Analytics Agent

## Overview

This project explores how large language models can simplify the way people interact with data. In many analytics environments, extracting insights from structured datasets requires writing SQL queries, which can be difficult for users who are not familiar with database schemas or query syntax.

The goal of this project is to build a lightweight analytics agent that allows users to ask questions in natural language and receive answers directly from a structured dataset. Instead of manually writing SQL queries, the system uses an LLM to translate the question into SQL, run the query against the dataset, and return the results.

The project simulates a common scenario in analytics platforms where teams want to enable self-serve data exploration for analysts, product teams, or business stakeholders.

## What the Project Does

The system accepts a natural language question such as:

"What is the average task completion time by region?"

The agent processes the question in the following steps:

1. The question is sent to a language model.
2. The model generates a SQL query based on the dataset schema.
3. The query is executed against the analytics database.
4. The results are returned to the user.

This allows users to explore datasets without needing to know SQL.

## Dataset

For demonstration purposes, the project uses a small structured dataset that represents task data from an analytics pipeline. Each record contains information such as:

- task id  
- region  
- worker id  
- task type  
- completion time  
- task cost  
- quality score  

Although the dataset is small, the architecture is designed to mirror the workflow used in larger analytics systems.

## Project Structure

The repository is organized into separate modules so that each component of the system is easy to understand and modify.

config  
Contains configuration settings for the database and model.

data  
Stores the dataset used for analytics queries.

src/ingestion  
Handles dataset loading and preprocessing.

src/database  
Manages the database connection and executes SQL queries.

src/analytics  
Computes basic dataset metrics such as averages and distributions.

src/llm  
Contains the logic that converts natural language questions into SQL queries.

src/agent  
Combines the LLM and database components to create the analytics agent.

src/pipelines  
Runs the end-to-end pipeline that loads the dataset, stores it in the database, and executes example queries.

## Example Workflow

A typical workflow with the system looks like this:

1. Load the dataset into the analytics database.
2. Initialize the analytics agent.
3. Ask a natural language question.
4. The agent generates a SQL query.
5. The query is executed and results are returned.

Example question:

What is the average task completion time by region?

The agent generates the SQL query and retrieves the answer automatically.

## Technologies Used

Python  
Pandas  
NumPy  
SQLAlchemy  
SQLite  
OpenAI API

## Why I Built This

I wanted to experiment with how generative AI can make analytics workflows more accessible. Many teams rely heavily on SQL to extract insights from their data, and natural language interfaces have the potential to make those systems easier to use.

This project is a small prototype that demonstrates how LLMs can act as a bridge between natural language questions and structured data queries.

## Possible Improvements

There are several directions this project could be extended:

- connecting the system to a cloud data warehouse such as Snowflake or BigQuery  
- adding query validation and safety checks  
- supporting larger datasets  
- building a simple UI for asking questions interactively  
- adding query caching or optimization  

## Author

Varsha C  
MS Data Science – University of North Texas
