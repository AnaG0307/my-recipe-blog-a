# My Recipe Book

![App page screenshot](assets/images/app_screenshot.png)
[View the app in Heroku here](https://adventureland-ana.herokuapp.com/)

## Table of Contents

1. [About](#About)
2. [User Stories](#User-Stories)
3. [Features](#Features)
4. [Data Model](#Data-Model)
5. [Testing](#Testing)
6. [Technologies Used](#Technologies-Used)
7. [Deployment](#Deployment)
8. [Credits](#Credits)



## About

My Recipe Book is been designed to facilitate keeping all the cooking recipes in one place and with easy access, allowing the site user to access their personal and family recipes safe and in one place. The site also provides the opportunity to being able to discover new recipes that the site user can save.


## User Stories

#### User Site Stories

- As a Site User I can register an account so that I can comment and like a past.
- As a Site User I can view a list of posts so that I can select one to read.
- As a Site User I can view the number of likes on each post so that I can see which ones are the most viral.
- As a Site User I can click on a post so othat I can read the full text.
- As a Site User I can view a paginated list of posts so that I can easily select a post to view.
- As a Site User I can leave comments on a post so that I can be involved in the conversation. 
- As a Site User I can view comments on an individual post so that I can read the conversation.
- As a Site User I can create and save my personal recipes so that I have all my recipe in the same place.
- As a Site User I can use the "search" bar so that I can easily find recipes I am looking for.


#### Admin Site Stories

- As an admin User I can acces the admin site so that I can create and control the content I wish for my site.
- As an admin User I can create draft posts so that I can finish writing or publish the content later.
- As an admin User I can create, read, update and delete posts so that I can manage my site content.
- As an admin User I can view the number of likes on each post so that I can see which ones are the most viral.
- As an admin User I can approve/disapprove comments so that I can filter out objectionable comments.


## Features

#### Existing Features
- Navigation Bar
- Footer
- Login/Logout/Register
- My Recipes
- My Favourite Recipes


#### Future Features
- My Shopping List
- Share personal recipes



## Data Model

Add database diagram


## Testing


#### Bugs


#### Remaining Bugs


#### Validator Testing

- Used [PEP8online.com](http://pep8online.com/) and no errors were returned.

![validator-screenshot](assets/images/pep8validator.png)


## Technologies Used

- [Gitpod](https://gitpod.io/)
- [Github](https://github.com/)
- [Unsplash](https://unsplash.com/)
- [Lucidchart](https://www.lucidchart.com/pages/)
- [Fontawesome](https://fontawesome.com/start)
- [Cloudinary](https://cloudinary.com/)
- [Django](https://www.djangoproject.com/)
- [Heroku](https://id.heroku.com/)


## Deployment

The project is been deployed to Heroku. Steps for deployment:

TO BE DEVELOPED (the one below is for adventureland)
- Local deployment:
    - Fork the project to copy the repository: 
        - On GitHub navigate to the Adventureland repository and in the top-right corner of the page click 'fork';
    - Clone the project to create a local copy of the repository in your computer:
        - Within the forked repository click on the green button 'Code';
        - To clone the repository using HTTPS, under "Clone with HTTPS", click the clipboard sign. Select if you want to use an SSH key or GitHub CLI, then click the clipboard sign;
        - Open the terminal and change the directory to the location you want;
        - Type 'git clone' and paste the URL copied in step 2 and press enter to create your clone;
    - Check the Procfile to ensure a correct deployment to Heroku;

- Deployment to Heroku:
    - Create an account in Heroku;
    - Create a new app in Heroku: choose a unique name and region;
    - Introduce sensitive data needed to be kept secret in the config Var tab (Cloudinary url, Database url and Secret Key);
    - Add necessary buildpacks: Python;
    - For deployment method, GitHub was selected and confirmed we want to connect to GitHub;
    - Connect Heroku to the repository for My Recipe Blog a;
    - Set "Enable Automatic Deploys" to allow automatic deployments every time the code is pushed;
    - Click on Deploy.



## Credits


[Back to Top ⇧](#My-Recipe-Book) 