# BookMyShow
Visit BookMyShow at set intervals to find whether booking is opened for a given movie.

Pre-requisites
1. Python2 or Python3
2. PIP package manager
3. Package - playsound
4. Package - pyttsx3
5. URL for required movie in BookMyShow

Steps to Install
1. Download and install python3
2. Installing python should auto-install PIP as well.
3. Use "pip install playsound" to install playsound.
4. Use "pip install pyttsx3" to install pyttsx3.
5. Get the bookmyshow url.
6. Clone to repository.

BookMyShow URL Example
1. https://in.bookmyshow.com/buytickets/spider-man-no-way-home-chennai/movie-chen-ET00319080-MT/20211216
2. "endpoint/movie-[location]/movie-[location_keyword]-[movie_id]/[date]
3. If the movie is released in certain theates but not in all, you can use the exact URL.
4. If the movie is yet to be released, visit the movie page in bookymyshow to get the movie_id.
5. Recreate a similar URL. Once it it released, it'll open.
6. In-order to change the available theatres, make changes to the "venues" array in the code.
7. Venue refers to the theate name displayed in bookmyshow.
 
How to Run
```
python3 bookmyshow.py "your_movie_url" 5 900
```

1. 5 refers to the number of times the alarm will ring for each matching theatre.
2. 900 refers to the polling duration, default is 300s or 5mins.
3. Note that, the PC should be awake at all times for this to work as expected.

Why it's working?
1. Analysing the HTML rendered, we can see specific tags used to list the theatres available.
2. We are essentially searching for this tag post downloading the HTML page.
