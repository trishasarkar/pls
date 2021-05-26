# pls

### Documentation

1. home is the main app
2. Static in the main repository has been used to gather static files while hosting
3. Db is IBM cloudant. npm json bin has been used for data. get_data() function in home/views.py gets the questions and options data from npm api.
4. choose_category() in home/views.py return the html code for the choose category page. This code will be attached to the global template and gets rendered.
5. Input checkboxes for each category of data available must be created here. for ex: if we have to add 2 new categories, we need to add 2 new input fields with the category names here.
6.  Similarly scene dictionary in get_scene() (in 'home/views.py') must be added for every category to be added/modified.
7. quiz function in 'home/views.py' asks to chose category and shows the screen of the first scenario.
8. quiz2 is the main loader for the quiz part. all questions and options are displayed from this view.
9. by default this view stores the responses of previous question AND gets the session info of scenario.no and question.no and shows the next scenario/questions
10. if there is some 'action' (jump section/exit), then it takes actions accordingly
11.
