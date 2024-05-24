<!-- src/App.vue -->
<template>
  <div class="bg-black min-h-screen min-w-screen overflow-hidden">
    <NavBar></NavBar>
    <div class="bg-black min-h-screen min-w-screen text-white">
      <div class="container mx-auto p-4">
        <notifications class="custom-notifications" />
        <RouterView></RouterView>
      </div>
    </div>
  </div>
</template>

<script setup>
import NavBar from './components/NavBar.vue';
</script>

<style scoped>
html, body {
  margin: 0;
  padding: 0;
  overflow-x: hidden; 
  overflow-y: hidden;
  width: 100%;
  height: 100%;
  box-sizing: border-box; /* Include padding and border in the element's total width and height */
}
.custom-notifications {
  position: fixed;
  top: 60px; /* Adjust based on the height of your NavBar */
  left: 50%;
  transform: translateX(-50%);
  z-index: 1000;
  width: auto; /* Adjust or remove to fit your design */
  padding: 0 20px;
  box-sizing: border-box;
}

.notification {
  display: flex;
  justify-content: center;
}
</style>
