# Source:
#  https://stackoverflow.com/questions/13311363/appengine-making-ndb-models-json-serializable

json.dumps([myModel.to_dict() for myModel in myModelList])
