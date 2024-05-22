<!-- src/App.vue -->
<template>
  <div>
    <NavBar></NavBar>
    <div class="bg-black min-h-screen text-white">
      <div class="container mx-auto p-4></div>">
      <notifications class="custom-notifications" />
      <RouterView></RouterView>
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue';

export default {
  components: {
    NavBar
  }
};
</script>

<style scoped>
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
