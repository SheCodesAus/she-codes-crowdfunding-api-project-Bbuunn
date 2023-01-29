# {{ 2gather: Crowdfunding Website for Skillshare }}
​
{{ ‘2gather’ is a crowdfunding platform that promotes community building and skill sharing. People can create an event with minimum and maximum attendances, and “pledge” by attending the event. The main focus of ‘2gather’ is economically inclusive while ultimately encouraging the bond between users. Target audience is quite broad ad anyone with time and or skills can participate - although, travellers or people who have recently moved could particularly benefit from '2gather'. }}
​
## Features
​
### User Accounts
​
- [X] Username
- [X] Email Address
- [X] Password
​

### Event
​
- [X] Create an event
  - [X] Title
  - [X] Owner (a user)
  - [X] Description
  - [X] Image
  - [X] Minimum attendance
  - [X] Maximum attendance
  - [X] Open/Close (Accepting new attendees)
  - [X] When was the event created
- [X] Ability to attend an event
  - [X] An amount
  - [X] The project the event is for
  - [X] The attendee
  - [ ] Whether the attendance is anonymous
    N/A
  - [ ] A comment to go with the attendance

  
### Implement suitable update delete
​
- Event
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [X] Destroy
- Attendance
  - [X] Create
  - [X] Retrieve
  - [ ] Update
    N/A
  - [X] Destroy
- User
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [X] Destroy
​

### Implement suitable permissions
​
- Event
  - [X] Limit who can create
    Logged in user
  - [ ] Limit who can retrieve
    All
  - [X] Limit who can update
    Only event owner
  - [X] Limit who can delete
    Only event owner

- Attendance
  - [X] Limit who can create
    Logged in user
  - [ ] Limit who can retrieve
    All(In the event view)
  - [ ] Limit who can update
    Only update needed is delete
  - [X] Limit who can delete
    User who is already attending & logged in(by token)

- User
  - [X] Limit who can retrieve
    List view: Only Admin/superuser
    Detail View: Authentiated user or read only
  - [X] Limit who can update
    Only the custom user
  - [X] Limit who can delete
​    Only the custom user

### Implement relevant status codes
​
- [X] Get returns 200
- [X] Create returns 201
- [X] Not found returns 404
​
### Handle failed requests gracefully 
​
- [X] 404 response returns JSON rather than text
​
### Use token authentication
​
- [X] impliment /api-token-auth/
​
## Additional features
​
- [ ] {Title Feature}
​
{{ No additional feature added }}
​
​
### External libraries used
​
- None
​
​
## Part A Submission
​
- [X] A link to the deployed project.
  https://throbbing-silence-5067.fly.dev/
  https://throbbing-silence-5067.fly.dev/users/
  https://throbbing-silence-5067.fly.dev/events/
- [X] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
  Check ./screenshots/
- [X] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
    Check ./screenshots/
- [X] A screenshot of Insomnia, demonstrating a token being returned.
    Check ./screenshots/
- [X] Your refined API specification and Database Schema.
​   https://docs.google.com/document/d/13fHFySlohOi3jYHqkQlKPRfCOEubOs0qW1ZNKghw-DA/


### Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data).
​
1. Create User
​
```shell
curl --request POST \
  --url http://127.0.0.1:8000/users/ \
  --header 'Content-Type: application/json' \
  --data '{
		"username": "frog",
		"email": "frog@user.user",
		"password": "frog"
	}'
```
​
2. Sign in User
​
```shell
curl --request POST \
  --url http://127.0.0.1:8000/api-token-auth/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "frog",
	"password": "frog"
}'
```
​
3. Create Project
​
```shell
curl --request POST \
  --url http://127.0.0.1:8000/events/ \
  --header 'Authorization: Token 84000773eb079e73acfecc911ec64cbbde5b344b' \
  --header 'Content-Type: application/json' \
  --data '{
	"title": "Kimchi Making",
	"description": "Who wants to learn how to make kimchi? I have the skills but no one to do it together. We can BYO ingredients and go home with kimchi.",
	"location": "Local community kitchen",
	"online": false,
	"image": "https://via.placeholder.com/300.jpeg",
	"min_attendees": 1,
	"max_attendees": 15
}'
