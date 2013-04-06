import uuid
import os
from vyazma import settings

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(getattr(settings, 'IMAGE_UPLOAD_TO', 'catalog/'), filename)