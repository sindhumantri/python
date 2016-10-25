>>> import os

>>> os.getcwd()
'/home/test/programming'

>>> os.chdir('/home/test')

>>> os.getcwd()
'/home/test'

>>> os.listdir('/home/test')
['.ssh', 'icmp-redirect.pkt', '.mysql_history', '.bashrc', 'process.txt', 'portscan.cap', '.cache', 'udp-traceroute.cap', '.vim', 'calndr.pdf', 'ftp-getfile.pkt', '.sudo_as_admin_successful', '.viminfo', '.profile', 'document2', 'ftp-getfile.cap', 'python_socket', '.local', '.bash_history', '.lesshst', 'test.py', 'sindhu_file', 'doc.txt', '.bash_logout', 'my-script.sh', 'command.awk', 'programming', '__pycache__']

>>> os.mkdir('os_demo')

>>> os.makedirs('os_demo_2/os_demo_1')

>>> os.rmdir('os_demo')

>>> os.removedirs('os_demo_2/os_demo_1')

>>> os.rename('test.py', 'test_demo.py')

>>> os.stat('test_demo.py')
posix.stat_result(st_mode=33204, st_ino=137162, st_dev=64512, st_nlink=1, st_uid=1000, st_gid=1000, st_size=97, st_atime=1476599249, st_mtime=1472079376, st_ctime=1477354355)

>>> file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
>>> file_path
'/home/test/test.txt'

>>> print(os.path.split('/tmp/test.txt'))
('/tmp', 'test.txt')

>>> print(os.path.exists('/tmp/test.txt'))
False
>>> print(os.path.isfile('/tmp/test.txt'))
False
>>> print(os.path.basename('/tmp/test.txt'))
test.txt
>>> print(os.path.dirname('/tmp/test.txt'))
/tmp

>>> print(os.path.splitext('/tmp/test.txt'))
('/tmp/test', '.txt')
