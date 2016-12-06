from stravalib import Client
import csv

client = Client(access_token='YourAccessToken')

athlete = client.get_athlete()
activities = client.get_activities(limit=9000)

for a in activities:
  #Add an if statement to filter activity type: e.g. if a.type == 'Ride': 
  id = a.id
  name = a.name
  tp = a.type
  da = a.start_date
  types = ['time','latlng']
  streams = client.get_activity_streams(id, types=types, resolution='high')
  times = streams['time'].data
  coords = streams['latlng'].data
  dateStart = (str(da)[:-15]).replace("-", "_")

  csvFile = "C:/strava/csv/" + dateStart + "_" + str(id) + ".csv"
  with open(str(csvFile), 'wb') as myfile:
      wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
      wr.writerow(["Date", "ActivityName", "ActivityType", "lat", "lon"])
      for cor in coords:
          wr.writerows(zip([dateStart], [name], [tp], [str(cor[0])], [str(cor[1])]))
  myfile.close()
