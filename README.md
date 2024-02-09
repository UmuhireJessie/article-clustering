# Article Clustering



## Description

This project utilises news article api to scrap and cluster articles found. After placing them into several cluster, we then present the clusters with their correspong articles and urls. The KMean model was used to help us cluster the articles. The app has been deployed on Streamlite since it offers easy and smooth presentation of results.

Note: Deployed version of the web pages [Here](https://article-clustering.streamlit.app/)

## Packages Used

This project has used the some packages such as numpy, tensorflow, which have to be installed to run this web app locally present in `requirements.txt` file. 

## Installation

To run the project locally, there is a need to have Visual Studio Code (vs code) installed on your PC:

- **[VS Code](https://code.visualstudio.com/download)**: It is a source-code editor made by Microsoft with the Electron Framework, for Windows, Linux, and macOS.

## Usage

1. Clone the project 

``` bash
git clone https://github.com/UmuhireJessie/article-clustering.git

```

2. Open the project with vs code

``` bash
cd article-clustering
code .
```

3. Install the required dependencies

``` bash
pip install -r requirements.txt
```


4. Run the project

``` bash
streamlit run article.py
```

5. Use the link printed in the terminal to visualise the app. (Usually `http://127.0.0.1:8501/`)


## Important Notes
- The app has used existing APIs for news articles so one may be required to generate an API KEY if they want to test the app locally.

## Authors and Acknowledgment

Jessie Umuhire Umutesi

## License
[MIT](https://choosealicense.com/licenses/mit/)
