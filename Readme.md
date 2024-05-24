# Account Management API

## Overview

This project implements an Account Management API using Flask and Flask-RESTful. The API supports operations to create, retrieve, update, and delete accounts. The update operation is implemented to work similarly to a PATCH request, updating only the fields provided in the request.
## Postman Collection
https://documenter.getpostman.com/view/20680920/2sA3QqfYGX
## Questions and Answers

### How long did it take you to complete this assignment?
- It took approximately 2-3 hours to complete this assignment, including setup, coding, and testing.

### What about this assignment did you find most challenging?
- The most challenging part was setting nup postgressql in Windows, it was a chain error of long issues including upgradation of Visual Studios, Lastly I have to move to WSl due to time constraints.And also as compared to django-drf functionalities I find troublesome here ensuring the update operation only modified the fields provided in the request while leaving other fields unchanged. This required careful checking of the request data and conditional updates.

### What about this assignment did you find unclear?
- Initially, the requirements around whether to use PUT or PATCH for partial updates were unclear. Clarification was needed on implementing PATCH-like behavior using the PUT method.

### What challenges did you face that you did not expect?
- Handling the integration and interaction between Flask, Flask-RESTful, and SQLAlchemy was a bit more tedious than anticipated, particularly ensuring proper error handling and response formatting.

### Do you feel like this assignment has an appropriate level of difficulty?
- The assignment had an appropriate level of difficulty. It required a good understanding of RESTful principles, Python, and Flask, making it a suitable challenge for someone with intermediate-level experience in these technologies.

### Briefly explain your decisions to use tools, frameworks, and libraries like Flask, Flask-RESTful, etc.
- **Flask**: Flask was chosen for its simplicity and flexibility, allowing for rapid development of the API.
- **Flask-RESTful**: Flask-RESTful was used to easily create RESTful APIs. It simplifies the creation of resource-based routes and integrates well with Flask.
- **SQLAlchemy**: SQLAlchemy was used as the ORM for database interactions. It provides a powerful toolkit for working with databases in Python.

### Did you make certain assumptions and decisions around the application? Please elaborate on your reasoning.
- **Assumptions**:
  - I assumed the data sent over a request to be in form format rather than json.
  - Only specified fields in the request are updated, leaving other fields unchanged.
  - The `toDict` method is available in the `Account` model to serialize the account objects.

- **Decisions**:
  - The `put` method was modified to behave like a `PATCH` method to update only the provided fields. This decision was made to simplify the API and avoid confusion between PUT and PATCH methods.
  - Error handling was implemented to provide clear feedback on invalid or missing data in requests.

## Installation and Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/account-management-api.git
   cd account-management-api
