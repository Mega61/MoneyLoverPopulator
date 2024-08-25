**README.md**
===============

**Money Lover Data Analysis**
---------------------------

A data analysis project for Money Lover, a personal finance management application. This repository contains the code for data processing, transformation, and analysis.

**Project Structure**
--------------------

The project is organized into the following directories:

* `src`: Source code for the project
* `src/models`: Database models for Money Lover data
* `src/facades`: API facades for interacting with Money Lover APIs
* `src/tests`: Unit tests for the project
* `src/conversion.json`: Category conversion data

**Key Features**
----------------

* Data processing and transformation for Money Lover data
* API facades for interacting with Money Lover APIs
* Unit tests for ensuring data integrity and accuracy
* Category conversion data for mapping Money Lover categories to custom categories

**Getting Started**
-------------------

1. Clone the repository: `git clone https://github.com/your-username/money-lover-data-analysis.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Configure environment variables: `cp .env.example .env` and update the values as needed
4. Run the data processing script: `python src/main.py`

**.env variables explained**
----------------------

The **MONEYLOVER** app actually does not have a public API documentation that allows it users to consume the data stored there. This repo was by reverse engineering the public github repo for the moneylover CLI.
The 3 Variables that you will need to connect to your **MONEYLOVER** account are:

1. EMAIL: This variable is the email that you use to login to the **MONEYLOVER** app.
2. PASSWORD: This variable is the password that you use to login to the **MONEYLOVER** app
3. BASE_URL: The base url as of this date is `https://web.moneylover.me/api` This could change in a future. Beware of this!

**API Documentation**
----------------------

API documentation can be found in the `src/facades` directory.

**Contributing**
---------------

Contributions are welcome! Please submit a pull request with a clear description of the changes.

**License**
----------

This project is licensed under the MIT License. See `LICENSE` for details.

Note: This is a generated README.md content based on the provided repository. You may need to modify it to better suit your project's specific needs.
