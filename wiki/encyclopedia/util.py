import re
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return sorted(re.sub(r"\.md$", "", filename)
                  for filename in filenames if filename.endswith(".md"))

def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown content.
    If an existing entry with the same title already exists, it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))

def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such entry exists, returns None.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        with default_storage.open(filename, "r") as f:
            return f.read()
    return None
