import os
from django.core.files.storage import default_storage

def upload_file_to_model(instance, field_name, file):
    """
    Service to handle file uploads to a specific model field.
    Handles deleting the old file if a new one is uploaded.
    """
    # Delete old file if exists
    old_file = getattr(instance, field_name)
    if old_file and hasattr(old_file, 'path') and os.path.exists(old_file.path):
        os.remove(old_file.path)
    
    # Set the new file
    setattr(instance, field_name, file)
    instance.save(update_fields=[field_name])
    return instance
