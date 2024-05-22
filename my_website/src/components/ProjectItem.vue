<template>
    <div class="box w-lg py-4 px-4">
        <h1 class="text-3xl font-bold text-left mb-8">{{ props.title }}</h1>
        <img v-if="props.image" :src="props.image" alt="Project Image">
        <div v-html="props.summary"></div>
        <p>Project Started on {{ props.start }}.</p>
        <p>Source code: <a :href="props.source" target="_blank">{{ props.source }}</a></p>
    </div>
  </template>
  
  <script setup>
  import { defineProps } from 'vue';
  
  const props = defineProps({
    title: String,
    summary: String,
    image: String,
    source: String,
    start: String
  });
  
  </script>