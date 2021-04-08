from invenio_search import RecordsSearch


class CommonRecordsSearch(RecordsSearch):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._source = self._source = self._source = [
            'control_number', 'oarepo:validity.valid', 'oarepo:draft', 'title', 'dateIssued',
            'creator', 'resourceType', 'contributor', 'keywords', 'subject', 'abstract', 'state',
        ]
        self._highlight['title.cs'] = {}
        self._highlight['title._'] = {}
        self._highlight['title.en'] = {}