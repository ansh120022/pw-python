The project contains tests for https://demo.ft-crm.com/

# Quick start

    docker build --tag tests . --no-cache
    docker run -it tests python3 -m pytest tests.py

## Explanation

The following best practices are used:

 1. Page object pattern: interactions with the browser separated from tests, which makes tests easy to read
 2. Playwright usage is separated from tests, and Selenium or another alternative can easily substitute it. 
 3. Tests are independent of each other

## What could be done better

 The test task is limited by time, and I intentionally missed some points I would implement in a real project:
 
 1. Asynchronous functions provided by Playwright
 2. Test report with screenshots
 3. Parametrized tests
 4. Negative tests
 5. Parallel run