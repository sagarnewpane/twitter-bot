import tweepy

def start_bot(img,author):
    # API keyws that yous saved earlier
    api_key = "R5hFaRx39t3ZFaH2SQ1RGPg65"
    api_secrets = "2PRjgAKXKZNykI4zEe5DHCgdJjVxiKREiASFuV3eKlne5Zjwjz"
    access_token = "1056204702231093248-wFyzhgwPtP9AfE04x69gBrFyLnjSeD"
    access_secret = "YKBXunZYHMlIvKErpUnppi1IhupB8urQdK7g5ewa92PMn"
    
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(api_key,api_secrets)
    auth.set_access_token(access_token,access_secret)
    api = tweepy.API(auth)

    # Upload image
    media = api.media_upload(img)
    # Post tweet with image
    tweet = 'Quote By : '+ author
    post_result = api.update_status(status=tweet, media_ids=[media.media_id])
    
    try:
        api.verify_credentials()
        print('Successful Authentication')
    except:
        print('Failed authentication')

