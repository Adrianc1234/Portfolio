# How to Use the Google API
### Tutorial about How to Use the Google API 

First you need to get the Google API key to have access to the resources of Google Cloud Platform. 
The API key is a unique identifier that is used to authenticate requests associated with your project for usage and billing purposes.

## To get an API key:

1. Visit the Google Cloud Platform Console.
2. Click the project drop-down and select or create the project for which you want to add an API key.
3. Click the menu button  and select APIs & Services > Credentials.
4. On the Credentials page, click Create credentials > API key.
    The API key created dialog displays your newly created API key.
5. Click Close.
  The new API key is listed on the Credentials page under API keys.
  (Remember to restrict the API key before using it in production.)
  
 That is all you have to do, if you are a new user of the Google API, you will get 300 dollars to spent for 12 months!!!
 
 ## Define what you would like to do
 
 Depending on what you would like to do, you choose the corresponding url required to make a request and fill its gaps with the inputs
 required and the extra data you would like to have as a response, check the example below:
 ```
 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&radius=2000&type={}&key={}'
 ```
 In this case, we are using the Places API to find the nearby places with the latitude and longitude as input parameter as well as the radius the type and the most important, the key, as it would allow you to make the request.
 
 As you may have noticed, the separator between parameters is the ```&``` symbol, so keep in mind
 
 It also shows which is the output, in this case it is a JSON (Recomended), but it also can be a xml.
  
## Add the API key to your request
 
 You must include an API key with every Places API request. In the following example, replace YOUR_API_KEY with your API key.
```
https://maps.googleapis.com/maps/api/place/nearbysearch/json
  ?location=-33.8670522,151.1957362
  &radius=500
  &types=food
  &name=harbour
  &key=YOUR_API_KEY
```
### Display your data 
  As you may have noticed a JSON is hard to navigate, so lest display it as datafreme in form of a table, to be more visually friendly.
  In a function we declare the url.
```
def search_nearby_place(latitude, longitude, place, key):
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&radius=2000&type={}&key={}'.format(
        latitude, longitude, place, key)
    res = requests.get(url)
    results = json.loads(res.content)
    return results     
```
Call the function with the location, the type restaurant and the API key.
```
raw_data = search_nearby_place(20.988459, -89.736768, 'restaurant', YOUR_API_KEY)
```
Display your table with the specific columns that you would like to have to appear.
```
restaurantes_yucatan = pd.read_json(json.dumps(raw_data['results']), orient = 'records')
restaurantes_table = restaurantes_yucatan[['name', 'place_id', 'rating', 'types','user_ratings_total']]
restaurantes_table
```
To do this do not forget to import the required libraries (requests, json, pandas).

## Comparison between  Google Maps [Places API] and GoogleMaps library
  THe use of Places API requires you to work with the string that eventually will work as url, and this is helpful when you want
  to create your own functions with specific porpouses, but there are already functions in the GoogleMaps library that have a similar 
  functionality, and you do not have to work directly with the url.
  
  Lets see another example of Places API:
  ```
    def find_place_id(placeName, location, key):
      placeName = urllib.parse.quote(placeName)
      url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={}&inputtype=textquery&locationbias=circle:600@{},{}&key={}'.format(placeName, location[0], location[1], key)
      res = requests.get(url)
      results = json.loads(res.content)
      return results  
  ```
In the example above, we ask for the id_place with Find Place From Text, we are working directly with the url, below we have an example with the library GoogleMaps.
  First import the correspondig library, and eventually store your API key with the function Client which will help you to never write the 
  API key again in case you use another funtion.
```
import googlemaps
gmaps = googlemaps.Client(key= API_KEY)
```
An the you call the function that you require, in this case a similar to Places API, to clarify the comparison between the two.
```
geocode_place_id = gmaps.find_place('McCarthys Irish Pub - Caucel', input_type ='textquery',
                                    location_bias='circle:600@20.999917,-89.682576')
```
Both options will have the same output, but with the Places API you requre to wotk directly with the url, which could have its pros and cons, depending on what you want to do, for example if you want to create your specific functions with a specific output, in the other had the library GoogleMaps already have a set of functions for you to use, but those may be not satisfies your objectives.

## Documentation and Resources 

[Get an API Key](https://developers.google.com/places/web-service/get-api-key)

[Places API](https://developers.google.com/places/web-service/search#FindPlaceRequests)

[Google Maps Services Github](https://github.com/googlemaps/google-maps-services-python#api-keys)

[Overview Place API](https://developers.google.com/places/web-service/intro)

[Python Client for Google Maps Services Documentation](https://googlemaps.github.io/google-maps-services-python/docs/#module-googlemaps)
