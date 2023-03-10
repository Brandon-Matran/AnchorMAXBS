# 1/26/23:
Today I worked on:
- I got all the 404 errors to disappear. It was a very good learning experience about useEffect within our JS files. Essentially what happenened was we were trying to fetch a token without passing in a proper url. That caused React to implement a default link and add that token string to the end of the url path, which resulted in the 404 errors. With the help of the SEIR's we were able to rewrite the useEffects to work correctly and not pass in that extra data to the url.

Tomorrow:
- I will help with the README but otherwise our MVP is ready!

# 1/25/23:
Today I worked on:
- Going to run through our app on localhost to make sure all requirements for the project are met so that the entire group will get a passing grade. Currently have some small tweaks we need to make on the front end. Afterwards, we plan to make a push to main and at that point the MVP should be complete.


## 1/24/23:
Today I worked on:
- Finished deployment completeley on the front and back end. The errors regarding disk space were resolved by clearing the disk space from the CapRover app itself. Unfortunately that information was not in their documentation. The other issue was getting the token to authorize for certain permissions within the Anchor app. With the help of a SEIR, we were able to create a valid token by updating the signing key within the CapRover dashboard and now all requests are going through.

## 1/23/23:
Today I worked on:
- Still having issues with deployment where the front end is not communicating with the backend on CapRover. I plan to meet with instructors and try to figure out what is happening and how to overcome this issue.

What I need to work on:
- I ran into a huge issue where it was telling me there was no more space on the device when trying to deploy the app through CapRover. I was unable to find a solution. Will try again tomorrow.

## 1/20/23:
Today I worked on:
- Got the app deployed through CapRover.

What I need to work on:
- The database is not communicating smoothly with CapRover, I'm going to need to consult with an instructor to get it working on Monday.

## 1/18/23:
Today I worked on:
-I finished a unit test for get_all accounts list.

## 1/17/23:
Today I worked on:
-Our group decided to merge all the code from the backend onto the Main branch on GitLab so we could all start working on the FrontEnd. So together, with my group, I was able to merge all the Feature branches into main. My group also really liked the Main Page Front End I worked on so we are going to go ahead with it. We also set up our CapRover instance. We are waiting to get our MVP up before we deploy it.

-Tomorrow I plan to help the group on anything they need to get our MVP up and running.

## 1/13/23
Today I worked on:
-It's Friday, so I didn't do as much as normal. I worked more on the main page and got clearance from the group to be able to make it look however I wanted. I also created a Test Page for blog creation.

-Over the weekend I plan to focus on finishing the Main Page Front End.
## 1/12/23:
Today I worked on:
-I helped the group out on figuring out how to get the accounts table to sync up with the blogs and job listings table on the backend. We need to have all microservices on the same signing key and have them all receive the same token so that they are able "communicate" with each other.

-Tomorrow I plan to work on the Main Page.

## 1/11/23
Today I worked on:
-I created the MainPage.js and assigned a signup and login button. Then I had 1 on 1 meetings with the instructors to understand how we could restrict certain endpoints for users with different roles. For instance, a regular user can only create blogs. However, a company user can only create job listings. Code was released and I was able have a better understanding on how to do that. I also finished the update job listings story.

- Tomorrow I plan to talk over with my team how we are going to pull data from the access token to allow users for creating blogs.

## 1/10/23
Today I worked on:
-I helped finish the Signup.js on the front end. We were having issues with the account not being created when we clicked the submit button on the sign up page. Afterwards, I worked on the logout button and that was completed. Afterwards, I tried to help other classmates with their code.

- Tomorrow I plan to work on the MainPage and start putting together the front end. Also I plan to finish my last story which is the update Job Listings.

## 1/9/23
Over the weekend I:
-I was able to get my Login/Logout/Signup backend working. I am now able to receive a token upon account creation. All my endpoints are working.

Today I worked on:
-I started working on my front end, specifically the login form. I added the code for the authentication on the front end to it's own file. This file is basically a library that will allow users to login/logout/signup.

- Tomorrow I plan to finish my stories regarding Login/Logout (Back-end and Front-end)

## 1/6/23
Today I worked on:

