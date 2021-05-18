#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/sigopt/sigopt-examples/blob/experiment-management/surprise_recommender.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# ![Two-Sigma_SigOpt_Logo_300px.png](data:image/png;base64,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)
# 
# Recommendation systems are some of the most fundamental and useful applications that machine learning can deliver to businesses. Also known as recommender systems, these algorithms typically suggest what movie to watch next, what blog to read, or which product to buy.
# 
# Today we'll use a dataset from [MovieLens](https://grouplens.org/datasets/movielens/), featuring movie reviews in plaintext right alongside various scores, associated with specific users and specific films. This dataset is built right into Surprise, which leverages the scikit model, the most famouse example of which is likely scikit-learn, which we've explored in the past, and will use again in a future blog post on Natural Language.
# 
# [Surprise](http://surpriselib.com/) is both useful and simple because it can train a model that serves recommendations by using simple annotated data that includes fields for user ratings, item ratings, total user counts, item counts, ratings, and rating scale, all of which is required to build a simple recommender system.
# 
# Meanwhile, Surprise includes the SVD algorithm as standard, similar to Probabilistic Matirx Factorization, that became popular thanks to the [Netflix Prize](https://en.wikipedia.org/wiki/Netflix_Prize), a recommendation systems copmetition that took place over multilple years, between 2006 and 2009.
# 
# Here we'll look at two standard metrics, RMSE (root mean squared error) and MAE (mean average error) with cross-validation on a 5-way split. We'll later compare this result to a simpler 3-way random test-train-evaluation split.

# In[ ]:


get_ipython().system('pip install scikit-surprise')
# !conda install -y -c conda-forge scikit-surprise # If you use conda on a non-Colab environment

from surprise import SVD
from surprise import Dataset
from surprise.model_selection import cross_validate

# Load the movielens-100k dataset (download it if needed),
data = Dataset.load_builtin(name='ml-100k', prompt=False)

# Or if you'd rather, comment the above line and uncomment the below line 
# for a larger data set, while anticipating longer training times.

# data = Dataset.load_builtin(name='ml-1M', prompt=False)

# We'll use the famous SVD algorithm.
algo = SVD()

# Run 5-fold cross-validation and print results
cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)


# ## Splitting up the dataset:
# 
# This time we'll simply use a training set and a test set, as is both common and standard in scikit-learn:

# In[ ]:


from surprise import accuracy
from sklearn.metrics import mean_absolute_error
from surprise.model_selection import train_test_split

# sample random trainset and testset
# test set is made of 25% of the ratings.
trainset, testset = train_test_split(data, test_size=.25)

# We'll use the famous SVD algorithm.
algo = SVD()

# Train the algorithm on the trainset, and predict ratings for the testset
algo.fit(trainset)
predictions = algo.test(testset)

# Then compute RMSE
accuracy.rmse(predictions)


# The above result seems fairly reasonable, but it stands to reason that with either tweaking or tuning, we might do a little better. Let's start off with the exhaustive and typicaly time-consuming approach, grid search.
# 
# ## Set a baseline with a simple grid search:

# In[ ]:


from surprise.model_selection import GridSearchCV
param_grid = {'n_epochs': [5, 10], 'lr_all': [0.002, 0.005],
              'reg_all': [0.4, 0.6]}
gs = GridSearchCV(SVD, param_grid, measures=['rmse', 'mae'], cv=3)

gs.fit(data)

# best RMSE score
print(gs.best_score['rmse'])

# combination of parameters that gave the best RMSE score
print(gs.best_params['rmse'])


# But can we still improve? Of course we can. SigOpt's ensemble, including Bayesian Optimization, will very likely deliver a lower RMSE score. Let's try it out now.
# 
# If you don't yet have an account or an API key, you can [sign up for free here](https://app.sigopt.com/signup). If you click on your name at top left, you should see an "API Tokens" link where you will find your main "API Token." You should paste that in the following cell:

# In[ ]:


get_ipython().system('pip install sigopt')
# Pass your API token directly, overriding any environment variables
from sigopt import Connection
conn = Connection(client_token="YOUR_API_TOKEN_HERE")


