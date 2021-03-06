# FindCokeZero
Mobile-first web app that provides locations of stores filtered by CokeZero flavors and user location. Django REST framework enables browsable API and administrative management. Integration with Google Maps API supports mapping.

## A very serious mission
I'm building this app because I love CherryCokeZero, but it's not omni-present and retailer inventories of all Coke flavors fluctuate.
When I find myself in a new location, I have to scout out the stores that carry it regularly.  Surely, I'm not the only one!
This app keeps track of my store inventory and uses crowd-sourcing to grow the database.


## Run the Program
1. Add your own GoogleMaps API key
  - Get an Google Maps API key [here](https://developers.google.com/maps/documentation/geocoding/get-api-key).
  - Add that string to your local environment variables, e.g. `GOOGLEMAPS_KEY="copy/paste your key here"`.
2. Enter the virtual environment
  - `. venv/bin/activate`
3. Install dependencies
  - `pip install -r requirements.txt`
4. Migrate the database
  - `./manage.py makemigrations` then `./manage.py migrate`
5. Load data from seed
  - `./manage.py loaddata initdata.json`
6. Run development server locally
  - `./manage.py runserver`
7. If static files are not running locally:
  - `./manage.py collectstatic`
8. Run tests:
  - `./manage.py test app1_findcokezero`


## API Endpoints

#### HTML LANDING PAGE

- `GET /` - serves HTML template, e.g. "www.findcokezero.com"


#### JSON API
*Don't forget closing slash unless url includes a query string*

### Retailers

|Endpoint                                         | Description                                   | Example
|-------------------------------------------------|-----------------------------------------------|------------
| GET /api/retailers/                             | retrieve all retailers                        | www.findcokezero.com/api/retailers/
| GET /api/retailers/:retailer_id/                | retrieve specific retailer                    |
| GET /api/retailers/:retailer_id/sodas/          | retrieve all retailers with specific soda     | www.findcokezero.com/api/retailers/2/sodas/
| GET /api/retailers/?postcode=:retailer_postcode | retrieve all retailers with specific postcode | www.findcokezero.com/api/retailers/?postcode=11111
| GET /api/retailers/?postcode=:retailer_postcode&sodas=:soda_abbreviations | retrieve all retailers with specific postcode and selection of soda types | www.findcokezero.com/api/retailers/?postcode=94108&sodas=CH,CZ
| POST /api/retailers                             | create retailer                               |
| PATCH /api/retailers/:retailer_id/              | edit retailer                                 |
| DELETE /api/retailers/:retailer_id/             | remove retailer                               |




### Sodas

|Endpoint                             | Description                               | Example
|-------------------------------------|-------------------------------------------|------------
| GET /api/sodas/                     | retrieve all sodas                        | www.findcokezero.com/api/sodas
| GET /api/sodas/:soda_id/            | retrieve specific soda                    |
| GET /api/sodas/:soda_id/retailers/  | retrieve all sodas at a specific retailer | www.findcokezero.com/api/sodas/2/retailers/
| POST /api/sodas/                    | create soda                               |
| PATCH /api/sodas/:soda_id/          | edit soda                                 |
| DELETE /api/sodas/:soda_id/         | remove soda                               |



## Major Dependencies
*see requirements.txt and requirements-dev.txt for full list*
- python 2.7.10
- pip 9.0.1
- virualenv 15.1.0
- Django-1.11.4
- pytz-2017.2


## Wireframes

#### Mobile Sample
![Mobile](https://res.cloudinary.com/dckkkjkuz/image/upload/v1513744099/findcokezero/Mobile2.png)


#### Web Sample
![Web](https://res.cloudinary.com/dckkkjkuz/image/upload/v1513744057/findcokezero/Web1.png)



See all [development documents][docs]

[docs]: docs/


## Future Development
- Build client that shows map of retailers based on some geographic input (e.g. current user location or manually entered zip code)

[docs]: docs/