-I was having issues with my containers so I took a look at the Docker Compose file and found that there were some syntax errors. I checked the learn modules and was able to fix them in my Docker-Compose file. My containers worked after that. Afterwards, I started the Accounts microservice. I imported the dependencies to get started on authentication. Created my models and connected FASTAPI.

-Tomorrow I plan to read through the JWTDown Authentication docs and watch the videos to get started on creating tokens.



## 1/5/23

Today I worked on:

-Finishing up the issues and features with the team.

The team finished up the features and issues today. We assigned each team member to tasks totalling up to 13 points per the grading rubric. I am in charge of Log In (Front End/Back End), Log Out(Front End/Back End), And Updating a Blog (Back End).

## 1/4/23

Today I worked on:

-The issues and features regarding Project Anchor with my team.

The team worked together on creating Features and identifying the issues that would have to be done in order to get each feature to work for the MVP.

For design decisions, we decided that tomorrow we will go over a My Jobs Page and My Blogs page.

I learned how to create issues and features using GitLab today.

## 1/3/23

Today, I worked on:

- Creating the API-Design Markdown with my team.

My team and I wrote in the API-Design.md readme about the our API endpoints and the methods
we would use to create our MVP using FASTAPI.  In the API-Design, we, together as a group came up with the names of the endpoints as well as the Request shape, Response, and Response shape for the Log In, Log out, Sign Up, Get a Blog, Get all Blogs, Create a Blog, Update Blog, Get Job Listings, and Create Job Listings.

As far as design descisions, we decided to keep our initial layout detailed in Excalidraw.

Today, I learned how to create Issues within the GitLab Group Project. I also learned how to create and assign roles to group members. Additionally, I had a quick refresher on how to merge and pull from the main repo.

Tomorrow, I want to finish the discussion over the feature and issues regarding our MVP and have our tasks assigned to each member so that we have a clearer understanding of how each person will contribute to the project.

As far as issues/features go I think we could break it up into the following:

## Log In

```
As a user
I want to be able to login
So that I can have access to read blogs, create blogs, and look at job listings
```

## Feature 1

```
Given a valid filled form by the user
When they click the "Log In" button
Then a token is generated if the account is valid and used
to log the user in
And the user is redirected to the Logged In Main Page

```


## Description

...

## Sign Up

```
As a new visitor
I want to be able to sign up
So that I can gain access to a list of blogs, create a blog, and see all job listings
```

## Feature 2

```
Given a valid form filled out by the new user
When the user fills out the form and then clicks sign up
Then the user will see a successful account creation message
And be able to access a user page which has blogs and job listings

```


## Create a Blog

```
As a user
I want to be able to create a blog
So that I can help other users with coding related issues
```

## Feature 3

```
Given a valid form is filled for create a blog
When a user clicks the submit blog button
Then they will see a successful blog created message
And be redirected to their blog
```

## Update a Blog

```
As a user
I want to be able to update my blog
So that I can change the content within my blog if corrections are needed
```

## Feature 4

```
Given a user correctly fills out a valid form for Update a blog
When the user clicks the submit update button
Then the user will be able to see a successful blog updated message
And be redirected to their blog

```


## Delete a blog

```
As a user
I want to be able to delete a blog
So that I can delete my content if I no longer want to share or if my content is no longer valid
```

## Feature 5

```
Given a user wants to delete a blog
When the user clicks the delete blog
Then the user is asked if they really want to delete their blog
And if the user clicks Yes then the blog is deleted and a successful delete blog message is shown

```

## View Job Listings

```
As a user
I want to be able to view job listings
So that I can apply to jobs that fit my experience and interests
```


## Feature 6

```
Given a user wants to view job listings
When the user clicks the job listings button within the dropdown menu
Then the user is directed to all the job listings available
And the user is able to click the apply button and be directed to the companies page

```

## Create a Job

```
As a company user
I want to be able to post a job listing
So that an applicant can apply to the position I posted
```

## Feature 7

```
Given a company wants to inform users that they have a job listing
When a company user clicks the create a job button
Then they will be directed to a form that allows them to create a job
And upon successful create a job form filled they will see their job listing put on the job listing page
...
```
