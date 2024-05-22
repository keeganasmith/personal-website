<template>
    <div class="box w-lg py-4 px-4">
      <h1 class="text-3xl font-bold text-left mb-8">{{ title }}</h1>
      <img v-if="image1Src" :src="image1Src" alt="Project Image 1" class="mb-4">
      <img v-if="image2Src" :src="image2Src" alt="Project Image 2" class="mb-4">
      <div v-html="summary" class="prose mb-4"></div>
      <p>Project start date: {{ start }}</p>
      <p>Source code: <a :href="source" target="_blank" class="underline text-blue-500 hover:text-blue-700">{{ source }}</a></p>
    </div>
  </template>
  
  <script setup>
  import { defineProps, computed } from 'vue';
  
  const props = defineProps({
    title: String,
    summary: String,
    image1: String,
    image2: String,
    source: String,
    start: String
  });
  
  const image1Src = computed(() => {
    return props.image1 ? require(`@/assets/${props.image1}`) : '';
  });
  
  const image2Src = computed(() => {
    return props.image2 ? require(`@/assets/${props.image2}`) : '';
  });
  </script>
  
  <style scoped>
  /* Add any additional styles here if necessary */
  </style>
  