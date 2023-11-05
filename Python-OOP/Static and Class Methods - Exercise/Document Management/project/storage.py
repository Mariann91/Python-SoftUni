from typing import List

from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    @staticmethod
    def return_object(object_id, object_list):
        returned_object = next(filter(lambda x: x.id == object_id, object_list))

        return returned_object

    def add_category(self, category: Category) -> None:

        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:

        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:

        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str) -> None:

        Storage.return_object(object_id=category_id, object_list=self.categories).edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:

        Storage.return_object(object_id=topic_id, object_list=self.topics).edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None:

        Storage.return_object(object_id=document_id, object_list=self.documents).edit(new_file_name)

    def delete_category(self, category_id) -> None:

        category_to_delete = Storage.return_object(object_id=category_id, object_list=self.categories)

        self.categories.remove(category_to_delete)

    def delete_topic(self, topic_id) -> None:
        topic_to_delete = Storage.return_object(object_id=topic_id, object_list=self.topics)

        self.topics.remove(topic_to_delete)

    def delete_document(self, document_id) -> None:
        document_to_delete = Storage.return_object(object_id=document_id, object_list=self.documents)

        self.documents.remove(document_to_delete)

    def get_document(self, document_id) -> object:
        return Storage.return_object(object_id=document_id, object_list=self.documents)

    def __repr__(self):
        return "\n".join(item.__repr__() for item in self.documents)
