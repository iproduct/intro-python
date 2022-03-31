import uuid

class IdGeneratorUuid:
    def get_next_id(self):
        return str(uuid.uuid1())