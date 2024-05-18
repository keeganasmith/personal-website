<script setup>
import GoogleSigin from './GoogleSignin.vue'
</script>
<template>
    <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/blog">Blog</RouterLink>
        <RouterLink to="/projects">Projects</RouterLink>
        <RouterLink to="/new_post">New Post</RouterLink>
        <GoogleSigin />
    </nav>
</template>