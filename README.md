**Codechella Crisis Response App Spec V1**

**Internal Definitions**

1. **Crisis:** A period of immense difficulty or danger (i.e Social unrest, natural disasters, conflict zones, Food deserts, High senior citizen density, High poverty rates, Shootings and terrorist attacks)
2. **Verified Crisis:** A crisis that is internally recognized in our system -\&gt; might not need this

**Product description**

An application curated to crisis zones to facilitate dissemination of mission critical information from source to key partners with minimal lag time.

1. Web Application

a) For citizens - curate and display information with degree of confidence in validity **(tackle misinformation)**

b) For responders - cluster and aggregate relevant information that can help responders deal with situations using up to date info, visualize data

1. Text Notifications **(secondary focus)** - Text important updates to users who opt in

**Value proposition #Hackforgood (lets define our MVP)**

Helping individuals get access to accurate information from sources on the ground with little to no lag time.

**MVP questions (IMPORTANT !!!!)**

_ **How will a user using the app get info specific to their location?** _

Do they have to enter location or can we use browser to get their location and backend logic to determine if there is a crisis? -\&gt; we may be able to simplify this by just using categories to search by at all times instead of maintaining current crises

We should give a user predefined categories to select from to get tweets i.e **help, aid, food**

 **How do we know what regions to run our program in and when?** 
 
How do we know what regions have an ongoing crisis? -\&gt; can simplify as mentioned above

 **How will our app find a crisis zone and start displaying information?** 

If a &quot;verified&quot; crisis we display info otherwise display null? -\&gt; we may be able to simplify this by just using categories to search by at all times (i.e help, food, resources, aid) instead of maintaining a list of current crises

**Use case examples**

1. I am in a small town and there is a natural disaster near me and I need to immediately know if there are people near me I can help or aid resources close to me.

2. I am a first responder in a civil war and I want to use the data visualisation to see where there are clusters of affected people so I can deploy my resources best.

3. I am a senior citizen living in a food desert and don&#39;t have immediate access to people near me. I want to find the closest grocery store, restaurant or facility offering free food for the homeless or elderly.

**Key features**

1. [Embed filtered relevant tweets in the web page](https://developer.twitter.com/en/products/twitter-for-websites) tweet IDs will have to be retrieved from the backend using a GET request to our API **Frontend Team**

2. Display data visualization and relevant information to first responders **Frontend &amp; Data Team**

1. Give all users filter tweet clusters by keyword same as end user but responders get data visualisation e.g. help, hurt, injured (When a user clicks a category we send a GET request to our backend) **Frontend Team**

2. Confidence score in the validity of a tweet. Using internal logic how accurate do we believe a tweet is **Backend/Data Team**

3. Internal API for frontend team to use **Backend/Data Team**

4. Texts [Twilio](https://www.twilio.com/)**(last priority)** - the only way to send a text using the API is if a user initiates the action as we don&#39;t have access to that data so we would need someone to either sign up for the notification in the app or tweet at us etc. Tech heavy - save for last


**Moonshot features**

1. Link to other resources in the area i.e locally owned businesses etc.

**Deliverables (per person)**

Front end:

1. React web app - Nandini and Luisa
  1. Home page:
    1. Responders section, same information of citizens but with data visualization.
    2. Citizens sections.
    3. Deployment (discuss with backend team)

Backend

1. Tweet filtration - pull the right relevant tweets from the API and store them
2. Misinformation Logic - confidence score for tweet validity
3. API for frontend
4. Tweet Database

**Product roadmap/timeline**

**First review** _**20th (11pm EST) (10pm CT) (8pm PST)**_ _ **:** _

1. Misinformation logic and tweet storage database first rev - **Gobind**

2. Tweet filtration/streaming and internal API for frontend first rev - **Gobind**

3. Web app mockup &amp; skeleton
 (answer questions about database, hosting and full stack linking to our endpoints - we need to discuss how you want to receive data and what data you want to receive i.e the ID of a tweet for you to fetch to embed on the page) - **Luisa**

**Second review** _**21st (2pm EST) (1pm CT) (11am PST)**__ **:** _

1. Misinformation logic and tweet storage database complete Data Visualization - **Gobind**

2. Tweet filtration/streaming and internal API for frontend complete - **Gobind**

3. Webpage functional &amp; start tying into backend - **Frontend Team**

**Final review** _**21st (11pm EST) (10pm CT) (8pm PST)**__ **:** _

1. Fully functional application with Backend and Frontend Tied into each other and us as users doing testing. **Gobind**
2. Video for submission purposes

**Devpost Submission 22nd (9am EST) (8am CT) (6am PST)**

**API Usage:**

&quot; **cd** react-flask-app&quot;

(using two terminal windows)

In the first: &quot; **yarn** start&quot; (frontend server)

In the second: &quot; **yarn** start-api&quot; (backend server both served on post localhost:5000)
