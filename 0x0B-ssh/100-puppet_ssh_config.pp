# a Puppet Script to change ssh config file(/etc/ssh/ssh_config)
# in the server

file_line { 'forbid passwd auth':
  path   => '/etc/ssh/ssh_config',
  ensure => 'present',
  line   => '    PasswordAuthentication no',
}

file_line { 'change file to identify':
  path   => '/etc/ssh/ssh_config',
  ensure => 'present',
  line   => '    IdentityFile ~/.ssh/school',
}
