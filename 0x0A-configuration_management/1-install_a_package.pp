# install flask using pip3
package { 'Flask':
  provider => 'pip3',
  ensure   => '2.1.0'
}
