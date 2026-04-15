# Bangumi Anime Rating Data Analysis & Visualization
> &nbsp;&nbsp;&nbsp;&nbsp;A data-driven project focused on automated **data crawling** (from https://bgm.tv/anime/browser?sort=rank), **exploratory data analysis (EDA)**, **trend mining**, and **interactive visualization** for Bangumi anime rating data—designed to demonstrate practical skills in data collection, analysis, and visualization for data science/big data roles.
### Project Overview
&nbsp;&nbsp;&nbsp;&nbsp;This project implements an end-to-end data pipeline to crawl, process, analyze, and visualize anime rating data from Bangumi (https://bgm.tv/anime/browser?sort=rank), a popular anime community platform. It showcases hands-on experience in data collection, cleaning, statistical analysis, and visualization—key competencies for data science & big data positions.

&nbsp;&nbsp;&nbsp;&nbsp;The crawled data includes 8,390 sets of anime records until Dec 24, 2025(only anime with ratings on Bangumi are included; most anime with insufficient ratings are not recorded). The data is sorted by score (from highest to lowest), with partial missing values in the year and company fields.
### Crawled Data Fields
- `subject_id`: The time-based sequence number of anime data recorded on Bangumi official website, starting from 1.
- `name_cn`: Chinese name of the anime.
- `name`: Original name of the anime (mostly Japanese).
- `score`: Anime rating (ranging from 1 to 10 points).
- `total`: Total number of users who rated the anime.
- `year`: The year the anime was first aired (with partial missing values).
- `company`: The animation production company (with partial missing values).
- `rate_i` (1 ≤ i ≤ 10): The number of users who gave an i-point rating (e.g., rate_1 = number of users who gave 1 point, rate_10 = number of users who gave 10 points).


        File Structure
        │  bangumi_dashboard.html    # Interactive visualization dashboard (HTML), implemented by AI Agent
        │  requirements.txt          # Project dependencies (Python packages)
        │  server.exe                 # Local Server for dashboard deployment
        │  start_server.bat           # One-click script to launch the local server
        │  
        ├─bangumi_data                # Raw anime data (crawled from Bangumi, stored by date)
        │      bangumi_anime_2025-12-17.csv
        │      bangumi_anime_2025-12-24.csv
        │      
        ├─Final Report                # Comprehensive final report & visualization figures
        │  │  Final Project Report.pdf
        │  │  
        │  └─fig                      # Visualization figures (used in the final report)
        │          fig1.png ~ fig14.png
        │          
        ├─Prime Analysis              # Core analysis & crawling scripts
        │      bangumi.crawling.py    # Web crawling script (target: https://bgm.tv/anime/browser?sort=rank)
        │      bangumi_analysis.ipynb # Jupyter Notebook for EDA & statistical analysis
        │      bangumi_anime.csv      # Processed data for analysis
        │      
        └─resource                    # Project resources (algorithm diagrams, references)
               Bayesian.png
               Shannon.png
               Spearman.png
### Key Skills
- **Data Collection**: Built a web crawler using Python (**Requests**, **BeautifulSoup**) to scrape 8,390 sets of anime rating data from Bangumi (https://bgm.tv/anime/browser?sort=rank).


- **Data Processing**: Processed missing values (in year and company fields), cleaned and transformed raw data using **Pandas** and **NumPy**.
- **Statistical Analysis**: Applied EDA, correlation analysis (Spearman), Bayesian inference, and Shannon entropy to derive meaningful insights from anime rating data using **Pandas**, **Statsmodels** and **Scipy**.
- **Visualization**: Developed static visualizations in Jupyter Notebook (**Plotly**, **Matplotlib**) and an interactive HTML dashboard (functionality implemented by AI Agent) to present data insights clearly.
- **Engineering Practice**: Designed modular code, one-click deployment scripts, and comprehensive documentation for reproducibility.
### Quick Start
#### 1. Install Dependencies

        pip install -r requirements.txt
#### 2. Launch Interactive Dashboard in Localhost

        start_server.bat

#### 3. Run Web Crawler

        cd Prime Analysis
        python bangumi.crawling.py
   
### Technical Stack
- Programming Language:   Python 3.10+

- Data Crawling:   Requests, BeautifulSoup
- Data Analysis:   Pandas, NumPy, Scipy, Statsmodels
- Visualization:   Matplotlib, Plotly
- Deployment:   Local Server, Batch Scripts
- Analysis Methods:   EDA, Correlation Analysis, Trend Mining, Bayesian Inference, Information Entropy, LOWESS


### Analysis Deliverables
- 8,390 sets of crawled anime rating data (sorted by score, only anime with ratings are included). For the improvement, try to implement automatic web crawling.
- Deep dive into single-week data: Rating distribution, tag analysis, and regional breakdown.
- Multi-week trend analysis: Changes in ratings, popularity shifts, and correlation trends over time (Although there are only two-week data).
- Interactive dashboard for real-time data exploration and visualization.
- Comprehensive final report (PDF + Markdown) with detailed insights and visualization figures.
### Project Highlights
- End-to-end data pipeline: From automated crawling (targeting https://bgm.tv/anime/browser?sort=rank) to actionable insights, demonstrating full-cycle data processing capabilities.
- Real-world data application: Analyzed 8,390 sets of real anime rating data, solving practical data cleaning and analysis problems.
- Reproducibility: Clear code structure, detailed documentation, and one-click deployment for easy verification.
- Technical versatility: Combined web crawling, data analysis, and visualization to deliver a complete, data-driven solution.
### About Me
&nbsp;&nbsp;&nbsp;&nbsp;A passionate Data Science & Big Data student with hands-on experience in automated data crawling, data analysis, and visualization. Proficient in Python-based data tools (Pandas, NumPy, Seaborn, Plotly...) and statistical methods, committed to building data-driven solutions. Eager to apply technical skills in a professional data role.
