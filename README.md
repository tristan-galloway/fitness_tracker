# Overview

Currently I decided to switch from working on learning languages to learning an important part of coding, syncing my projects with databases. So this project will be less focused on using the language as much as it will be focused on connected to a cloud database to store and retrieve values for a user. Specifically this app will allow users to record basic workouts like running, bicycling, and swimming events.

[Software Demo Video]()

# Cloud Database

I am using Google Firebsase Firestore to store all of the data collected from the user. There is one collection that has a document for each event. Each event is converted to a dictionary to be stored, and converted back to a string to be displayed to the user. 

# Development Environment

**Visual Studio Code:** 1.91.1
**Python:** 3.12.4

# Useful Websites

- [Intro to firebase](https://firebase.google.com/docs/database/?authuser=0&hl=en)
- [Python Functions](https://www.freecodecamp.org/news/python-functions-define-and-call-a-function/)
- [Classes in python](https://www.w3schools.com/python/python_classes.asp)
- [Encapsulation](https://www.geeksforgeeks.org/encapsulation-in-python/)
- [Poplymorphism](https://www.w3schools.com/python/python_polymorphism.asp)
- [Hanling data in Firestore Database](https://www.youtube.com/watch?v=-jWD-vIyirw)

# Future Work

- **FIX WARNING IN get_all_events FUNCTION**
- Add quantifiers to objects for distance and duration
- Add better feedback for the user when items are successfully created or removed.
- Use the object in the push_event() rather then parting it out prior.
- Add the ability to calculate missing values in workouts, like using the speed and duration to figure out the distance traveled.
- Allow users to enter an email and password to sync their data with.
- Allows users to view a summary of the combined stats from each category of event