<template>
    <div>
      <h1 class="text-4xl font-bold text-center mb-8">Keegan's Projects</h1>
      <p class="text-center">Below is a list of projects I have worked on. If you would like a live demo of any of these projects, please reach out to me.</p>
      <ProjectItem
        title="This Website"
        summary="<p>This website was built using Vue.js and Tailwind CSS. It showcases my projects and provides a platform for me to share my work.</p>"
        image=""
        source="https://github.com/your-repo"
        start="January 1, 2023"
      />
    </div>
  </template>
  
  <script setup>
  import ProjectItem from './ProjectItem.vue';
  </script>