<h1 align="center">
📖 EmbedChain-Streamlit-Docker App Template
</h1>

[![A Video Guide](ui.PNG?raw=true)](https://youtu.be/yJAWB13FhYQ)

[https://youtu.be/yJAWB13FhYQ](https://youtu.be/yJAWB13FhYQ)


## 🔧 Features

- Basic Skeleton App configured with `openai` API
- A ChatBot using embedchain and Streamlit
- Docker Support with Optimisation Cache etc
- Deployment on Streamlit Public Cloud

This repo contains an `main.py` file which has a template for a chatbot implementation.

## Example Input Data:

Select the number of Data Sources from slider and enter the details.


| Source    | URL |
| -------- | ------- |
| youtube  | https://www.youtube.com/watch?v=3qHkcs3kG44   |
| pdf_file |https://navalmanack.s3.amazonaws.com/Eric-Jorgenson_The-Almanack-of-Naval-Ravikant_Final.pdf    |
| web    | https://nav.al/feedback  |
|qna_pair| "Who is Naval Ravikant?", "Naval Ravikant is an Indian-American entrepreneur and investor." |

**Question:** What unique capacity does Naval argue humans possess when it comes to understanding explanations or concepts?


## Adding your chain
To add your chain, you need to change the `load_chain` function in `main.py`.
Depending on the type of your chain, you may also need to change the inputs/outputs that occur later on.


## 💻 Running Locally

1. Clone the repository📂

```bash
git clone https://github.com/amjadraza/fintech-virtual-assistant-app.git
```

2. Install dependencies with [Poetry](https://python-poetry.org/) and activate virtual environment🔨

```bash
poetry install
poetry shell
```

3. Run the Streamlit server🚀

```bash
streamlit run demo_app/main.py 
```

Run App using Docker
--------------------
This project includes `Dockerfile` to run the app in Docker container. In order to optimise the Docker Image
size and building time with cache techniques, I have follow tricks in below Article 
https://medium.com/@albertazzir/blazing-fast-python-docker-builds-with-poetry-a78a66f5aed0

Build the docker container

``docker  build . -t fintech-virtual-assistant-app:latest ``

To generate Image with `DOCKER_BUILDKIT`, follow below command

```DOCKER_BUILDKIT=1 docker build --target=runtime . -t fintech-virtual-assistant-app:latest```

1. Run the docker container directly 

``docker run -d --name fintech-virtual-assistant-app -p 8080:8080 fintech-virtual-assistant-app:latest ``

2. Run the docker container using docker-compose (Recommended)

``docker-compose up``


Deploy App on Streamlit Public Cloud
------------------------------------
This app can be deployed on Streamlit Public Cloud using GitHub. Below is the Link to 
Publicly deployed App

https://embedchain.streamlit.app/



## Report Feedbacks

As `fintech-virtual-assistant-app:latest` is a template project with minimal example. Report issues if you face any. 

## DISCLAIMER

This is a template App, when using with openai_api key, you will be charged a nominal fee depending
on number of prompts etc.