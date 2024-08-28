# Django Passkey Example App

## Project Overview

This project implements a web application with a login system using Corbado' passkey-first authentication service
integrated with a Django backend. The application consists of two main pages: a login page and a home page. Once users
log in successfully via the Corbado service on the login page, they are redirected to the home page where they can log
out and view protected content.

Please see the [full blog post](https://www.corbado.com/blog/django-passkeys) to understand all the required steps to integrate passkeys into Django apps.

## Tools and Technologies Used

- **Django**: A full-featured Python web framework, used to build the backend of the application.
- **Corbado**: An authentication service used to handle passkey-first user authentication.
- **HTML & CSS**: Used to structure and style the frontend of the application.

## Features

- **Passkey-first Authentication**: Utilizes Corbado's authentication service for secure user login.
- **Session management**: Uses Corbado's session management to display content based on the user's authentication status.

## How to Use

### 1. File structure
```
├── .env                    # Contains all environment variables
├── passkeys_demo
|   ├── settings.py         # Global settings
|   ├── urls.py             # Route config
|   ├── views.py            # Controller for our pages
|   ├── templates
|   |   ├── index.html      # Login page
|   |   └── profile.html    # Profile page
```

### 2. Setup
#### Step 2.1: Clone the Repository

Clone this repository to your local machine by running:

```sh
git clone https://github.com/corbado/example-passkeys-django
```

#### Step 2.2: Create .env File

To configure the credentials, you will need to create a `.env` file with your `Project ID` and `API secret` from Corbado:
To get your `Project ID` and `API secret` visit your [Corbado developer panel](https://app.corbado.com/?technology=passkeys&framework=Django#signup-init).

Please refer to the [Corbado docs](https://docs.corbado.com/overview/welcome) for more details on obtaining the
necessary credentials and integrating Corbado authentication in your application.

```sh
PROJECT_ID=<your-project-id>
API_SECRET=<your-api-secret>
```

#### Step 2.3: Configure Corbado project

In the Corbado developer Panel, visit the [URLs settings](https://app.corbado.com/app/settings/general/urls) and enter the values shown in the image below:

![Corbado developer panel URL](https://github.com/user-attachments/assets/533857f6-cd2f-42fe-b72b-c4b0277f8300)


#### Step 2.4: Run the Project

Use the following command to run the project in a docker container:

```sh
docker compose up
```

### 3. Usage

After step 2.4. your local server should be fully working.

If you now visit [http://localhost:8000](http://localhost:8000), you should be able to sign up using the Corbado UI component.

![django passkeys ui component](https://github.com/user-attachments/assets/8d894ba6-17b7-4769-b5ff-3dd9ec5b648a)


When authenticated you will be forwarded to the `/profile` page.

<img width="1435" alt="Django Passkey List" src="https://github.com/user-attachments/assets/3d67f3db-205c-455e-99f6-31ddb63171a3">




