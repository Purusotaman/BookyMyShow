import os
import sys
import time
import pyttsx3
from playsound import playsound
from urllib.request import Request, urlopen


def main():
  if len(sys.argv) < 2:
    print("Insufficient Configuration")
    return
  
  url = sys.argv[1]
  
  htmlStr = getHtmlStr(url)
  venues = getVenues()
  matchingVenues = getMatchingVenues(htmlStr, venues)
  print(matchingVenues)
  if matchingVenues:
    triggerAlarm(matchingVenues)


def getHtmlStr(url):
  try:
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    web_byte = urlopen(req).read()
    webpage = web_byte.decode('utf-8')
    return webpage
  except Exception as e:
    print('Error fetching data !!!')
    return None


def getVenues():
  venues = [
    "PVR: VR Chennai, Anna Nagar", 
    "Rohini Silver Screens: Koyambedu",
    "AGS Cinemas: Maduravoyal",
    "SPI: Palazzo-The Forum Vijaya Mall, Vadapalani"
  ]
  return venues


def parseVenue(venue):
  return '\"VenueName\":"{}"'.format(venue)


def getMatchingVenues(htmlStr, venues):
  matchingVenues = []

  if htmlStr is None:
    return matchingVenues

  for venue in venues:
    if parseVenue(venue) in htmlStr:
      matchingVenues.append(venue)
  
  return matchingVenues


def triggerAlarm(matchingVenues):
  engine = pyttsx3.init()
  alarmConfig = 5 if len(sys.argv) < 2 else int(sys.argv[2])

  for venue in matchingVenues:
    for i in range(alarmConfig): playsound("alarm.mp3")
    engine.say("Booking opened in {}".format(venue))
    engine.runAndWait()

def fetchCronTime():
  if len(sys.argv) == 4:
    return int(sys.argv[3])
  return 300

if __name__ == '__main__':
  cronTime = fetchCronTime()
  while True:
    try:
      main()
    except Exception as e:
      print("Caught it!")
    finally:
      print("Sleeping for {} seconds or {} minutes".format(cronTime, cronTime // 60))
      time.sleep(cronTime)

