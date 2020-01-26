import tweepy as tw
import pandas
import re
from textblob import TextBlob
import json
import argparse

def main():
    
    parser=argparse.ArgumentParser()
    parser.add_argument("--credential_file","-cf",dest="fname",default='credential_file.txt',help="Name of the file with twitter credential stored in separate lines. default='credential_file.txt'")
    parser.add_argument("--query","-q",dest="query",default='query.txt',help="Search query file name for tweets. default='query.txt'")
    parser.add_argument("--num","-n",dest="num",default=100,help="number of tweets to parse. default=100")
    args=parser.parse_args()
    
    file=args.fname
    query=args.query
    numt=int(args.num)
    
    # input arguments
    with open(query,'r') as q:
        queryt=q.readline()
    
    with open(file,'r') as cf:
        string=cf.readlines()
    cred=[]
    for i in range(0,len(string)-1):
        cred.append(string[i][:-1])
    cred.append(string[i+1])
        
    df=get_tweets(cred[0],cred[1],cred[2],cred[3],query=queryt,num=numt)
    print('\n\n')
    print(df)

def get_tweet_sentiment(tweet): 
    ''' 
    Utility function to classify sentiment of passed tweet 
    using textblob's sentiment method 
    '''
    # create TextBlob object of passed tweet text 
    analysis = TextBlob(clean_tweet(tweet)) 
    
    # set sentiment 
    if analysis.sentiment.polarity > 0: 
        return 'positive'
    elif analysis.sentiment.polarity == 0: 
        return 'neutral'
    else: 
        return 'negative'
    
def clean_tweet(tweet): 
    ''' 
    Utility function to clean tweet text by removing links, special characters 
    using simple regex statements. 
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def count_entities(i):
    if 'media' in i:
        return len(i['media'])
    return 'None'


def get_tweets(ck='None',cs='None',at='None',ats='None',query='@MercedesBenz good OR @MercedesBenz bad OR @MercedesBenz love OR @MercedesBenz hate',num=10):
    
    
    auth = tw.OAuthHandler(ck, cs)
    auth.set_access_token(at, ats)
    api = tw.API(auth, wait_on_rate_limit=True)

        
    print("Writing tweet objects to JSON please wait...")
    dlist=[]
    for tweet in tw.Cursor(api.search, q=query ,lang='en',tweet_mode='extended').items(num):
        dlist.append(tweet._json)
    with open('tweets.json', 'a', encoding='utf-8') as f:
        json.dump(json.dumps(dlist),f)
    
    with open('tweets.json','r',encoding='utf-8',newline='') as tf:
        j=json.load(tf)
    j1=json.loads(j)
   
    text=[]
    user=[]
    fav=[]
    rt=[]
    date=[]
    sentiment=[]
    entities=[]
    for tweets in j1:
        if (not tweets['retweeted']) and ('RT @' not in tweets['full_text']):
            text.append(tweets['full_text'])
            #print(tweets.full_text,'\nhi\n')
            user.append(tweets['user']['name'])
            fav.append(tweets['favorite_count'])
            rt.append(tweets['retweet_count'])
            date.append(tweets['created_at'])
            sentiment.append(get_tweet_sentiment(tweets['full_text']))
            entities.append(count_entities(tweets['entities']))
    
    dictionary={'Text of Tweet':text,
                 '# of Likes':fav,
                 '# of Retweets':rt,
                 'Date Tweeted':date,
                 'User':user,
                 'Sentiment of the Tweet':sentiment,
                 '# of Media Items in Tweet':entities}
     
    df=pandas.DataFrame(data=dictionary)
        
    return df
    
if __name__=="__main__":
    main()