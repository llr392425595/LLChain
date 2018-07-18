from flask.json import JSONEncoder

from model.block import Block


class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Block):
            return obj.serialize()
        return super(MyJSONEncoder, self).default(obj)
