<?php

// Hey admin, I have deleted these data, remember to erase the remainings


function checkUserSession() {

    $encoded_data = $_COOKIE['UserSession'] ?? '';

    if ($encoded_data) {
       
        $decoded_data = base64_decode($encoded_data);
        $user_data = unserialize($decoded_data);

        // Check if the unserialized data is valid
        if (is_array($user_data) && isset($user_data['name'], $user_data['password'])) {
            $username = $user_data['name'];
            $password = $user_data['password'];

            // erasing the password
            if ($username == 'administrator' && $password == '....') {
                
                $_SESSION['flash'] = 'zeroday{fake_flag}'; // erasing flag
                header('Location: /flag');
                exit;
            } else {
              
                $_SESSION['flash'] = '.....';
            }
        } else {
            $_SESSION['flash'] = '.....';
        }
    } else {
        $_SESSION['flash'] = '.......';
    }
}

checkUserSession();

header('Location: /login.php');
exit;


// Ok, I have erased a lot
