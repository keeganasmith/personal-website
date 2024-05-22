<template>
    <h1 class="text-4xl font-bold text-center mb-8">Keegan's Blog</h1>
    <p v-if="not_loaded" class="text-center text-gray-400">Loading...</p>
    <div id="posts" class="space-y-4">
        <BlogPost 
            v-for="(item, index) in posts" 
            :key="index" 
            :title="item.title"
            :msg="item.msg"
            :likes="item.likes"
            :dislikes="item.dislikes"
            :liked="item.liked"
            :disliked="item.disliked" 
            :p_key="item.p_key"
            :s_key="item.s_key"
        />
    </div>
</template>
<script setup>
import BlogPost from './BlogPost.vue'
import { ref, onMounted } from 'vue'
import { get_posts, get_user } from '../helper/request.js';
import { notify } from "@kyvg/vue3-notification";
import { useRouter } from 'vue-router';
const router = useRouter();
let posts = ref([])
let not_loaded = ref(true);
let likes = ref(new Set())
let dislikes = ref(new Set())
onMounted(() => {
    not_loaded = true;
    get_user().then((data) =>{
        console.log(data)
        likes.value = new Set(data["liked_posts"])
        dislikes.value = new Set(data["disliked_posts"])
        
        get_posts().then((data) =>{
            posts.value = data
            for(let i = 0; i < posts.value.length; i++){
                posts.value[i]["liked"] = false;
                posts.value[i]["disliked"] = false;
                let s_key = posts.value[i]["s_key"]
                if(likes.value.has(s_key)){
                    posts.value[i]["liked"] = true;
                }
                if(dislikes.value.has(s_key)){
                    posts.value[i]["disliked"] = true;
                }
            }
            not_loaded = false
        })
    }).catch(() => {
        notify({
            title: "Not Authorized",
            text: "Howdy, your access token has expired, please try logging out and logging back in again.",
        });
        router.push('/login');
    });

    

})

</script>