import re
import os
import sys
from celery.__main__ import main

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    os.environ['PROJECT_TYPE'] = 'CELERY'
    sys.exit(main())
