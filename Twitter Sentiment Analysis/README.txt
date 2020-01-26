When running the script through console please paste your twitter app credentials in the file named 'credential_file.txt'(every credential should be separated by newline and in order: consumer_key, consumer_secret, access_token, access_token_secret) and the search query for tweets in a file named 'query.txt' in single line.

You can use a different file name as well but then you have to pass those file names as arguments while running script as:
python get_tweets.py --credential_file <your credentials file name> --query <your query file name> --num <number of tweets you want your script to parse>

Everytime before running the script, please move the old .json file somewhere other than current working folder, so that any desireable data could be preserved from your last search.