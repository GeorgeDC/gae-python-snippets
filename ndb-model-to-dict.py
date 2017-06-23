# Source:
#  https://stackoverflow.com/questions/16850136/ndb-to-dict-method-does-not-include-objects-key

class ModelUtils(object):
    def to_dict(self):
        result = super(ModelUtils, self).to_dict()
        result['id'] = str(self.key.id())
        return result

# Usage

class MyModel(ModelUtils, ndb.Model):
    name = ndb.StringProperty()
