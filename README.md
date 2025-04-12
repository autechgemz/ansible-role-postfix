# Ansible Role: postfix

## Description

Manage the postfix configuration and service.

This role installs, configures, and manages the Postfix. It supports both RedHat and Debian-based distributions and allows for extensive customization of postfix's configuration.

## Requirements

- Ansible 2.9 or higher

## Dependencies

None

## OS Platforms

- RedHat family
- Debian family

## Example Playbook

```yaml
- hosts: all
  roles:
    - postfix
```

## Role Variables

### postfix_package_ensure: (string)

Defines the desired state of the postfix package.

```yaml
postfix_package_ensure: 'present'
```

### postfix_service_ensure: (string)

Defines the desired state of the postfix service.

```yaml
postfix_service_ensure: 'started'
```

### postfix_service_enable: (bool)

Specifies whether the postfix service should be enabled at boot.

```yaml
postfix_service_enable: true
```

### postfix_master_config_options: (dict)

Custom options for the postfix master.cf configuration.

```yaml
postfix_master_config_options:
  - name: smtp
    enabled: false
```

### postfix_main_config_options: (dict)

Custom options for the postfix main configuration.

```yaml
postfix_main_config_options:
  inet_protocols: 'ipv4'
  myhostname: 'mta01.example.com'
  myorigin: 'mta01.example.com'
  mydomain: 'example.com'
  mynetworks: '127.0.0.0/8 192.168.56.0/24'
  mynetworks_style: 'subnet'
  minimal_backoff_time: '5m'
  maximal_backoff_time: '5m'
  maximal_queue_lifetime: '60m'
  bounce_queue_lifetime: '0'
```

## Example vars

```yaml
postfix_package_ensure: 'present'
postfix_service_ensure: 'started'
postfix_service_enable: true

postfix_master_config_options:
  - name: smtp
    type: inet
    command: smtpd
    enabled: false

postfix_main_config_options:
  inet_protocols: 'ipv4'
  myhostname: 'mta01.example.com'
  myorigin: 'mta01.example.com'
  mydomain: 'example.com'
  mynetworks: '127.0.0.0/8 192.168.56.0/24'
  mynetworks_style: 'subnet'
  minimal_backoff_time: '5m'
  maximal_backoff_time: '5m'
  maximal_queue_lifetime: '60m'
  bounce_queue_lifetime: '0'
```

## TODO

- Manage /etc/postfix/header_checks
- Manage /etc/postfix/virtual
- Manage /etc/postfix/canonical

## License

This role is under the MIT License. See the LICENSE file for the full license text.

