# ETL Pipeline Design and Development Approach

1. Identify and list desired data elements from each source
2. Develop scripts to retrieve desired data elements from [ESPN Scoreboard and Team API Endpoints](https://gist.github.com/akeaswaran/b48b02f1c94f873c6655e7129910fc3b)
3. Develop methods to retrieve desired data elements from [OpenCage Forward Geocode API Endpoint](https://opencagedata.com/api#)
4. Develop script to transform extracted data into data structures matching the relational Pickem Database schema
5. Develop script to load data into the MySQL database
6. Devlelop script to scrape Game Odds and and Team Stats data elements from [CBS Scoreboard](https://www.cbssports.com/college-football/scoreboard/) and [Team Stats](https://www.cbssports.com/college-football/stats/team/team/passing/all-conf/) pages
7. Load data into local MySQL database instance
8. Create [infinityfree](https://www.infinityfree.com/) account to host MySQL database with remote access