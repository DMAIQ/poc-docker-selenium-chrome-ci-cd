# Proof of Concept: Docker/Selenium/Chrome CI/CD

## Overview
This repository holds code and GitHub configurations for the Docker/Selenium/Chrome proof of concept.
It demonstrates how to set up a CI/CD pipeline for UI testing using Selenium with Chrome in a Docker container for local testing and via GitHub actions for automated testing.

## Prerequisites
- [Docker](https://docs.docker.com/desktop/install/windows-install/)
- [Python](https://apps.microsoft.com/store/detail/python-312/9NCVDN91XZQP) - via Windows Store
- [Python](https://www.python.org/downloads/) - via Windows Installer
- [GitHub](https://github.com/) Account

## Setup and Execution

### 1. Set Up a local Selenium/Chrome instance with Docker
- Install Docker and the Windows Subsystem for Linux (WSL) 2 on your machine. Follow the [Docker installation guide](https://docs.docker.com/get-docker/) and the [WSL 2 installation guide](https://docs.microsoft.com/en-us/windows/wsl/install) for detailed instructions.
- Open a terminal or command prompt
- Run the following commands to start an Selenium/Chrome instance locally:
    ```sh
    docker pull selenium/standalone-chrome
    docker run -d -p 4444:4444 --shm-size="2g" selenium/standalone-chrome
    ```
    - The -p 4444:4444 maps the port 4444 inside the container to port 4444 on your host.
    - '--shm-size="2g" is to allocate enough shared memory for Chrome to run smoothly.

### 2. Setup Python Environment
- Install Python:
    - If you're using the Windows Store:
        - Install [Python from the Windows Store](https://apps.microsoft.com/store/detail/python-312/9NCVDN91XZQP).
        - Once installed, you can access Python by typing python in your terminal or command prompt.
    - If you're using the Windows Installer:
        - Download the [Python installer from the official website](https://www.python.org/downloads/).
        - Run the installer. Ensure you check the box that says "Add Python to PATH" during installation.
- Verify Python Installation:
    - Open a terminal or command prompt.
    - Type `python --version` and press Enter. You should see the version of Python you installed.
- Install pip (Python package installer):
    - Pip is usually included with recent versions of Python. To check if you have it installed, type `pip --version` in your terminal or command prompt.
    - If you need to install pip, download [get-pip.py](https://bootstrap.pypa.io/get-pip.py) to a folder on your computer.
    - Open a terminal or command prompt and navigate to the folder containing get-pip.py.
    - Run 'python get-pip.py'. This will install pip.
- Install Selenium:
    - Install Selenium using pip:
        ```sh
        python -m pip install selenium
        ```

python -m pip install selenium

### 3. Clone the Repository and Run the Tests
- Clone the Repository:
    - Open a terminal or command prompt.
    - Navigate to the directory where you want to clone the repository.
    - Run the following commands:
        ```sh
        git clone https://github.com/DMAIQ/poc-docker-selenium-chrome-ci-cd.git
        cd poc-docker-selenium-chrome-ci-cd
        ```
- Set Environment Variables for the example test script:
    - Before running the tests, you need to set the environment variables `USERNAME`, `EMAIL`, and `PASSWORD` which are used by the example test script. These are your GitHub credentials and information that will be entered into the GitHub login page inputs.
        ```sh
        set USERNAME=your_username
        set EMAIL=your_email
        set PASSWORD=your_password
        ```
        - *If your password contains special characters, you must escape those by adding a `^` character before each special character. Otherwise the terminal will read those special characters as breaking points and your full password will not be input.
- Run the Tests:
    - Ensure your Docker container with Selenium/Chrome is running (from step #1).
    - Execute the example test script. For example, if your test script is named testGitHubLogin.py, you'd run:
        ```sh
        python testGitHubLogin.py
        ```
    - Monitor the terminal or command prompt for test results. The script should provide feedback on the steps it takes and the success or failure of the tests.

### 4. Clean Up
After running your tests and verifying the results, it's a good practice to clean up any resources you've set up to ensure there's no unnecessary consumption of system resources. Here's how you can do that:
- Stop the Docker Container:
    - If you've started a Docker container for Selenium/Chrome, you can stop it to free up system resources.
    - First, identify the container ID or name:
        ```sh
        docker ps
        ```
    - Look for the container running `selenium/standalone-chrome` and note its `CONTAINER ID` or `NAMES`.
    - Stop the container using its ID or name:
        ```sh
        docker stop [CONTAINER_ID_or_NAME]
        ```
- Remove the Docker Container (Optional):
    - If you wish to remove the container entirely (especially if you won't be using it again soon), you can do so with:
        ```sh
        docker rm [CONTAINER_ID_or_NAME]
        ```
- Remove Cloned Repository (Optional):
    - If you don't plan on running the tests again or wish to start fresh next time, you can remove the cloned repository from your system.
    - Navigate to the directory containing the cloned repository and run:
        ```sh
        cd ..
        rm -rf poc-docker-selenium-chrome-ci-cd
        ```