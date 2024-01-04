# ChatGPT-Clone

**ChatGPT-Clone** features a layout similar to ChatGPT which provides answer from Bard. User can ask many questions user wants or delete from the database. The data is stored in a database of MongoDB.

**Special Thanks to** [CodeWithHarry (github.com)](https://github.com/CodeWithHarry) and his [video](https://www.youtube.com/watch?v=OAr6AIvH9VY) &

The project uses Flask (Python package), Tailwind CSS, JavaScript and MongoDB for storing data. Docker file has been created of the repo which has been rendered on Render.

Web App is accessible here - [ChatGPT-Clone](https://harshgptclone.onrender.com/)

See demonstration video on Youtube - [Demo Preview](https://youtu.be/ki2X6bPT75w)

(More Updates will be implemented Later)

## Requirements

Make sure that you have both [Node.js](https://nodejs.org/) and [Python](https://www.python.org/) installed on your local machine.
Clone the repository onto your local computer and run:

1. `pip install -r requirements.txt` to install flask packages
2. `npm install` to install npm packages from `package.json`
3. In one terminal run `npm run tailwind` to run Tailwind during development - this will start real time compilation of styles used in your HTML templates
4. In second terminal run `python main.py` to start the Flask development server (debug mode is ON). As you add/remove Tailwind classes in HTML templates, the watcher running in step 3 will automatically regenerate your `app\static\main.css` file which is picked up the flask server running in step 4.

## Setting Up MongoDB Database

1. Create your account in [MongoDB Atlas](https://www.mongodb.com/atlas/database)
2. Click on **+ Create** to create a database
3. After Database is created, on the database dashboard, click on **Connect** and select **Compass** option.
4. Copy the connection string and replace it in the `main.py` file where `app.config["MONGO_URI"]` is present.
5. If your collection name is different aur database is different, configure it accordingly in the connection string and in the `collection` variable in the `main.py` file.
