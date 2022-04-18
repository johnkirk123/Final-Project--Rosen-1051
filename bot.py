#John Kirkpatrick


#1.) Import tweepy and time
import tweepy
import time




#2.) Store developer account passwords
apiKey='TP74USEMSfclYuRdIC9fQVL80'
apiSecret='xM4pQexZPvCVYklndzJD0ho9EMhcJvX3gfzgEeuXAg5RqPztLX'
accessToken= '1513610359004876808-VHCzkeJmLTja5Td0r9zINyb8JNRsHN'
accessSecret= 'sXrRnrKIOu8RrXTr9oa2XZ6tzbtsILpLmq407sNFCcAhw'


#3.) Create Oauth client ans set authentication and create API object
oauth= tweepy.OAuthHandler(apiKey,apiSecret)
oauth.set_access_token(accessToken, accessSecret)
print('Authentication successful')


api = tweepy.API(oauth)

#4.) Upload media
def tweet():

    media= api.media_upload('ts.MOV')
    result= api.update_status(status= "Tony Soprano cries while listening to Accidentally in Love by the Counting Crows", media_ids= [media.media_id_string]) 
    print('Upload success')

tweet()








        


