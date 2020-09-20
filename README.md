# Python3 🐍 & PostgreSQL 🐘

This repository contains concepts and code related to apply CRUD operations using Python3 and PostgreSQL. Feel free to go through the repository and contribute/raise-issues if needed.

## Dependencies

- Install Python3 from **[here](https://www.python.org/downloads/)**.
  - Installation Validation Steps: Open terminal and type in **`python3 --version`** (for linux/macOS) or **`py -3 --version`** (for windows).
- Install PostgreSQL from **[here](https://www.postgresql.org/download/)**.
  - Installation Validation Steps: Open **`psql`** from your terminal, or from the start.
  - Prompt will be asked for password, type it, and we're using PostgreSQL successfully &mdash; which means it was successfully installed.
- After Installing Python3, open a directory &mdash; say `pypostgres` (we can name it however we want) and inside it, run the following command: **`pip3 install virtualenv`**. Now make a virtual environment in python inside the `pypostgres` directory using the command **`source ./Scripts/activate`** (for linux/macOS) [for Windows, run the command: **`./Scripts/activate`**], to run the environment. To stop the virtual environment, we can use the command: **`deactivate`** w.r.t the virtual environment.

## Contents

### PostgreSQL Basics Using `psql`

1. Database Initialization Commands
   - DB Creation: **`CREATE DATABASE db_name;`**
   - List all the DBs: **`\l`**
   - Switching DBs: **`\c db_name`**
2. Relation/Table Initialization
   - Creating a Table: **<code>CREATE TABLE *table_name* (*attr_1* *dtype_1*, *attr_2* *dtype_2*, *attr_3* *dtype_3*, ..., *attr_n* *dtype_n*);</code>** <br>
   Example Usage: **<code>CREATE TABLE students(name text, address text, age int, number int);</code>**
3. Data Insertion into Relations
   - Insert Single Record: **<code>INSERT INTO *table_name* (*attr_1*, *attr_2*, *attr_3*, ..., *attr_n*) VALUES (*val_1*, *val_2*, *val_3*, ..., *val_n*);</code>** <br> Example Usage: **<code>INSERT INTO students(name, address, age, number) VALUES('Ram', 'Hyd', 25, 81878);</code>**
4. Querying Records From Relation
   - Query All Records: **<code>SELECT * FROM *table_name*;</code>** <br> Example Usage: **<code>SELECT * FROM students;</code>**
   - Querying Records w.r.t a Condition: **<code>SELECT * FROM *table_name* WHERE *condition*;</code>** <br> Example Usage: **<code>SELECT * FROM students WHERE number=81878;</code>**
