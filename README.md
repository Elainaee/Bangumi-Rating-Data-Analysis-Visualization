Bangumi Anime Rating Data Analysis & Visualization Project
A data-driven project focused on automated data crawling, exploratory data analysis (EDA), trend mining, and interactive visualization for Bangumi anime rating data—designed to demonstrate practical skills in data collection, data processing, and data visualization for data science/big data roles.
Project Overview
This project implements an end-to-end data pipeline to collect, process, analyze, and visualize anime rating data from Bangumi (a popular anime community platform). It showcases hands-on experience in automated web crawling, data cleaning, statistical analysis, and interactive dashboard development—key competencies for data science and big data positions.
The project delivers actionable insights into anime rating distributions, trend changes, and correlation patterns, with a focus on reproducibility, code modularity, and engineering best practices.
File Structure
│  bangumi_dashboard.html    # Interactive visualization dashboard (HTML)
│  requirements.txt          # Project dependencies (Python packages)
│  server.exe                 # Local server for dashboard deployment
│  start_server.bat           # One-click script to launch the local server
│  
├─bangumi_data                # Raw anime data (stored by date)
│      bangumi_anime_2025-12-17.csv
│      bangumi_anime_2025-12-24.csv
│      
├─Final Report                # Comprehensive analysis report & visualization figures
│  │  Final Project Report.pdf
│  │  Bangumi Rating Data Analysis - Single Week Deep Dive & Multi-Week Trend Analysis.md
│  │  
│  └─fig                      # Visualization figures (used in the final report)
│          fig1.png ~ fig14.png
│          
├─Prime Analysis              # Core analysis & crawling scripts
│      bangumi.crawling.py    # Web crawling script for Bangumi data
│      bangumi_analysis.ipynb # Jupyter Notebook for EDA & statistical analysis
│      bangumi_anime.csv      # Processed data for analysis
│      
├─resource                    # Project resources (algorithm diagrams, references)
│      Bayesian.png
│      Shannon.png
│      Spearman.png
│      
└─Web Crawling Timer          # Automated scheduled crawling module
        bangumi_crawler.log   # Crawler execution logs
        bangumi_crawler.py    # Core crawling logic
        bangumi_scheduler.py  # Scheduled task configuration
        run_crawler.py        # Script to run the crawler
        setup.bat             # Environment setup script
Key Skills Demonstrated
- Data Collection: Automated web crawling with Python (Requests, BeautifulSoup), scheduled task management, and log monitoring.
- Data Processing: Data cleaning, transformation, and aggregation using Pandas, NumPy, and Scipy.
- Statistical Analysis: Exploratory Data Analysis (EDA), correlation analysis (Spearman), Bayesian analysis, and information entropy (Shannon) application.
- Visualization: Interactive dashboard development (HTML) and static visualization (Matplotlib, Seaborn) for clear insight communication.
- Engineering Practice: Modular code design, reproducible project structure, and one-click deployment scripts.
Quick Start
1. Install Dependencies
pip install -r requirements.txt
2. Launch Interactive Dashboard
Run the one-click script:
start_server.bat
Or directly open the HTML file in your browser:
bangumi_dashboard.html
3. Run Scheduled Web Crawler
cd Web Crawling Timer
python run_crawler.py
Technical Stack
- Programming Language: Python 3.10+
- Data Crawling: Requests, BeautifulSoup, Scheduler
- Data Analysis: Pandas, NumPy, Scipy
- Visualization: Matplotlib, Seaborn, Plotly (embedded in HTML dashboard)
- Deployment: Local Server, Batch Scripts
- Analysis Methods: EDA, Correlation Analysis, Trend Mining, Bayesian Inference, Information Entropy
Analysis Deliverables
- Deep dive into single-week anime rating data (distribution, tag analysis, regional breakdown).
- Multi-week trend analysis (rating changes, popularity shifts, correlation trends).
- Interactive dashboard for real-time data visualization and exploration.
- Comprehensive final report (PDF + Markdown) with detailed insights and visualization figures.
Project Highlights (For Recruiters)
- End-to-end data pipeline: From automated data collection to actionable insights.
- Reproducible code: Clear structure, detailed documentation, and one-click deployment.
- Practical problem-solving: Applied statistical methods to derive meaningful insights from real-world data.
- Technical versatility: Combined web crawling, data analysis, and visualization to deliver a complete solution.
About Me
A passionate Data Science & Big Data student with hands-on experience in data collection, analysis, and visualization. Proficient in Python-based data tools and committed to building data-driven solutions. Eager to apply technical skills in a professional data role.
