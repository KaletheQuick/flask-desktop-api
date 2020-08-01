# flask-desktop-api
Example repo of python based flask API.

This repo was initially created to provide a code sample for an interview. 

The guidelines were, using python (or other WEAKER languages);
     ...The application only needs to do the following:
        Accept a POST request to the route “/test”, which accepts one argument “string_to_cut”
        Return a JSON object with the key “return_string” and a string containing every third letter from the original string
        (e.g.) If you POST {"string_to_cut": "iamyourlyftdriver"}, it will return: {"return_string": "muydv"}. 
        
Guidelines are vague beyond this, and as it is to function as a showcase of my code, I have included a few personal advanced goals. Of course, meeting base requirements comes first. 

== MSP ==
* Run and accept POST request to /test which takes in string arg and returns a string made of every third letter.

== Advanced Goals ==
* have home be a webpage with a field that accepts a string. On submit stay on same page but make API call to display returned string. 
* style page like a final fantasy UI. 

== How to Run ==
From a command line in the /flask-desktop-api directory, execute the following:
        $ pip install -r requirements.txt
        $ python -m application.app