<script setup>
import { check_admin } from '../helper/permissions';
const is_admin = check_admin()
</script>
<template>
     <nav class="bg-gray-800 p-4">
        <div class="container mx-auto flex justify-between items-center">
            <div class="flex space-x-4">
                <RouterLink to="/" class="text-white px-3 py-2 rounded-md text-sm font-medium hover:bg-gray-700">Home</RouterLink>
                <RouterLink to="/blog" class="text-white px-3 py-2 rounded-md text-sm font-medium hover:bg-gray-700">Blog</RouterLink>
                <RouterLink to="/projects" class="text-white px-3 py-2 rounded-md text-sm font-medium hover:bg-gray-700">Projects</RouterLink>
                <RouterLink to="/new_post" v-if="is_admin" class="text-white px-3 py-2 rounded-md text-sm font-medium hover:bg-gray-700">New Post</RouterLink>
            </div>
            <div>
                <RouterLink to="/login" class="text-white px-3 py-2 rounded-md text-sm font-medium hover:bg-gray-700">Login</RouterLink>
            </div>
        </div>
    </nav>
</template>