# Now that we've successfully connected to SigOpt, it's time to define the parameters we'd like to optimize. As you can see, n_epochs is an integer, which you can increase if you're willing to spend more time training. Training time is also dependent on dataset size, so if you opted for the larger MovieLens variant, it may make sense to keep the range of epochs you wish to explore a little smaller here.

# In[ ]:


experiment = conn.experiments().create(
  name='Surprise Movies-100k Recommender',
  # Define which parameters you would like to tune
  parameters=[
    dict(name='n_epochs', type='int', bounds=dict(min=5, max=10)),
    dict(name='lr_all', type='double', bounds=dict(min=0.002, max=0.005)),
    dict(name='reg_all', type='double', bounds=dict(min=0.4, max=0.6))
  ],
  metrics=[
    dict(name='RMSE', objective='minimize', strategy='optimize'),
    dict(name='MAE', objective='minimize', strategy='store')
  ],
  parallel_bandwidth=1,
  # Define an Observation Budget for your experiment
  observation_budget=50,
)
print("Created experiment: https://app.sigopt.com/experiment/" + experiment.id)


# Although you can take a look at your experiment page now, it will be empty: we still need to define the functions required to create the model, and then evaluate its performance on the metrics we specified above, RMSE and MAE.

# In[ ]:


# Evaluate your model with the suggested parameter assignments
def create_model(assignments):
  algo = SVD(
      n_epochs=assignments['n_epochs'],
      lr_all=assignments['lr_all'],
      reg_all=assignments['reg_all']
  ).fit(trainset)
  return algo

def evaluate_model(assignments):
  algo = create_model(assignments)
  predictions = algo.test(testset)
  # Then compute RMSE and MAE:
  return [
      dict(name="RMSE", value=accuracy.rmse(predictions)),
      dict(name="MAE", value=accuracy.mae(predictions))
    ]


# Now we'll run the optimization loop. Note that we are are tracking "values" instead of "value" because we have multiple metrics. In this case, we're choosing to optimize against only one, but it is possible to optimize against both. Because these metrics should be related by a scaling factor, I wouldn't expect to see much benefit from optimizing against both.
# 
# *Note:*
# 
# The full 60 epochs we've specified here will take roughly 5 minutes to complete on the 100k dataset.

# In[ ]:


# Run the Optimization Loop until the Observation Budget is exhausted
while experiment.progress.observation_count < experiment.observation_budget:
  suggestion = conn.experiments(experiment.id).suggestions().create()
  value_dicts = evaluate_model(suggestion.assignments)
  conn.experiments(experiment.id).observations().create(
    suggestion=suggestion.id,
    values=value_dicts,
  )

  # Update the experiment object
  experiment = conn.experiments(experiment.id).fetch()

# Fetch the best configuration and explore your experiment
all_best_assignments = conn.experiments(experiment.id).best_assignments().fetch()
# Returns a list of dict-like Observation objects
best_assignments = all_best_assignments.data[0].assignments
print("Best Assignments: " + str(best_assignments))
print("Explore your experiment: https://app.sigopt.com/experiment/" + experiment.id + "/analysis")


# 
# As you can see from the above metric trajectory, we've improved markedly on our grid search results, and really only needed 40 or so experimentation loops for this particular problem. On your own, you may find that more epochs are required for improved performance on the larger (1M row) Movielens dataset.
# 
# Credit goes to Nicolas Hug from Facebook AI Research (FAIR) for implementing and maintaining scikit-surprise. You can find the documentation [here](https://surprise.readthedocs.io/en/stable/getting_started.html) from which these SigOpt-enhanced examples were developed, and without which this work would not be possible! Kudos to Nicolas for building such a simple and elegant library.
# 
# If you'd like to try another Spark MLLib recommender system that uses Collaborative Filtering, you can [find that code example here](https://github.com/sigopt/sigopt-examples/tree/master/spark/recommender_sys).

# Thanks for trying out this example today, and if you'd like to be notified of more technical content in the future, be sure to [sign up for updates here](https://modeling.sigopt.com/blogupdates).
# 