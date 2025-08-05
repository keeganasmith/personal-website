<template>
  <div class="p-4">
    <form @submit.prevent="submitForm" class="space-y-4">
      <div>
        <label for="title" class="block text-sm font-medium text-white">Title:</label>
        <input type="text" v-model="title" id="title" class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm text-black">
      </div>
      <div>
        <label for="msg" class="block text-sm font-medium text-white">Message:</label>
        <textarea v-model="msg" id="msg" class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm h-32 text-black"></textarea>
      </div>
      <button type="submit" class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">Submit</button>
    </form>
    <p v-if="submitted" class="mt-4 text-green-600">Submitted with title: {{ prev_title }}, message: {{ prev_msg }}</p>
    <p v-if="error" class="mt-4 text-red-600">There was an error posting, see logs</p>
  </div>
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