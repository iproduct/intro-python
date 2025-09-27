import json
import os
from uuid import UUID
from datetime import datetime
from enum import Enum
from typing import TypeVar, Type

from dao.id_generator import IdGenerator
from dao.repository import Repository
from model.answer import Answer
from model.instructor import Instructor
from model.question import Question, QuestionType
from model.student import Student
from model.test import Test

ENTITY_CLASSES = {Student, Instructor, Test, Question, Answer, QuestionType}


class RepositoryJsonFile[T](Repository):
    def __init__(self, filename: str, id_generator: IdGenerator):
        self.filename = filename
        self.id_generator = id_generator
        self._entities = {}
        self._entity_classes = {cls.__name__: cls for cls in ENTITY_CLASSES}


    def __contains__(self, item: T) -> bool:
        return item in set(self._entities.values())

    def __iter__(self):
        return iter(self._entities.values())

    def __len__(self) -> int:
        return len(self._entities)

    def add(self, entity: T):
        entity.id = self.id_generator.generate_id()
        self._entities[entity.id] = entity
        self.save_to_file()
        return entity

    def edit(self, entity: T):
        self._entities[entity.id] = entity
        return entity

    def delete(self, entity_id):
        old = self.find_by_id(entity_id)
        del self._entities[entity_id]
        return old

    def find_by_id(self, entity_id):
        return self._entities[entity_id]

    def find_all(self):
        self.load_from_file(self._entity_classes, overwrite=True)
        return list(self._entities.values())

    def load_from_file(self, entity_classes: dict[str, Type], overwrite: bool = False):
        def _object_hook_factory(entity_cls: dict[str, Type]):
            def object_hook(obj):
                class_name = obj['__class']
                cls = entity_cls[class_name]
                if issubclass(cls, Enum):
                    return cls[obj['value']]
                elif class_name == UUID:
                    return UUID(obj['value'])
                else:
                    instance = cls()
                    del obj['__class']
                    instance.__dict__.update(obj)
                    return instance

            return object_hook

        with open(self.filename, "r", encoding="utf-8") as f:
            self._entities = {
                entity.id: entity for entity in json.load(f, object_hook =_object_hook_factory(entity_classes))
            }
    def save_to_file(self):
        def _dumper(obj):
            if isinstance(obj, datetime):
                return {
                    "__class": obj.__class__.__name__,
                    "value": obj.isoformat()
                }
            elif isinstance(obj, Enum):
                return {
                    "__class": obj.__class__.__name__,
                    "value": obj.name
                }
            elif isinstance(obj, UUID):
                return {
                    "__class": obj.__class__.__name__,
                    "value": str(obj)
                }
            else:
                result = dict(obj.__dict__)
                result.update({"__class": obj.__class__.__name__})
                return result

        dirname = os.path.dirname(self.filename)
        if dirname:
            os.makedirs(dir, exist_ok=True)
        # self.load_from_file()
        with open(self.filename, 'w', encoding="utf-8") as f:
            json.dump(list(self._entities.values()), f, indent=4, default=_dumper)
