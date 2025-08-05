<template>
    <h1 class="text-4xl font-bold text-center mb-8">Work Experience</h1>
    <div class="space-y-8">
    <WorkItem 
        title="Digital Innovation Intern"
        company="The Coca-Cola Company"
        summary="<p>As a digital innovation intern at the Coca-Cola company, I designed and implemented an algorithm for determining bundle promotions for specific retailers.</p>
        <br>
        Essentially, I would segment the retailers based on location, volume, and channel. For each segment, I would calculate the average number of SKUs (stock keeping units, think unique items 2L sprite, 12 pack of 12 oz coca-cola, etc.) for each development set. Where a development set is a category of items that fulfill a similar purpose. For instance a development set might be called energy drinks, and it contains single and multi serve drinks under the monster or reign brands.</p>
        <br>
        <p>If a retailer is selling below the average number of skus for the development set, they are lacking in assortment, and thus a bundle discount with items in that development set should be offered.</p>
        <br>
        <p>If a retailer is selling above the average number of skus for the development set, they need to focus on selling more of their best selling items in that development set. Thus a discount on their top selling items within the development set is offered.</p>
        <br>
        <p>If a retailer is selling nothing in the development set, then an aggressive development discount on the top selling items overall within the development set is offered.</p>
        <br>
        <p>I implemented this algorithm in Python with real customer data, and I also created a web GUI for it. The web GUI used vue.js, much like the website you are currently looking at.
        "
        start="6/3/2024"
        end="8/2/2024"
    />
    <WorkItem 
        title="Student Technician" 
        company="Texas A&M High Performance Research Computing" 
        summary="<p>As a student technician I was responsible for helping researchers, creating and 
        maintaining ticket automation software, and training new technicians.</p><br>
        <p>Most of the issues I assisted with involved helping users set up their environment on one or more clusters on Linux (CentOS). These issues ranged from guiding machine learning
        researchers in configuring their Python environments to utilize our GPUs, to assisting aerospace researchers in running their decade-old Fortran code on hundreds of CPU cores.</p><br>
        <p>The automation software I helped write and maintain involved creating and automating ticket workflows. The software consisted of two frontends: 1) a form on our website where users 
        could submit requests and 2) a shortcut in slack which allowed hprc staff to create requests on behalf of users. When a request is made, an https request is made to the bot, and the bot decides 
        what should happen to the request next. This decision is made based on the type of request being made, the current step of the request, and the workflow for said request type. These workflows 
        can be created, read, updated, and deleted via a command line interface. The bot sends updates to slack where HPRC staff can choose to advance the step. This process of updating and receiving 
        requests continues until a terminal step in the workflow is reached, at which point the request is marked as resolved.</p>
        <br>
        <p>I was responsible for refactoring the bot such that it could read in and use workflows, and I was responsible for creating the command line 
        interface for managing workflows. I also fixed many of the bot's bugs. The bot was written in Python, and has handled 1081 tickets since it's creation.</p>"
        start="5/2023"
        end="N/A"
    />
    <WorkItem    
        title="Software Developer"
        company="AKW Ventures"
        summary='<p>As a software developer at AKW Ventures I worked on several different projects, including: an iOS application for college football, a web application for automatically 
            filling out a google document with chatgpt, and a custom gpt for reading and drafting emails for your gmail account.</p><br>
            <p>The iOS application I helped develop is available on the app store here: <a href="https://apps.apple.com/us/app/college-football-schedules-23/id1028810756" class="underline text-blue-500 hover:text-blue-700">https://apps.apple.com/us/app/college-football-schedules-23/id1028810756</a>. 
            I was responsible for managing the cloudkit database and pulling college football data from various endpoints.</p><br>
            <p>The web application I developed was an internal tool designed to make the process of creating white papers easy. This website was created with vue.js, python, flask, google apis, and openai apis. I 
            was the sole developer for this application.</p>
            <br>
            <p>The custom gpt I created was another internal tool. This tool was created to help us answer support emails for the college football app. This was created using openai customgpt and by 
            creating my own endpoints for google authentication, retrieving/filtering emails from a users inbox, and for drafting emails. The endpoints were created with python and the FastAPI framework</p>
            '
        start="5/2023"
        end="N/A"
    />
    <WorkItem
        title="Overnight Stocker"
        company="Kroger"
        summary="<p>As an overnight stocker at Kroger, I was responsible for unloading trucks and stocking shelves between 12 and 8 am on 5 random nights of the week.</p>"
        start="5/2022"
        end="8/2022"
    />
    <WorkItem
        title="Tennis Coach"
        company="Kings Court Tennis Academy"
        summary="<p>As a coach at Kings Court, I was responsible for putting together practice plans and teaching people how to play tennis. My class sizes ranged from 2 to 30 and the ages I taught 
        ranged from 12 to 74.</p>"
        start="5/2020"
        end="8/2021"
    />
    <WorkItem
        title="Math Instructor"
        company="Mathnasium"
        summary="<p>As an instructor at Mathnasium, I was responsible for teaching kids math. My class sizes ranged from 1-4 and the ages I taught ranged from 8 to 16.</p>"
        start="5/2020"
        end="8/2021"
    />
    </div>
</template>
<script setup>
import WorkItem from '../components/WorkItem.vue'
</script>