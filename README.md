# PhotoGallery

#### Created on 19th October 2021
#### By Floice Nyota Ndiiya

---
# Description  
This is A PhotoGallery Application that is able to display my photos for others to see. 
  
---
## User Stories  
User Can :-

* View different photos that interest them  
* Click a single image to expand it and view the details of that photo  
* Search for different categories   
* Copy a link to the photo to share with their friends.  
* View photos based on the location they were taken.  

---
## Access the website
Need the latest browser to be able to View

Follow this link https://photogallerynyota.herokuapp.com/

It is hosted by heroku

---

## Setup and Installation  
To get the project .......  
  
##### Clone Repository:  
 ```bash 
https://github.com/FloiceNyota98/photogallery.git
```
##### Install and activate Virtual Enviroment envgallery  
 ```bash 
cd photogallery && python3 -m venv envgallery && source envgallery/bin/activate 
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
##### Setup Database  
  SetUp Database User,Password, Host then following Command  
 ```bash 
python manage.py makemigrations photo 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run Application  
 ```bash 
 python3 manage.py server 
```
##### Test Application  
 ```bash 
 python manage.py test photo
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* HTML, CSS, Bootstrap

* Git

* Python, Django Framework

* Heroku 
  
  
## Bugs  
* It may take a while to load due to the size of the photos
  
## Contact Details
nyotafloice@gmail.com

@FloiceNyota (Twitter)

@Floice Nyota `Slack Moringa`

---

### License
This Project is under the [MIT](LICENSE) license