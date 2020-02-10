activate_this = '/path/to/env/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
    
#!/usr/bin/python
import sys
sys.path.insert(0,"/var/www/space.wdelenclos.fr/")
from app import app as application