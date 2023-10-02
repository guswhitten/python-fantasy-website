## How to run (in VS code):

Open myproject.py and press F5
This will run the Flask development server on your local machine, and you'll be able to visit the website at http://localhost:8000

## How to run (in Docker):
- `cd` into directory
- `docker build -t python-fantasy-website:latest .`
- `docker run -p 8000:8000 python-fantasy-website`

## Fixes needed:

- when page is refreshed, no old mp4's should be displayed
- when creating bar chart race:
  - slow down speed of video
  - add green up arrow and red down arrow to indicate change in rank
- add a dropdown to select which type of race we're doing
  - Points For
  - Points Against
  - Wins
  - etc.