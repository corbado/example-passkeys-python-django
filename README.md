# Passkey-First Authentication with Django and Corbado

## 1. File structure
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

## 2. Setup
### Step 2.1: Clone the Repository

Clone this repository to your local machine by running:

```sh
git clone https://github.com/corbado/example-passkeys-django

```

### Step 2.2: Create .env File

To configure the credentials, you will need to create a .env file with your project ID and API secret from Corbado:
To get your project ID and API secret visit your [Corbado developer panel](https://app.corbado.com/).

Please refer to the [Corbado docs](https://docs.corbado.com/overview/welcome) for more details on obtaining the
necessary credentials and integrating Corbado authentication in your application.

```sh
PROJECT_ID=<your-project-id>
API_SECRET=<your-api-secret>

```

### Step 2.3: Run the Project

Use the following command to run the project in a docker container:

```sh
docker compose up
```

## 3. Usage

After step 2.2. your local server should be fully working.

If you now visit [http://localhost:8000](http://localhost:8000), you should be able to sign up using the Corbado web component.

<img width="1125" alt="webcomponent" src="https://github.com/corbado/example-passkeys-django/assets/23581140/1390088d-26bd-4a69-b8d8-d87334a5c9a6">


When authenticated you will be forwarded to the `/profile` page.

<img width="1125" alt="profile_page" src="https://github.com/corbado/example-passkeys-django/assets/23581140/340a7ec2-2e3a-44bb-b781-bbe42f215f0c">



