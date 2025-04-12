
def test_system_type(host):
    assert host.system_info.type == "linux"

def test_system_dist(host):
    assert host.system_info.distribution in ["ubuntu", "debian", "redhat", "centos", "rocky"]
    assert host.system_info.arch == 'x86_64'

def test_user(host):
    assert host.user("postfix").exists

def test_postfix_config(host):
    postfix_config = host.file("/etc/postfix/master.cf")
    assert postfix_config.user == "root"
    assert postfix_config.group == "root"
    assert postfix_config.mode == 0o644

def test_postfix_config(host):
    postfix_config = host.file("/etc/postfix/main.cf")
    assert postfix_config.user == "root"
    assert postfix_config.group == "root"
    assert postfix_config.mode == 0o644

def test_postfix_installed(host):
    postfix = host.package("postfix")
    assert postfix.is_installed

def test_postfix_running_and_enabled(host):
    postfix = host.service("postfix")
    assert postfix.is_running
    assert postfix.is_enabled

def test_postfix_tcp_socket(host):
    postfix_tcp_v4 = host.socket("tcp://25")
    postfix_tcp_v6 = host.socket("tcp://:::25")
    assert postfix_tcp_v4.is_listening
    assert postfix_tcp_v6.is_listening
