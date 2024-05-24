<template>
<div class="max-w-4xl max-h-screen mx-auto p-4 bg-black h-screen">
    <iframe
    ref="pygameFrame"
    :src="iframeSrc"
    class="w-full h-3/4"
    frameborder="0"
    ></iframe>
</div>
</template>
<script setup>
import { onMounted, ref } from 'vue';
const pygameFrame = ref(null);
const iframeSrc = ref('/pygbag_assets/index.html');
const loadPygame = () => {
        if (pygameFrame.value) {
        pygameFrame.value.onload = () => {
            console.log('Pygame is ready in iframe');
        };
    }
}
onMounted(() => {
    loadPygame();
})
</script>