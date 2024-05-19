<template>
    <h1>Keegan's Blog</h1>
    <p v-if="not_loaded">Loading...</p>
    <div id="posts">
        <BlogPost v-for="(item, index) in posts" 
        :key="index" 
        :title="item.title"
        :msg="item.msg"
        :likes="item.likes"
        :dislikes="item.dislikes" 
        :p_key="item.p_key"
        :s_key="item.s_key"
        />
    </div>
</template>
<script setup>
import BlogPost from './BlogPost.vue'
import { ref, onMounted } from 'vue'
import { get_request } from '@/helper/request';
let posts = ref([])
let not_loaded = ref(true);
onMounted(() => {
    not_loaded = true;
    get_request("get_posts", sessionStorage.getItem('token'), sessionStorage.getItem('refresh')).then((data) =>{
        posts.value = data
        not_loaded = false
    })
})

</script>