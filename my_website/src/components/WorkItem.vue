<template>
    <div class="box max-w-3xl mx-auto p-4 bg-black">
        <h1 class="text-2xl font-bold text-white mb-2">{{ props.title }} at {{ props.company }}</h1>
        <div v-html="props.summary" class="prose mb-4"></div>
        <p>Started: {{ props.start }}</p>
        <p>Ended: {{ props.end }}</p>
    </div>
</template>
<script setup>
import { defineProps } from 'vue';

const props = defineProps({
  title: String,
  company: String,
  summary: String,
  start: String,
  end: String
});
</script>