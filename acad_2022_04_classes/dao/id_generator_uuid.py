import uuid

class IdGeneratorUuid:
    def get_next_id(self):
        return uuid.uuid1()