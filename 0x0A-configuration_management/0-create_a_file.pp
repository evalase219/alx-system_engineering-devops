# create a file in /tmp

file { '/tmp/school':
  ensure  =>  file,
  content =>  'I Love Puppet',
  mode    =>  '0744',
  owner   =>  'www-data',
  group   =>  'www-data',
}
