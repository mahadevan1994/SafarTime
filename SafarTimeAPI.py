import sys
import json
from flask import Flask
from flask import request
from jproperties import Properties

app = Flask(__name__)
configs = Properties()

with open('SafarTimeAPI-config.properties', 'rb') as config_file:
    configs.load(config_file)

if len(sys.argv) > 1:
	option = 1 if sys.argv[1] == configs["GOOGLE_MAPS_REALTIME_API_CALL_ARG"].data else 0
else:
	option = 0

if option == 1:
	"""
	#UNDER DEVELOPMENT
	Implementation needs to be as below:
	response = requests.get("https://maps.googleapis.com/maps/api/js?key=API_KEY_HERE&callback=initMap&libraries=&v=weekly")
	directionsService.route(
    {
      origin: {
        query: document.getElementById("start").value,
      },
      destination: {
        query: document.getElementById("end").value,
      },
      travelMode: google.maps.TravelMode.TRANSIT,
      transitOptions: {
    		modes: ['BUS'],
    		routingPreference: 'FEWER_TRANSFERS'
  		},
      
    },
	"""
	print('Coming soon, stay tuned...')
	quit()

#Getting response stored in files
"""
Sample GET request: http://localhost:5000/safartime/v1/getroute?from=Hebbala&to=SilkBoard
"""

@app.route('/safartime/v1/getroute')
def get_route():
	source = request.args[configs["GETROUTE_FROM_PARAM"].data]
	dest = request.args[configs["GETROUTE_TO_PARAM"].data]
	pick_file = configs["API_RESPONSE_STORED_FILENAME_PREFIX"].data+source+'_'+dest+configs["API_RESPONSE_STORED_FILETYPE"].data
	with open(configs["FILE_PATH"].data+'/'+pick_file) as response_file:
		data = json.load(response_file)
	return data

if __name__ == "__main__":
    app.run(debug=True)