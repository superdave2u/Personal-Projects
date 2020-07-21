<?php
$imgPath = 'jack_russell.png';

$pict = fopen($imgPath, "r") or die("Unable to open file!");



  function is_jpeg(&$pict)
  {
    return (bin2hex($pict[0]) == 'ff' && bin2hex($pict[1]) == 'd8');
  }

  function is_png(&$pict)
  {
    return (bin2hex($pict[0]) == '89' && $pict[1] == 'P' && $pict[2] == 'N' && $pict[3] == 'G');
  }
  function is_imageType(&$pict){
    return (exif_imagetype($pict));
  }

$fileContents = fread($pict,filesize($imgPath));
if(is_jpeg($fileContents)){
  echo "File is jpeg\n";
}elseif(is_png($fileContents)){
  echo "File is png\n";
}else{
  echo "File is not jpeg/png\n";
};

echo exif_imagetype($imgPath);
fclose($pict);
?>
