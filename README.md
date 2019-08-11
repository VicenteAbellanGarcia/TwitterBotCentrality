# TwitterBotCentrality
This is a twitter bot which calculate the Centrality of a number of twitter accounts based in a search of words and the accounts relations
that have tweeted about that words generating a graph and associating a value to each account.

![alt tag](https://i.gyazo.com/b12921b92f62c6bb2586bc436c3857c2.png)

## How it works

- You'll need a twitter account prepared for work with the API, you can get it and check for information here: https://developer.twitter.com/en.html

- Once you have your twitter account and 1 APP created you'll recive a CONSUMER KEY, CONSUMER SECRET, ACCESS KEY and ACCESS SECRETS which
are the tokens for work. In my case, I have been using 2 accounts with 8 APPS created (you can have 4 per account as free) because you'll
have to wait if you use too many access to the API, for this bot you'll need do it.

- You will need write the previous information as a List. The firsts tokens used will be the account where the bot will tweet.

- You have to write the topic about you want to check the twitter accounts relations ("query")

- The bot'll look for the tweets, it'll get the twitter accounts who tweeted it (you can modify how many tweets you want check in "max_tweets)
and will check if that accounts are related (following and/or followed). Finally, the bot will generate a pdf with a directed graph 
of the accounts and will asociate a value for each account based in how many relations it has (Centrality)

![alt tag](https://i.gyazo.com/7a83d010d76110d96712e5af0c667e6d.png)
