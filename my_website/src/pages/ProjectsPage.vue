<template>
    <div class="py-4">
        <h1 class="text-4xl font-bold text-center mb-8">Keegan's Projects</h1>
        <p class="text-center ">Below is a list of projects I have worked on. If you would like a live demo of any of these projects, or if you would like to collaborate, please reach out to me.</p>
        <br>
        <div class="space-y-8">
        <ProjectItem
            title="This Website"
            summary="<p>This website was built using Vue.js, Tailwind CSS, Python, Flask, and DynamoDB. I use this website to showcase my progress as a software developer.</p>
            <p>This website was deployed with AWS and github actions</p><br>"
            image1=""
            image2=""
            source="https://github.com/keeganasmith/personal-website"
            start="5/16/2024"
        />
        <ProjectItem 
            title="Crash Test Predictor"
            summary="<p>This web application predicted the safety rating of a vehicle based on criteria such as the size of the vehicle and the roll stability factor of the vehicle.
                The predictions were made using an XGBoost model. This model was trained on a thousand crash test records from the NHTSA.</p>
                <p>The application was created with Vue.js, Python, and Flask. The application was deployed with Render and github actions, although it is not currently deployed.</p>
                <p>This was a group project at a hackathon, however I did the lionshare of the work on both the frontend and backend as proven by the commit history.</p><br>"
            image1="crash-1.png"
            image2="crash-2.png"
            source ="https://github.com/keeganasmith/TidalHack2024"
            start="2/24/2024"
        />
        <ProjectItem 
            title="Phishing Email Detector"
            summary="<p>This web application scanned a user's email inbox for fraudulent emails. Users would login to their google account and we would grab the first 20 emails in their inbox. Users could analyze emails by clicking on one of their emails.</p>
            <p>We determined the threat severity of an email by looking through the email for malicious links, determining the validity of the email address of the sender, and by passing the email through openai's chatgpt api.</p>
            <p>This project was done at a hackathon, I was responsible for setting up the flask api and creating the endpoint for fetching user emails, which included putting the emails into a readable format.</p>"
            image1="phish-1.png"
            image2=""
            source="https://github.com/keeganasmith/tamuhack2024"
            start="1/27/2024"
        />
        <ProjectItem
            title="Learnalytics"
            summary="<p>This web application predicted the outcome of a student given certain characteristics. Predictions were made by an XGBoost model. Only 600 records were used for training.</p>
                <p>I was responsible for training the model and for creating the web api. Both tasks were accomplished with python, the api was built with the flask framework.</p>"
            image1="Learn-1.png"
            image2="Learn-2.png"
            source="https://github.com/GigaSmurf/TidalHackathon2023"
            start="11/11/2023"
        />            
        <ProjectItem
            title="Block TD"
            summary="<p>This was a 2d tower defense game built only with pygame. This game was built for the Capsher 2023 coding challenge, in which my team placed third.</p>
            <p>I designed and programmed the different towers and their projectiles and handled projectile collisions with enemies. I also programmed and designed the different rounds and enemies/enemy types.</p>"
            image1="block-1.png"
            image2="block-2.png"
            source="https://github.com/keeganasmith/CapsherCodingChallenge2023"
            start="3/21/2023"
        />
        <ProjectItem
            title="Portfolio Risk/Yield"
            summary='<p>Picture unavailable: since the creation of this app, it appears the api ninja endpoint for American FED interest rates is broken. If you want to see this project up and running again, please let me know.</p><p>This desktop application aimed to predict the risk and yield of a portfolio based on metrics such as a portfolio`s sharpe ratio.</p>
            <p>I was responsible for the backend: pulling and sanitizing stock and bond data from various apis and calculating the sharpe ratio for a given portfolio.</p>
            <p>Devpost submission here: <a href="https://devpost.com/software/joe-s-portfolio-risk-analysis">https://devpost.com/software/joe-s-portfolio-risk-analysis</a></p>'
            image1=""
            image2=""
            source="https://github.com/keeganasmith/TAMUHack2023"
            start="1/28/2023"
        />
        </div>
        
    </div>
  </template>
  
  <script setup>
  import ProjectItem from '../components/ProjectItem.vue';
  </script>