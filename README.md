# Hangman

![Hangman Responsive](documentation/amiresponsive.JPG)

Hangman is a terminal game based on the classic word game Hangman.

* The link to [Hangman](https://af-project-3-hangman-ab624bdbed0d.herokuapp.com/)

## How to play

*   Click on this link (https://af-project-3-hangman-ab624bdbed0d.herokuapp.com/) or copy and paste to browser.
*   As soon as the page loads enter your name.
*   Select one of the options from the menu.
*   Learn the rules
*   Start the game.

## User Stories
  As a user:
*    I want to be able to enter my name and get feedback if I have entered it incorrectly.
*   I want to be able to view the rules of the game.
*   I want to be able to see how many letters I need to guess.
*   I want to be able to see what letter I have already guessed.
*   I want to be notified if I select something other than a letter.
*   I want to be notified if I have already guessed a certain letter.
*    I want to know how many lives or guesses I have left.
*   I want a picture so I can visualise how many lives or guesses I have left.
*   I want to be able to restart the game without having to exit first.

## Features

### Welcome Screen
The welcome screen has a large hangman logo to show the user what game they are playing.
The user is then welcomed to the game via a welcome message and asked to enter their name.

![Hangman](documentation/hangman.JPG)


After entering their name the user is then welcomed by name.


### Main Menu 
The user is then presented with a menu from which they can select one of three options :

1. Play the game.
2. See the Rules.
3. Exit game.

![Main Menu](documentation/menu.JPG)

#### Play the Game 
*   If the user selects to play the game they are presented with a statement informing them of how many lives they have and what letters they have already used. They will also be presented with a graphic that will change every time the user loses a life.
The user will be shown lines to indicate how many letters in length the current word is, which they have to guess. They will then be asked to input a letter and press enter.

![Play](documentation/lets_play.JPG)

*   If the user enters a letter that is not in the current word, they will be told Sooy but your chosen letter is not in the word, followed by the number of lives they have left and the letters used. The graphic will also be updated to reflect this.

*   If the user fails to select a correct letter then the game will come to an end.

*   If the user guesses the word they will be congratulated and asked if they would like to play again, here they can either select Y to play again or hit any other key to exit where they will receive a goodbye message.

#### The Rules
*   If the user selects to view the rules they will be presented with a list of rules and told to click enter, to return to the main menu.

![Rules](documentation/rules.JPG)

#### Exit

*   If the user selects to exit the game they will be presented with a goodbye message.

![Exit](documentation/exit.JPG)

## Design
As no images could be used for this project. I created a logo image for the star of the game using the Python Art library to convert text to ASCII.

![Hamgman logo](documentation/hangman_image.JPG)

The colors available for this project were also limited so I introduced colors where I could to make the terminal more aesthetically pleasing to the user.

![Colors](documentation/lets_play.JPG)

## Technologies Used

The following technologies were used to complete this project.

*   [Python](https://www.python.org/) - was used to write the program.
*   HTML - was used to build that mock terminal.
*   Javascript - was used to provide the start-up script to run the Code Institute terminal.
*   [GitHub](https://github.com/) was used to host the project code after being pushed.
*   Git - was used for the version control of the website.
*   Heroku - was used to deploy the project.
*   VS Code - was used to write and edit code for the project.

### Imported Libraries 
*   [random](https://docs.python.org/3/library/random.html) - was used to randomly select a word for the user to play from the list of words in the words.py file.

*   [os](https://docs.python.org/3/library/os.html) - was used to clear the terminal to make for a better user experience by reducing clutter on the screen.

*   [Colorama](https://pypi.org/project/colorama/) - was used to add some color to the project and make it more aesthetically pleasing for the user.

*   [Art](https://pypi.org/project/art/) - was used to create ASCII for the starting page of this project.

## Bugs 

### Solved Bugs
 *  I had a bug in my restart game function, whereby it was not giving the correct response to the user's input, in order to solve this I added a while loop so that now the user must select Y to restart the game again and hit enter otherwise any other selection will exit the game.

*    I also had a bug as I originally had my game logo in an external file but every time the program was run the logo would go out of sync. Therefore I opted to import Python Art and use that instead to convert text to ASCII.

 *  On deployment I had a bug running my Art import however according to logs on Heroku, I understood that I had not set up the Art import correctly in my requirements.txt file.

 *  I did have another issue calling the user's name so in order to resolve this user_name was defined and added to the functions which required it.

## Testing 
Please find the link to testing here: [Testing](TESTING.md)
## Deployment

The project was deployed to Heroku

### To deploy the project as an application that can be run locally

You must first have Python installed 

*   Download  Zip File

Go to the GitHub Repo page.
Click the Code button and download the ZIP file containing the project.
Extract the ZIP file to a location on your PC.


*   Clone Repository

In order to make a local copy of this project, you can clone 
it to your desktop.

Sign in to GitHub, locate the repository and click to open the repository.

On the repository main page, click the green code button where the files are located.

This will open a drop - menu.

In the dropdown menu stay on the HTTPS option and click the copy icon button next to the URL to copy it.

![Github](documentation/hangman_github.JPG)

Next open Git Bash and type git clone and your directory link.

![Gitbash](documentation/gitbash.JPG)

Then type cd and the directory name.

Then code . to open VS Studio using Windows.


### To deploy on Heroku

Clone the repository as above.

Create Heroku account here

Create a new Heroku application by clicking creat new app.

![Create App Heroku](documentation/heroku_new.JPG)

Go to the deploy tab.

Link your Github account

![Github Heroku](documentation/heroku_github.JPG)

Go to settings and add buildpack.

Add Python and Node.js in that order.


![Buildpack Heroku](documentation/buildpack_heroku.JPG)

Go to the Deploy tab and select deploy from branch.


Wait for completion and click view.

![Deploy from branch Heroku](documentation/heroke_deploy_2.JPG)

## Credits
Color formatting: [Colorama](https://pypi.org/project/colorama/)

## Acknowledgements
