# project-a-29
Welcome to What's Changed! 

What's Changed is a web application that allows signed-in users to submit changes to any locations due to COVID. It detects the user's location on the map, shows COVID rating for each place, and contains the updated information of a place by users. 

Please follow the link to the app's online platform:
https://whats-changed-cville.herokuapp.com/


Features to Discover:
1. Header: By clicking options shown on the header, What's Changed's will redirect you to the correct page.
2. Login Feature: You can log in with a personal Google account, as well as "@virginia.edu". What's Changed will record your email and username.
3. Map: Your current location will shown on the map. 
   Here are several things you can do on this page: 
      (1)You can switch between the “Map” setting and “Satellite” settings in the top left corner of the map. There should be a difference in the display of the background screen, “Satellite” will be actual pictures of the Earth from space. 
      (2) Clicking the button in the top left of the map API that reads “Pan to Current Location” will relocate your location to the correct position on the map. 
      (3) You may use search bar to search for places such as "bagels". 
      (4) After clicking on the marker for Roots, you should see an ‘Info Card’ on which there are the labels: Rating, Price Level, Address, and Website. Following those labels, there should be a green button labeled as “See Changes” and/or a blue button labeled as “Submit Changes.” If other users have submitted changes to a certain place, you should be expecting both buttons. Otherwise, only the “Submit Changes" button would show up. 
4. See Changes: All changed submitted by users will be displayed on this page in a chronological order. You may click on a place to view/submit changes for this specific location. Once you are redirected to view all changes (including submitted time and Covid-Rating) of a specific location, you can then submit a new change if needed. However, only signed-in users are allowed to submit a change. Unauthenticated users will be redirected back to the login page. For requesting a change, you can fill out the form by answering questions on Change Request. If the form is submitted successfully, then new changes will be shown in the list of changes. Additionally, a user can click on a change that has been made for a specific place and submit a comment on that change. By clicking on the change, one will be redirected to a page listing the comments that have been made on that change. Only users that are logged in can submit changes; those that are unauthenticated will be redirected to the login page. This feature is designed for users to comment about the changes that have occurred at a certain place or ask for clarifications on the submitted changes.
5. Leaderboard: What's Changed will rank all users by number of changes they contribute to the app. In addition, the number of changes will be displayed next to each user's username.
7. Logout: This feature will log out an user and redirect him to the login page.

Please play around with this app. Hopefully you will enjoy it!

![whatschange](https://user-images.githubusercontent.com/61603017/117171512-ed221480-ad98-11eb-9467-1d1ded20a324.png)
