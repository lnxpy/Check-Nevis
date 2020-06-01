# Check-Nevis
Do you need something to keep your schedules in?
Well, let Check Nevis (چک نویس) does that for you.

Check-Nevis is sort of a micro-service allows you to build it up on your local server and use it. Just build it and use it.
On Check Nevis, any member of your team or family may have an account for themselves, so they can sign-in and make records directly.

This tool has been made with DRF which stands for (Django Rest Framework) a high-end library to build Restful API endpoints on Django.

All endpoints will be listed once you build this project up.

### Build
Here we have the steps you need to do to set this service up.
. Clone Check Nevis
. Make `virtualenv` as you wish
. Activate your environment and install `requirements.txt` file
. Migrate all changes on DB
. Run this up and browse `localhost:8000`

Now, you've already installed Check Nevis on your local system. In spite on the browsed page all API endpoints listed, you can use the following chart to access to endpoints.


| API           |       Methods      |          Descryption         |  CRUD Style |
| :-----------: | :----------------: | :--------------------------: | :---------: |
| api/user      |       `POST`       | To create new user           |       C     |
| api/login     |       `POST`       | To Login as a user           |       C     |
| api/logout    |       `POST`       | To Logout as a user          |       C     |
| api/todo      |    `GET, POST`     | To create and list todos     |     C, R    |
| api/todo/ID   | `GET, PUT, DELETE` | To modify a specific a todo  |   R, D, U   |
| api/them      |      `GET,PUT`     | To get and change theme      |     R, U    |
| api/profile   |      `GET,PUT`     | To get and change profile    |     R, U    |

### Original Interface
__Contents will be updated__

### Fork
Fork for free :)
