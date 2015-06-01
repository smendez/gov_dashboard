#Gov Dashboard

## What is Gov Dashboard?
The government dashboard is a companion tool to data.pr.com to make it easier to follow desired statistics.

## Who can use Gov Dashboard?
Anyone with access to Github can download the source code and either run the Dashboard locally or install it PaaS 
platform such as Heroku or OpenShift.

## How to get Gov Dashboard?
Please see the [Commonwealth of Puerto Rico](https://github.com/commonwealth-of-puerto-rico/gov_dashboard) Github 
repository.

## Technology
Please read [here](https://github.com/commonwealth-of-puerto-rico/gov_dashboard/blob/master/requirements.txt).

## How to get started?

### Create a data.pr.gov account
You will need to [create](https://data.pr.gov/en/signup) an account to be able to used this dashboard.

### Create a app token
Once you've created your account, you will need to create an app token. Go to your home page, and at the bottom you 
will see "Aplicaciones de *tu_usuario*" or "*your_user* aplications". Next to that will be "Administrar" or "Manage". 
Click here and then click "Create New Application" or "Crear nueva aplicación". Fill in the blanks and generate your 
app token and secret token.

### Setting up the Gov Dashboard
In the Dashboard, your app token will be CLIENT_ID and your secret token will be CLIENT_SECRET. These can go in a 
.env file or a local_settings.py file. Also include the following in your .env or local_settings:

* AUTHORIZE_URL=https://data.pr.gov/oauth/authorize
* TOKEN_URL=https://data.pr.gov/oauth/access_token

These all will have to be set as environmental variables when deploying to Heroku.

### Sample data
In your project directory, run the following command to load sample data into your dashboard:

```
./manage.py loaddata dashboard/fixtures/dashboard_sample_data.json
```

## Using the Gov Dashboard
Create an admin user for your dasboard:

```
./manage.py createsuperuser
```

And follow the prompts. Log into the admin (http://127.0.0.1:8000/admin) you can add a Category and a Data Point.

### Creating a Data Point
For any dataset in data.pr.gov, go to the "Export" or "Exportar" tab. Here you will see the SODA API endpoint. This url
is were the dashboard is going to look for information. When creating a data point, this will go in the *resource* 
field. Then put a date field in *date field* and the data you want to track in *data field*.

For example, let's say you want to track [data](https://data.pr.gov/Desarrollo-e-Infraestructura/Generacion-y-demanda-de-energia-PR/mt8n-mwk8) 
from AEE. In this data set, [this](https://data.pr.gov/resource/mt8n-mwk8.json) is the SODA API endpoint, and that would 
be the Data Point *resource*. My date field would be *fecha* and the data to be tracked is demand, so my data field is *demanda_maxima*.

Mark *Featured Set?* to make this Data Point visible on the home page. Mark *Upward trend positive?* if you consider this data to be positive.


