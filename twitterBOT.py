import tweepy
from unsplash_search import UnsplashSearch
from time import sleep
from py_unsplash_source import PyUnsplashSourceClient
#Burda boş bırakıldı siz kendi Twitter keylerinizi yazmalısınız.
consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""
unsplash = UnsplashSearch("RszBAE1P-AsvFhNEdCbgOQIp-PhAPWKs8F256QAtR_4")
baglanti = tweepy.OAuthHandler(consumer_key, consumer_secret)
baglanti.set_access_token(access_token, access_token_secret)

api = tweepy.API(baglanti, wait_on_rate_limit=True)
su = PyUnsplashSourceClient(width=1920, height=1080)

while True:
    i=0
    i=i+1

    image = (su.random_image()
             # Or .weekly()
             .search('animal')).get()



    image.save_as('C:/Users/user/Desktop/uns/random.jpg')
    img = "C:/Users/user/Desktop/uns/random.jpg"
    api.update_with_media(img, status="#animal")
    print("Durum Güncellendi"+str(i))
    sleep(600)


#DELETE TWEETS
# for status in tweepy.Cursor(api.user_timeline).items(200):
#     api.destroy_status(status.id)
