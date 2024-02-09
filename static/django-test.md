## Task


You are tasked with creating an django application which is designed to take a scrambled word as input and provide a list of possible words that are equal or lesser than the length of given word.


## Requirements


* The application should accept a single scrambled word as input max 15 length.
The input should be case-insensitive and may contain spaces or special characters.


* Implement a function to unscramble words.
The function should take a scrambled word and return a list of unscrambled words.


* consider '?' as wiled characher, system should handled max 3 wild charachters.
eg: given input: a?ple, in place of '?' can be any charachter.


* Create a Django view to handle the search functionality.
Use AJAX or a form submission to send the scrambled word to the server.
Display the unscrambled words in the response.


* Create an HTML template with a form for user input.
Use JavaScript for form validation and asynchronous communication with the server.


* For UI Show the input field for the scrambled word.
Display the unscrambled words below the input field.


* Scrambled Word Constraints:
Validate that the input is a valid word (exists in the dictionary).
Ensure the scrambled word has a maximum length of 15 characters.
Allow a maximum of 3 wildcard characters in the scrambled word.


* You will be shared with the word list:
Populate the database with a dictionary of words.
Use this dictionary to check the validity of the unscrambled words.


* Feel free to modify or extend this test based on your specific requirements and the skills you want to evaluate.


### Reference
You can check unscramblex.com for reference.


### Bonus

* Write unit tests for the unscrambler function.


## Submission Notes


* Code Compilation instructions for the IDE/Plugin expected, dependency management, etc

* Short description explaining architecture (e.g View, ViewModel...)

* Any 3rd party libraries used and rational

* Explain what each test does in comments or in a document format

* Explain any additional features covered - apart the requirements given above

* Please either share your repository (public repo preferred) or use a service like Dropbox to share the file.



## How we evaluate

We want you to succeed! We aim to evaluate each submission with the same criteria, they are:

 * *requirements* you've build the right product, attention to details!

 * *code style* idiomatic, safe, clean, concise.

 * *unit tests* coverage, stable, reliable, maintainable, mocked where required

 * *user experience* responsive, user-centric design.