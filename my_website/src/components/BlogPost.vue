<template>
    <h1>{{ props.title }}</h1>
    <p>{{ props.msg }}</p>
    <p>Likes: {{ props.likes }}</p>
    <p>Dislikes: {{ props.dislikes }}</p>
    <button @click="delete_post" v-if="is_admin">Delete</button>
</template>
<script setup>
  import { defineProps } from "vue";
  import { del_post } from '../helper/request.js'
  import { check_admin } from '../helper/permissions.js'
  const props = defineProps({
    likes: Number,
    dislikes: Number,
    title: String,
    msg: String,
    p_key: String,
    s_key: String
  });
  const is_admin = check_admin()
  function delete_post(){
    try{
      del_post(props.p_key, props.s_key, sessionStorage.getItem('token'), sessionStorage.getItem('refresh')).then(() => {
        window.location.reload();
      })
    } catch (error) {
      console.error('Error deleting post:', error);
    }
  }
</script>