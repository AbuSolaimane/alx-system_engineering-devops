# install flask using pip3
package { 'flask':
  provider => 'pip3',
  ensure   => '2.1.0'
}
