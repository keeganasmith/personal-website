<template>
  <div class="box max-w-2x1 mx-auto p-4 bg-black">
    <h1 class="text-2xl font-bold text-white mb-2">{{ props.title }}</h1>
    <p class="text-white mb-4">{{ props.msg }}</p>
    <div class="flex space-x-4 mb-4">
      <div class="w-1/4">
        <p class="text-white mb-2">Likes: <span class="font-semibold">{{ likes }}</span></p>
      </div>
      <div class="w-1/4">
        <p class="text-white mb-2">Dislikes: <span class="font-semibold">{{ dislikes }}</span></p>
      </div>
    </div>
    <div class="flex space-x-4 mb-4">
      <button 
        @click="like" 
        :disabled="liked" 
        class="w-1/4 px-4 py-2 border border-white text-white bg-transparent rounded hover:bg-white hover:text-black disabled:border-gray-500 disabled:text-gray-500 disabled:bg-transparent disabled:cursor-not-allowed">
        Like
      </button>
      <button 
        @click="dislike" 
        :disabled="disliked" 
        class="w-1/4 px-4 py-2 border border-white text-white bg-transparent rounded hover:bg-white hover:text-black disabled:border-gray-500 disabled:text-gray-500 disabled:bg-transparent disabled:cursor-not-allowed">
        Dislike
      </button>
      <button 
        @click="delete_post" 
        v-if="is_admin" 
        class="w-1/4 px-4 py-2 border border-white text-white bg-transparent rounded hover:bg-white hover:text-black disabled:border-gray-500 disabled:text-gray-500 disabled:bg-transparent disabled:cursor-not-allowed">
        Delete
      </button>
    </div>
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