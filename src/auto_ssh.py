import os, sys, paramiko
from getpass import getpass
paramiko.util.log_to_file('auto_ssh.log', 0)
def parse_user(user, default_host, default_port):
	if '@' not in user:
		return user, default_host, deafult_port
	user, host = user.split('@', 1)
	if ':' in host:
		host, port = host.split(':', 1)
	else:
		port = default_port
	return user, host, int(port)
def autoSsh(users, cmds, host='localhost', port=22, timeout=6.0,
		maxsize=2000, passwords = None):

	user_tuples = []
	if passwords is None:
		passwords = {}
	for user in users:
		user, ht, pt = parse_user(user, host, port)
		user_tuples.append((user, ht, pt))
		if user not in passwords:
			passwords[user] = getpass("Enter user '%s' password: " % user)
	for usertuple in user_tuples:
		user, host, port = usertuple
	try:
		transport = paramiko.Transport((host, port))
		transport.connect(username=user, password=passwords[user])
		channel = transport.open_session( )
		if timeout: channel.settimeout(timeout)
		for cmd in cmd_list:
			channel.exec_command(cmd)
			response = channel.recv(maxsize)
			print 'CMD %r(%r) -> %s' % (cmd, user, response)
	except Exception, err:
		print "ERR: unable to process %r: %s" % (user, err)
		raise

if __name__ == '__main__':
	logname = os.environ.get("LOGNAME", os.environ.get("USERNAME"))
	host = 'localhost'
	port = 22
	usage = """
usage : %s [-h host] [-p port] [-f cmdfile] [-c "command"] user1 user2...
	-c command
	-f command file
	-h default hos (default: localhost)
	-p default port (default: 22)
Example: %s -c "echo $HOME" %s
same as: %s -c "echo $HOME" %s@localhost:22
""" % (sys.argv[0], sys.argv[0], logname, sys.argv[0], logname)
	import getopt
	optlist, user_list = getopt.getopt(sys.argv[1:],'c:f:h:p:')
	if not user_list:
		print usage
		sys.exit(1)
	cmd_list = []
	for opt, optarg in optlist:
		if opt == '-f':
			for r in open(optarg, 'rU'):
				if r.rstrip( ):
					cmd_list.append(r)
				elif opt == '-c':
					command = optag
					if command[0] == '"' and command[-1] == '"':
						command = command[1:-1]
					cmd_list.append(command)
				elif opt == '-h':
					host = optag
				elif opt == '-p':
					port = optarg
				else:
					print 'unknown option %r' % opt
					print usage
					sys.exit(1)
				autoSsh(user_list, cmd_list, host=host, port=port)
