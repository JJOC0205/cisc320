Solution:
My program uses a python Dataclass in order to store all the data about the student that we will be using. It has lowest_page, latest_page, tot_score(total score), and num_subs(number of submissions) as it fields. I built a helper function that is used to mutate the class that I created. It first takes in the string from the input list, it breaks it into a list with the split method. If the action code is 'P', it then checks if the current page is a lower number than the lowest field. It then updates the latest_page as well. If instead it was a 'S', it add the score to the tot_score, and increments the num_subs by 1. It does all of these to an instance that was brought in as parameter.
The main calc_logs fucntion uses a for loop from 1 to the number given by line 1 in the input + 1, I use this to split the string taken from input into a list, and then take the first element(student id number) and use that as a key in a dictionary. If the key doesnt already exist, I create a new instance of the student class, otherwise i call my mutate_student function with the string and the instance associate with my key. After this I use Python's built in sort function to sort by the latest_page number, and then turn the output of that, which is a list, back into a dictionary. In order to output my dictionary, I use another for loop. Which uses keys and value as the incrementor, and my dictionary's items as the place to pull data from. I then check if it has both sumbissions and pages visited, if it does i then print all my values, and divide the total by the number of submissions in line.

Time Complexity:
This function runs in worst case O(n*log(n) + L), where L is the number of lines read from input. This is due to using pythons built in sort function. For all time complexities, the dominant term(highest power for example) is the one we care about most. In this case, thay is the sort functions, O(nlog(n)). While I use for loops, with a time of O(n), this is obviously overshadowed by O(nlog(n)). And while that is the dominant term, it is also important to include the input complexity, which as it has to read L number of lines, is L. This is linear time and for our sakes we will add it to the O(nlog(n)) for a more accurate complexity