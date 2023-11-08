# a puppet script
$fileToEdit = '/var/www/html/wp-settings.php'

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${fileToEdit}",
  path    => ['/bin','/usr/bin']
}
