# Financial News and Stock Price Integration Analysis

This repository hosts the code for the analysis of the Financial News and Stock Price Integration Dataset (FNSPID). The goal is to perform exploratory data analysis (EDA) to understand the relationship between financial news and stock prices.

## Branches

- **main**: The main branch containing the finalized code.
- **task-1**: A branch dedicated to the initial analysis tasks.
- **task-2**: A branch dedicated to the initial analysis tasks.


## Objectives

1. **Exploratory Data Analysis (EDA)**:
   - **Descriptive Statistics**: Analyze headline lengths, article counts per publisher, and publication date trends.
   - **Text Analysis**:
     - Perform sentiment analysis on news headlines.
     - Extract common keywords and phrases using natural language processing (NLP).
   - **Time Series Analysis**: Investigate publication frequency over time and identify peaks related to market events.
   - **Publisher Analysis**: Assess the activity of different publishers and identify unique domains.

2. **Stock Price Data Analysis**:
   - Load stock price data into a Pandas DataFrame.
   - Calculate technical indicators using TA-Lib (e.g., moving averages, RSI, MACD).
   - Use PyNance to extract financial metrics.

3. **Visualization**:
   - Visualize data to illustrate the impact of news and technical indicators on stock prices.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/FNSPID-Analysis.git
   cd FNSPID-Analysis
   ```

2. Switch to the task branch:
   ```bash
   git checkout task-1
   ```
   ```bash
   git checkout task-2
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the analysis scripts in the `analysis` directory.


