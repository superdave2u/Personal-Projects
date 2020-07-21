<?php

// plaintext xor cyphertext = key

function xor_encrypt($in) {
    $key = 'qw8J';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

function loadData($def, $inCookie) {
//    global $_COOKIE;
    $mydata = $def;
    if(array_key_exists("data", $inCookie)) {
      $tempdata = json_decode(xor_encrypt(base64_decode($inCookie["data"])), true);
      if(is_array($tempdata) && array_key_exists("showpassword", $tempdata) && array_key_exists("bgcolor", $tempdata)) {
          if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {
          $mydata['showpassword'] = $tempdata['showpassword'];
          $mydata['bgcolor'] = $tempdata['bgcolor'];
          }
      }
    }
    return $mydata;
}

function saveData($d) {
    setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
}

$override = array(
  'showpassword' => 'yes',
  'bgcolor' => '#ffffff'
);

echo print_r(base64_encode(xor_encrypt(json_encode($override))),1);
