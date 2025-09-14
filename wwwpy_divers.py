from webdiver.web_diver import *

www_diver_add_task('https://electronics.howstuffworks.com/tv.htm')
www_add_filter('ul','list-none border-b border-primary mb-2 pb-2')
www_add_filter('li','my-2')
www_diver_start('db_six.sqlite')
