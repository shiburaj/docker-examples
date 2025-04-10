<?php

// Check if the correct number of arguments were provided
// $argv[0] is the script name itself
// $argv[1] should be the first number
// $argv[2] should be the second number
if ($argc != 3) {
    echo "Usage: php add.php <number1> <number2>\n";
    exit(1); // Exit with an error code
}

// Get the arguments from the command line
$number1_str = $argv[1];
$number2_str = $argv[2];

// Validate if the inputs are numeric
if (!is_numeric($number1_str) || !is_numeric($number2_str)) {
    echo "Error: Both arguments must be numeric.\n";
    exit(1); // Exit with an error code
}

// Convert arguments to numbers (e.g., float for decimals or int for whole numbers)
$number1 = (float)$number1_str; // Use float to handle decimals
$number2 = (float)$number2_str;

// Add the numbers
$sum = $number1 + $number2;

// Display the result
echo "The sum of " . $number1 . " and " . $number2 . " is: " . $sum . "\n"; // Add newline for cleaner CLI output

?>
