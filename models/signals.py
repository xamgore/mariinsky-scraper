from datetime import datetime


def update_modified(sender, document):
    document.modified = datetime.utcnow()
