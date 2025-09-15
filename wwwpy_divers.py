from webdiver.web_diver import *

_uri = 'https://github.com/ssmool/webdiver'
_db = 'webdiver_db.sqlite'
_hour = '13'
_minute = '13'
www_diver_add_task(_uri) # - to add PIPE FIFO URI DIVER
www_diver_start(_db,'_html') # - to get HTML content by URI
sql_setup(_db) # - to get database setting content by FILE_NAME
set_task(_uri, _hour, _minute, '_text') # - to get text content by URI check the HOURS
