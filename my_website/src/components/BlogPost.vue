<template>
    <h1>{{ props.title }}</h1>
    <p>{{ props.msg }}</p>
    <p>Likes: {{ props.likes }}</p>
    <p>Dislikes: {{ props.dislikes }}</p>
</template>
<script setup>
  import { defineProps } from "vue";
  const props = defineProps({
    likes: Number,
    dislikes: Number,
    title: String,
    msg: String,
  });
</script>