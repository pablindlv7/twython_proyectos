from twython import Twython
from auth import  (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )

twitter = Twython (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )

#Configuración para Texto
#message= "LAS VACACIONES #ESONOALCANZA"
#twitter.update_status(status=message)
#print("Tweeted: " + message)


#Configuración para imagen
#message = "Palacio Maya"
#image = open ("palaciomaya.jpeg" , "rb" )
#response = twitter.upload_media(media=image)              
#media_id = [response["media_id"]]              
#twitter.update_status(status=message, media_ids=media_id)
#print("Tweeted: " + message)


#Configuración para video
message = "SE ACABA EL TIEMPO SEÑOR ESPONJA"
video = open ("tiempo.mp4" , "rb" )
response = twitter.upload_video(media=video, media_type="video/mp4")              
media_id = [response["media_id"]]              
twitter.update_status(status=message, media_ids=media_id)
print("Tweeted: " + message)