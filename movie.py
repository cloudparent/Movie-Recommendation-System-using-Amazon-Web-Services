# Build a map to convert a movie id to the movie title
movies = pd.read_csv(dataset_dir + '/movies.csv', usecols=[0,1])
movies['movieId'] = movies['movieId'].astype(str)
movie_map = dict(movies.values)

# Getting a random user:
user_id, item_id = interactions_df[['USER_ID', 'ITEM_ID']].sample().values[0]

get_recommendations_response = personalize_runtime.get_recommendations(
    campaignArn = campaign_arn,
    userId = str(user_id),
)
# Update DF rendering
pd.set_option('display.max_rows', 30)

print("Recommendations for user: ", user_id)

item_list = get_recommendations_response['itemList']

recommendation_list = []

for item in item_list:
    title = movie_map[item['itemId']]
    recommendation_list.append(title)
    
recommendations_df = pd.DataFrame(recommendation_list, columns = ['OriginalRecs'])
recommendations_df.head()