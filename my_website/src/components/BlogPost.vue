<template>
  <div class="max-w-md mx-auto p-4 bg-white rounded-lg shadow-md">
    <h1 class="text-2xl font-bold text-gray-800 mb-2">{{ props.title }}</h1>
    <p class="text-gray-600 mb-4">{{ props.msg }}</p>
    <div class="mb-4">
      <p class="text-gray-700 mb-2">Likes: <span class="font-semibold">{{ likes }}</span></p>
      <button 
        @click="like" 
        :disabled="liked" 
        class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 disabled:bg-blue-300 disabled:cursor-not-allowed">
        Like
      </button>
    </div>
    <div class="mb-4">
      <p class="text-gray-700 mb-2">Dislikes: <span class="font-semibold">{{ dislikes }}</span></p>
      <button 
        @click="dislike" 
        :disabled="disliked" 
        class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 disabled:bg-blue-300 disabled:cursor-not-allowed">
        Dislike
      </button>
    </div>
    <button 
      @click="delete_post" 
      v-if="is_admin" 
      class="px-4 py-2 bg-gray-800 text-white rounded hover:bg-gray-900">
      Delete
    </button>
  </div>
</template>
<script setup>
  import { defineProps, ref } from "vue";
  import { del_post, like_post, dislike_post } from '../helper/request.js'
  import { check_admin } from '../helper/permissions.js'
  const props = defineProps({
    likes: Number,
    dislikes: Number,
    title: String,
    msg: String,
    p_key: String,
    s_key: String,
    liked: Boolean,
    disliked: Boolean
  });
  let likes = ref(props.likes)
  let dislikes = ref(props.dislikes)
  let liked = ref(props.liked)
  let disliked = ref(props.disliked)
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
  function like(){
    if(disliked.value){
      disliked.value = false
      dislikes.value -= 1
    }
    if(liked.value){
      return;
    }
    likes.value += 1
    liked.value = true;
    like_post(props.s_key)
  }
  function dislike(){
    if(liked.value){
      liked.value = false
      likes.value -= 1
    }
    if(disliked.value){
      return
    }
    dislikes.value += 1
    disliked.value = true
    dislike_post(props.s_key)
  }
</script>