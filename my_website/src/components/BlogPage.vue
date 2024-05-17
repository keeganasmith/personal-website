<template>
    <h1>Keegan's Blog</h1>
    <div id="posts">
        <BlogPost v-for="(item, index) in posts" 
        :key="index" 
        :title="item.title"
        :msg="item.msg"
        :likes="item.likes"
        :dislikes="item.dislikes" 
        />
    </div>
    <button @click="new_post">New Post</button>
</template>
<script setup>
import BlogPost from './BlogPost.vue'
import { ref, onMounted } from 'vue'
import { get_request } from '@/helper/request';
let posts = ref([])

onMounted(() => {
    get_request("get_posts").then((data) =>{
        posts.value = data
    })
})
function new_post(){

}
</script>