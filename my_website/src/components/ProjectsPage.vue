<template>
    <div class="py-4">
        <h1 class="text-4xl font-bold text-center mb-8">Keegan's Projects</h1>
        <p class="text-center">Below is a list of projects I have worked on. If you would like a live demo of any of these projects, please reach out to me.</p>
        <div class="space-y-8">
        <ProjectItem
            title="This Website"
            summary="<p>This website was built using Vue.js, Tailwind CSS, Python, Flask, and DynamoDB. It showcases my progress as a software developer</p>
            <p>This website was deployed with AWS and github Actions</p><br>"
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
        </div>
    </div>
  </template>
  
  <script setup>
  import ProjectItem from './ProjectItem.vue';
  </script>