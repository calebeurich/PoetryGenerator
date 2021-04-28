# PoetryGenerator

This system is called Dr. Thug. 

It takes a text version of the cat in the hat by dr seuss and extracts syntax trees based on the lines in the book. The system also uses lyrics from 200 young Thug songs and a bag of words approach within a syntax token keyed dictionary to pick NUM_LINES lines of dr seuss syntax and replace the words in those lines with syntactically identical young thug words as used in his lyrics. The system then generates NUM_POEMS poems and grades them all on sentiment with the nltk evaluator and selects the poem with the highest score to preform. Poems are saved to examples.txt within the generated_poems folder. I always thought Young Thug had some of the funniest and most randomly poetic lyrics of any artist so I thought t would be funny to combine that lyricism with the typical format of a poetry style book for children in The Cat In The Hat. 


This system can be run by simply running executor.py with no system arguments.


This project definitely challenged me as a computer scientist. First, I spent a lot of time abstractly learning. I have no done much academic research before, so looking at academic papers to get ideas and insight was initially challenging. There were so many great ideas that I had no idea what to do with realistically. This forced me to get better at finding realistic take aways from larger cool projects. Admittedly, I could have done a better job implementing more of these cool features I thought about, but it was much harder than expeceted to get any functional system off the ground in the first place. Next, I was challenged by working with more confusing packages and data structures. I am used to generally creating my own data structures and understanding most of the functions in my code. This this project I had to use a lot of new libraries like NLTK which an ocean of features and documentation. I was constantly looking things up in documentation and on the internet in an attempt to understand the tools I was using and their potential. This was specifically hard when working with syntax trees and having to store them with pickle in order to not have large runtimes. The workflow between files also forced me to be more efficient in my seperate file usage so that my running code was much closer to all that it actually needed to be. In general my orginazation, planning, and problem solving skills were all challenged during this project which I view as fundamental aspects of being a computer scientist. I had very big dreams with such a cool concept and it took all my effort to make something that would actually work instead of chasing impossible concepts, so I am just glad that I was able to set more realistic goals in the end. Overall I found this project very difficult for a variety of reasons, but I learned a lot along the way. 


Inspiring Papers:

1. Hafez: an Interactive Poetry Generation System
Marjan Ghazvininejad, Xing Shi, Jay Priyadarshi, and Kevin Knight


What I gained the most from this paper the style control section. There were great ideas such as a list of curse words which I did not end up implementing, but could have been useful, and an evaluation based on sentiment which I did end up using. Overall the paper made me more thoughful about my implementations and ideas overall even though I did not end up doing a ton of tuning to the poems. 

2. Towards A Computational Model of Poetry Generation
Hisar Maruli Manurung, Graeme Ritchie, Henry Thompson

What I gained the most from this paper was the evaluation section. There were many interesting listed metrics for evaluation. Phonetics and semantics were the two aspects I really wanted to add into the evaluation but was unable to incorporate. If I were to improve this system, I think the first place I would go would be to implement these evaluation metrics and potentially utelize these concepts more in the generation as well. 

3. Full-FACE Poetry Generation
Simon Colton, Jacob Goodwin and Tony Veale

This was the paper that most inspired my system. The idea of corpus based generation was very useful and gave me the though to use a new corpus in the form of an old corpus. From this I used the Dr. Seuss syntax for the Young Thug words. My process was no where near as complicated, but it was helpful to read how they processed inputs in order to access the desired factors. 