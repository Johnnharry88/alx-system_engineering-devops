# A puppet a line in a server file

$file_to_edit = '/var/www/html/wp-settings.php'

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_toOedit}"
  path	  => ['/bin','/usr/bin']
}
