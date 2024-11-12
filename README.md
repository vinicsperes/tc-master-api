
markdown
Copiar código
# NBA Shot Chart API

This is a Flask-based API that provides NBA shot chart data using the `nba_api` Python package. It allows you to fetch the shot charts of players for a specific season and season progress.

## Requirements

- Python 3.8 or higher
- Flask
- nba_api
- pandas

## Setup

Follow the steps below to set up the project on your local machine.

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/vinicsperes/tc-master-api.git
cd tc-master-api
2. Create a Virtual Environment
Create a virtual environment to isolate dependencies:

bash
Copiar código
python3 -m venv venv
Activate the virtual environment:

On Windows:

bash
Copiar código
venv\Scripts\activate
On macOS/Linux:

bash
Copiar código
source venv/bin/activate
3. Install Dependencies
Install the required dependencies using pip:

bash
Copiar código
pip install -r requirements.txt
If you haven't created a requirements.txt file yet, you can manually install the required packages:

bash
Copiar código
pip install Flask nba_api pandas
4. Run the API
To run the API, execute the following command:

bash
Copiar código
python app.py
This will start a local development server at http://localhost:5000.

5. Use the API
The API exposes the following endpoint:

php
Copiar código
GET /shot-chart/<player_name>/<season_id>/<season_progress>
Example
To get the shot chart data for LeBron James in the 2023-24 season during the Regular Season:

perl
Copiar código
http://localhost:5000/shot-chart/LeBron%20James/2023-24/Regular%20Season
The API will return a JSON object containing the shot chart data for the specified player, season, and season progress.

6. Testing
You can test the API using any HTTP client, such as Postman or directly through your browser. Just replace the player name, season ID, and season progress with the desired values.

Additional Notes
The API relies on the nba_api package, which fetches data from the NBA Stats API.
Make sure to activate the virtual environment whenever you work on this project to ensure that the correct dependencies are used.