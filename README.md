# Question Geeneration API for Standard 52 Card Deck
The main focus of this project is to develop an API for generating questions for Probability for a stndard 52 Card Deck. We bundled in some questions from basic probability to probability with combinations using 5-card Poker hands.

## How to setup:
### Method 1 using Pip
Make sure to use a virtual environment. You must pip install django.
`https://docs.python.org/3/library/venv.html`

This is what is installed in our virtual environment:
I only had to use pip install for `Django` and `djangorestframework`
which you should be able to install using:
`pip install -r requirements.txt` <br/>
asgiref           3.5.2 <br/>
Django            3.2.16 <br/>
djangorestframework 3.14.0 <br/>
pip               22.1 <br/>
pytz              2022.6 <br/>
setuptools        62.2.0 <br/>
sqlparse          0.4.3 <br/>
typing_extensions 4.4.0 <br/>
wheel             0.37.1 <br/>

### Method 2 using Anaconda
This approach is for those who have Python set up using Anaconda. In the Environment folder, the Anaconda environment file to install from is `qa-gen-py10-env.yml`. To install it open the Anaconda Prompt, cd to the directory where `qa-gen-py10-env.yml` is and create a virtual environment using this commanbd  `conda env create -f qa-gen-py10-env.yml`. To activate the environment, use command `conda activate qa-gen-py10-env.yml` and you're set to go. To run the Django server, you'll need to use the Anaconda Prompt.

## Running the Django Server

### First Time Running
If you are working in multiple contexts, you may need to set this variable as well. <br/>
`export DJANGO_SETTINGS_MODULE=questionGenerationApi.settings`

You may have to run migrations with `python manage.py migrate`

### After Initial Setup
If you make any changes to the model for 'Questions' or add ny additional models, you will have to run `python manage.py make migrations` then migrate them with the command above.

#### Create a Super User for the admin/db interfaces
`python manage.py createsuperuser`

#### Go here to see admin and db data after you run:
`python manage.py runserver`
http://127.0.0.1:8000/admin/

#### Check out the API Here:
http://127.0.0.1:8000/questions/
if your server is up and running this should take you to an API Root page

Endpoint Example: `http://localhost:8000/returnQuestions/5/?difficulty=3`

#### To go to our question generation API demonstration page:
`http://localhost:8000/generate`

#### To go to our dashboard page:
`http://localhost:8000/gui`

## Files Containing Functions for Generating Each Question Type:
If you wish to make your own API, here are the files containing the functions used for the question generation:
- `utils.py` - Contains question generation for basic probability and some Poker hands.
- `pokerHandQuestionGen.py` - Is a dedicated file for generating questions for each Poker Hand. These functions are capable of creating bulks of n<={Max Possible for Hand Type} 
- `genericHandQuestionGen.py` Is a dedicated file for generating generic questions. These functions are capable of creating n<={Max Possible}. Some functions don't have a known limit, so they're unrestricted. An indication of surpassing that unknown limit is when an infinite loop occurs.

For example usage, see `views.py::generate`

This method calls each "hand" type and has two types of algorithms.  The first is to iterate over a deck of cards and generate hands that represent the question. IE  fullhouse(deck) might return a question with AAAQQ. The second method is to generate random hands, and store them in a set for uniqueness. In order to remove the database, each method could simply return a question and the "generate" method would be randomized in terms of which type of hand should be generated based on difficulty.

Difficulty is manually set as are answers. If the program is converted to using an actual math formula, the difficulty could be derived from that formula.  These are both set in the methods such as fullhouse() which is located in utils.py

There are api endpoints to return questions and these could be used with any front end.  Our initial thought was to return N questions with up to X difficulty. The questions returned are randomized from the database. 


## Endpoints ##:
admin/<br/>
  the super user can login and create / delete / edit data from the db<br/><br/>
generate/<br/>
  populate the db<br/><br/>
returnQuestions/<br/>
  arguments _GET:<br/>
     numQuestions: int<br/>
     difficulty: int<br/><br/>
gui/<br/>
  the html template for generating / clearing / viewing questions<br/><br/>
clearDatabase/<br/>
   reset the db<br/><br/>
singleQuestion/<br/>
   returns a single question of any difficulty<br/><br/>
   
   
## What Could be Improved:
- Create more API endpoints for a more barebone experience.
- remove the database and randomize the question returns
- Make questions more variable, add types of questions then generate hands
- Add multiple choice answers
- Add a quiz interface
- Add a way to display the formula used to determine the answer
- A feature where you can turn on/off question types/difficulty when generating 
- Create a better dashboard using React
