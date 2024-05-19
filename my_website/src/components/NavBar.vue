<script setup>
import { check_admin } from '../helper/permissions';
const is_admin = check_admin()
</script>
<template>
    <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/blog">Blog</RouterLink>
        <RouterLink to="/projects">Projects</RouterLink>
        <RouterLink to="/new_post" v-if="is_admin">New Post</RouterLink>
        <RouterLink to="/login">Login</RouterLink>
    </nav>
</template>