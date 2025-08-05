<template>
    <div class="bg-gray-800">
        <nav class="container p-4 mx-auto md:flex md:justify-between md:items-center">
            <div class="flex items-center justify-between w-full">
                <router-link to="/" class="text-white px-3 py-2 rounded-md text-base font-medium hover:bg-gray-700">About Me</router-link>
                <div @click="toggleNav" class="flex md:hidden">
                    <button type="button" class="text-gray-100 hover:text-gray-400 focus:outline-none focus:text-gray-400">
                        <svg viewBox="0 0 24 24" class="w-6 h-6 fill-current">
                            <path fill-rule="evenodd"
                                d="M4 5h16a1 1 0 0 1 0 2H4a1 1 0 1 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2z">
                            </path>
                        </svg>
                    </button>
                </div>
            </div>

            <ul :class="showMenu ? 'flex' : 'hidden'" class="flex-col mt-8 space-y-4 md:flex md:space-y-0 md:flex-row md:items-center md:space-x-10 md:mt-0">
                <router-link to="/byteboost25" class="text-white px-3 py-2 rounded-md text-base font-medium hover:bg-gray-700">Byteboost 25</router-link>
                <router-link to="/blog" class="text-white px-3 py-2 rounded-md text-base font-medium hover:bg-gray-700">Blog</router-link>
                <router-link to="/projects" class="text-white px-3 py-2 rounded-md text-base font-medium hover:bg-gray-700">Projects</router-link>
                <router-link to="/experience" class="text-white px-3 py-2 rounded-md text-base font-medium hover:bg-gray-700">Work Experience</router-link>
                <router-link to="/blocktd" class="text-white px-3 py-2 rounded-md text-base font-medium hover:bg-gray-700">Block TD</router-link>
                <router-link to="/contact" class="text-white px-3 py-2 rounded-md text-base font-medium hover:bg-gray-700">Contact Me</router-link>
                <router-link to="/new_post" v-if="is_admin" class="text-white px-3 py-2 rounded-md text-base font-medium hover:bg-gray-700">New Post</router-link>
                <router-link to="/login" class="text-white px-3 py-2 rounded-md text-base font-medium hover:bg-gray-700">Login</router-link>
            </ul>
        </nav>
    </div>
</template>
<script setup>
import { ref } from "vue";
import { check_admin } from '../helper/permissions';
const is_admin = check_admin()
let showMenu = ref(false);
const toggleNav = () => {
    showMenu.value = !showMenu.value
}

</script>
<!-- <script setup>
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
                <RouterLink to="/experience" class="text-white px-3 py-2 rounded-md text-sm font-medium hover:bg-gray-700">Work Experience</RouterLink>
                <RouterLink to="/blocktd" class="text-white px-3 py-2 rounded-md text-sm font-medium hover:bg-gray-700">Block TD</RouterLink>
                <RouterLink to="/contact" class="text-white px-3 py-2 rounded-md text-sm font-medium hover:bg-gray-700">Contact</RouterLink>

                <RouterLink to="/new_post" v-if="is_admin" class="text-white px-3 py-2 rounded-md text-sm font-medium hover:bg-gray-700">New Post</RouterLink>

            </div>
            <div>
                <RouterLink to="/login" class="text-white px-3 py-2 rounded-md text-sm font-medium hover:bg-gray-700">Login</RouterLink>
            </div>
        </div>
    </nav>
</template> -->