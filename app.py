import twint
from flask import jsonify
import json
c = twint.Config()
c.Search = "\"I'm at\" OR \"checked in\" OR \"went to\" OR visited"
c.Geo = "41.660769,-73.931236,500km"
c.Stats = True
c.Since = "2018-01-01"
c.Until = "2019-01-01"
c.Hide_output=True
c.Pandas = True
c.Store_json= True
c.Output = "file2.json"

twint.run.Search(c)
#tweets = twint.output.panda.Tweets_df
#print(tweets.empty)
