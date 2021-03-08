# branches_app

1. Given project is a singlepaged web app, which provide an ability to manage database of two tables: branches and employees. 
2. There implemented authorization/regisrtration system. Users, according to their roles, have different permissions to format database (in particular, there are two roles of users: CEOs and TeamLeads, only CEOs can format definite fields of branches table).
3. In addition there implemented AWS S3 storage for media fies and Googlemaps API for matching branches location (for correct work you should add your AWS credentials in settings.py).
4. Web app uses PostgreSQL as default database (please put the correct PostgreSQL credentials in settings.py).
5. Django migrations will add in database initial data (10 default branches and 10 000 employees, generator is located in directory '/objectsgenerator').
6. REST API is capable to find clothest branch for matching coordinates 
( e.g. https://localhost/api/v1/branches/lat=...&lng=...).
