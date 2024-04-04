# Using Puppet to create a custom HTTP headder response

exec {'update':
  command => '/usr/bin/apt-get update',
}
-> package {'nginx':
  ensure => 'present',
  match => 'http {',
  line  => 'htp {\n\tadd_header X-Served-By \$HOSTNAME}\";",
}
-> exec {'run':
  command => '/usr/sbin/service nginx restart',
}
