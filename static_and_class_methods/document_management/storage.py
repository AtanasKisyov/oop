class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    @staticmethod
    def get_object(iterable, object_id):
        return [x for x in iterable if x.id == object_id][0]

    def edit_category(self, category_id, new_name):
        category = Storage.get_object(self.categories, category_id)
        category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = Storage.get_object(self.topics, topic_id)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        document = Storage.get_object(self.documents, document_id)
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = Storage.get_object(self.categories, category_id)
        if category in self.categories:
            self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = Storage.get_object(self.topics, topic_id)
        if topic in self.topics:
            self.topics.remove(topic)

    def delete_document(self, document_id):
        document = Storage.get_object(self.documents, document_id)
        if document in self.documents:
            self.documents.remove(document)

    def get_document(self, document_id):
        return Storage.get_object(self.documents, document_id)

    def __repr__(self):
        return '\n'.join(repr(x) for x in self.documents)
