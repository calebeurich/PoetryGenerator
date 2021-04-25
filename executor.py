import pickle

seuss_trees = pickle.load( open( 'trees/' + "seuss_trees.pickle", "rb" ) )
thug_trees = pickle.load( open( 'trees/' + "thug_trees.pickle", "rb" ) )

print(thug_trees[300])