# Interview

Complete the following challenge in a language of your choice.  Once your work is done, create a Pull Request(PR) to the `Main` branch.
We will respond to your PR with questions in comments on the PR. Respond to all the questions to complete the challenge.

Create a REST API using any language or web framework you prefer, which performs the following functionality:

1. Provides a POST endpoint at /data where a client can submit a JSON list of 500 random numbers. The list must be validated to be exactly 500 numbers, if there are more or less than 500 an error must be returned to the client. Similarly, if something other than a list of numbers is submitted, an error must be returned.
    
2. Provides a GET endpoint at /data which returns the same JSON formatted list of 500 numbers that were submitted with the first task above, which are now sorted from lowest to highest.

BONUS:

- Provides a PATCH endpoint at /data which allows insertion of a single number into the list which gets placed in the proper order maintaining the 500 number limit. The largest number is removed from the list to keep the 500 number limit.

Questions you may have:

1. What is a valid number?  
- Any decimal number that is not scientific notation.  Trim non-sig figures and empty spaces.
2. How should I store the numbers?
- Do everything in memory for this implementation, don't use an external database.  Your code should compile/run if we want to run it ourselves without any external databases or tools.
