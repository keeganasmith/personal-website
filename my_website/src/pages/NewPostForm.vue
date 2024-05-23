<template>
    <form @submit.prevent = "submitForm">
      <label for="title">Title:</label>
      <input type="text" v-model="title" id="title">
      <label for="msg">Message:</label>
      <input type="text" v-model="msg" id="msg">
      <button type="submit">Submit</button>
    </form>
    <p v-if="submitted">Submitted with title: {{ prev_title }}, message: {{ prev_msg }}</p>
    <p v-if="error">There was an error posting, see logs</p>
  </template>
  
<script setup>
import { ref } from 'vue'
import { new_post } from '../helper/request.js'
let title = ref('')
let msg = ref('')
let prev_title = ref('')
let prev_msg = ref('')
let submitted = ref(false)
let error = ref(false)
const submitForm = () => {
    try{
        new_post(title.value, msg.value, sessionStorage.getItem('token'), sessionStorage.getItem('refresh'))
        prev_title.value = title.value
        prev_msg.value = msg.value
        title.value = "";
        msg.value = ""
        submitted = true;
    }
    catch{
        error = true;
    }

}
</script>